# xAI Analysis of TimeLDM for Time Series Generation

**Authors:** Iliass Khoutaibi, Théo Basséras

This project studies **latent diffusion models for multivariate time series generation** on a controlled synthetic dataset of sine waves.  
The goal is twofold:

1. generate realistic multivariate time series with a **Latent Diffusion Model (LDM)**,
2. analyze the learned latent space through **explainability tools** such as saliency, counterfactuals, Sobol sensitivity, latent perturbations, and ablation.

---

## Overview

We consider multivariate time series of shape

$$
x \in \mathbb{R}^{T \times D}
$$

with:

- `T = 24` time steps
- `D = 5` channels

Each channel is a sine wave with its own characteristic frequency distribution. This synthetic setup makes it possible to evaluate not only generation quality, but also whether the model captures **spectral structure**, **channel dependencies**, and **interpretable latent factors**.

---

## Project structure

The notebook is organized into five main parts:

1. **Visualization utilities**  
   Functions for plotting generated samples, frequency spectra, t-SNE projections, and KDE comparisons.

2. **Synthetic dataset generation**  
   Creation of multivariate sine-wave datasets with structured frequency variations.

3. **Evaluation metrics**  
   Statistical and downstream metrics to compare real and generated data.

4. **Two generative implementations**
   - **Implementation 1**: Transformer-VAE + Latent Diffusion
   - **Implementation 2**: Improved TimeLDM with architectural and optimization refinements

5. **Explainability analysis**
   - Saliency maps
   - Counterfactual generation
   - Sobol sensitivity indices
   - Series perturbation
   - Latent ablation

---

## Dataset

The dataset is composed of synthetic multivariate sine waves:

$$
x_t^{(j)} = \sin(f_j t + \phi_j)
$$

where:

- $f_j$ is the frequency of channel $j$
- $\phi_j \sim \mathcal{U}(0, 2\pi)$ is a random phase

The mean frequencies are:

$$
\mu = [0.3,\; 0.6,\; 3.8,\; 1.2,\; 2.4]
$$

with Gaussian perturbations around these values.

This dataset is useful because the true underlying structure is known, which makes it possible to study:

- periodicity preservation,
- spectral fidelity,
- latent controllability,
- interpretability of learned representations.

---

## Method 1 — Transformer VAE + Latent Diffusion

The first implementation follows a two-stage pipeline.

### Stage 1: Variational Autoencoder

A Transformer-based VAE encodes each input sequence into a latent representation:

$$
z_0 \sim q_\phi(z \mid x)
$$

and reconstructs the signal through a decoder:

$$
\hat{x} = D_\xi(z_0)
$$

The VAE objective combines:

- reconstruction loss,
- L1/L2 penalties,
- FFT reconstruction loss,
- KL regularization.

### Stage 2: Latent Diffusion

After training the VAE, latent vectors are extracted and used to train a diffusion model in latent space.  
The diffusion model learns to denoise noisy latent variables and generate new latent trajectories, which are then decoded back into time series.

This implementation provides a strong baseline with good signal fidelity, but the explainability experiments suggest that its latent space remains only **weakly disentangled**.

---

## Method 2 — Improved TimeLDM

The second implementation introduces several improvements:

- larger latent dimension (`16 -> 32`)
- larger diffusion network
- timestep conditioning by concatenation
- spectral normalization
- normalization layers
- dropout
- residual connections
- AdamW optimizer
- Xavier initialization
- KL warmup strategy

These changes improve training stability and latent diversity, but may also increase output noise and slightly reduce temporal coherence.  
This illustrates a classical trade-off between **diversity** and **signal fidelity**.

---

## Evaluation metrics

The notebook evaluates generated data using several complementary metrics:

### 1. Context-FID
A Fréchet-style distance computed on handcrafted statistical features such as:

- mean
- standard deviation
- skewness
- kurtosis
- autocorrelation
- FFT-based descriptors

Lower is better.

### 2. Correlational score
Measures whether cross-channel dependencies are preserved between real and generated data.

Lower is better.

### 3. Discriminative score
A classifier is trained to distinguish real from synthetic samples.

A score close to zero means generated data is difficult to distinguish from real data.

### 4. Predictive score
A Train-on-Synthetic-Test-on-Real setup evaluates whether generated data is useful for downstream forecasting.

Lower is better.

---

## Explainability analysis

A major contribution of this notebook is the use of **xAI tools** to analyze the latent diffusion model.

### Saliency analysis
Gradient-based saliency is used to identify which latent coordinates most influence specific output properties.

### Counterfactual explanations
Counterfactual latent codes are optimized to enforce structured output changes, such as **swapping two output channels** while keeping the latent representation close to the original one.

This helps test whether channel-specific information is localized in latent space.  
In practice, channel swapping is only partially successful, suggesting that the latent representation is **not strongly disentangled**.

### Sobol sensitivity
Sobol indices are used as a global sensitivity analysis tool to quantify the contribution of each latent channel to a scalar feature of the generated signal.

Results indicate that most latent channels have weak isolated influence, and that generation relies more on **distributed interactions** than on a few dominant coordinates.

### Series perturbation
Individual latent channels are incremented or decremented to observe how the output changes.

This reveals which latent directions correspond to smooth variations and which lead to unstable or collapsed generations.

### Latent ablation
Latent channels are set to zero one at a time to test redundancy and robustness.

The fact that many ablating operations induce only minor changes suggests that information is spread across multiple dimensions.

---

## Main takeaways

- Latent diffusion can generate realistic multivariate synthetic time series.
- The synthetic sine-wave setup is useful for probing spectral and structural behavior.
- The first implementation achieves strong fidelity.
- The improved implementation offers better stability and diversity.
- Explainability experiments consistently suggest that the learned latent space is **only weakly disentangled**.
- Information is distributed across multiple latent dimensions rather than being encoded in isolated, interpretable factors.

---

## Running the notebook

Clone the repository and open the notebook:

```bash
git clone https://github.com/KHOUTAIBI/xPlainableDiffusionModels
cd xPlainableDiffusionModels
