# Time Series — Structured Modeling & Learning

This repository gathers a set of projects focused on **modeling, generating, and understanding structured temporal data**.

The central question explored across all projects is:

> *How can we extract, represent, and manipulate the underlying structure of high-dimensional time series?*

Rather than treating time series as sequences of points, this work approaches them as **structured objects** governed by:
- latent variables,
- geometric constraints,
- sparse patterns,
- and non-linear dependencies.

---

## Core Themes

The projects in this repository revolve around:

- **Latent variable modeling**  
  Learning compressed representations that capture underlying dynamics

- **Generative processes**  
  Simulating realistic trajectories from learned distributions

- **Geometric learning**  
  Handling temporal misalignment and invariances

- **Sparse structure discovery**  
  Identifying dominant patterns in complex signals

- **Extreme event modeling**  
  Understanding rare but high-impact behaviors

- **Learning under constraints**  
  Few-shot and low-data regimes

---

## Projects

---

### 1. Latent Diffusion Models for Time Series

📁 `diffusion models / Time series in latent space`

This project studies **latent diffusion models (LDMs)** for multivariate time series.

#### Approach
- Encode sequences into latent variables using a Transformer-VAE
- Learn a diffusion process in latent space
- Decode generated latent trajectories into signals

#### Key observations
- Generated sequences preserve **spectral and structural properties**
- The latent space is **distributed rather than disentangled**
- No single latent dimension controls a clear interpretable factor

#### Additional contribution
A detailed **analysis of the latent space** using:
- sensitivity analysis (Sobol indices)
- counterfactual optimization
- latent perturbations and ablations

This provides insight into how generative models internally represent temporal structure.

---

### 2. Pattern Extraction & Sparse Representation

📁 `feature engineering / pattern extraction`

This project explores whether complex time series can be approximated by a small number of components.

#### Result
> A large proportion (~90%) of a signal can be reconstructed using only 2–3 dominant patterns

#### Interpretation
- Time series often lie on a **low-dimensional manifold**
- Structure can be separated from noise through sparse representations

#### Implications
- Efficient compression
- Interpretability of signals
- Identification of dominant modes of variation

---

### 3. Few-Shot Learning with Metric-Based Representations

📁 `Few shot learning for clustering with HUBERT`

This project studies **few-shot learning** using:

- self-supervised representations (HuBERT)
- Prototypical Networks

#### Method
- Embed signals into a representation space
- Compute class prototypes from few examples
- Classify by nearest-prototype matching

#### Findings
- Strong generalization to **unseen classes**
- Robust performance in **low-data regimes**
- Metric structure is more important than classifier complexity

---

### 4. Forecasting with Geometry-Aware Losses

📁 `Forecast time series with soft DTW`

This project investigates forecasting using **Soft-DTW**, a differentiable alignment-based loss.

#### Motivation
Standard losses assume strict temporal alignment, which is often unrealistic.

#### Contribution
- Learning under **temporal invariance**
- Robustness to shifts and local distortions

#### Insight
Comparing sequences requires accounting for their **geometry**, not just pointwise differences.

---

### 5. Modeling Cascades with Extreme Value Theory

📁 `Predicting Cascade Failures`

This project focuses on **multivariate extreme events** and their propagation.

#### Problem
When a large deviation occurs in one component:
→ how does it affect the rest of the system?

#### Approach
- Extreme Value Theory
- Sparse dependency modeling

#### Insight
Rare events are governed by **structured dependencies**, not independent fluctuations.

---

### 6. Fundamental Frequency Estimation under Noise

📁 `Pitch estimation / CREPE vs DSP`

This project studies the problem of **recovering periodic structure in noisy temporal signals**, 
through a comparison between:

- classical signal processing methods (Autocorrelation, YIN),
- and learned models (CREPE).

#### Focus
- robustness to stochastic and structured noise
- stability of temporal estimates
- behavior under regime shifts (voiced / unvoiced transitions)

#### Key insights
- Learned models achieve strong accuracy and stability in structured regimes
- Classical methods remain competitive for **binary structure detection**
- All approaches exhibit failure modes under:
  - rapid regime transitions
  - multi-source interference
  - distribution shifts

## Interpretation

Beyond predictive accuracy, the experiments reveal that model behavior is governed by the structural assumptions under which inference is performed.

Three assumptions appear central:

- **Rapid regime transitions** introduce instability because estimators require adaptation time before recovering reliable structure.

- **Multi-source interference** violates the assumption of a single dominant underlying pattern, producing ambiguous estimates and degraded performance.

- **Distribution shifts** expose the dependence of learned representations on the statistical properties observed during training.

This highlights an important principle:

> **model robustness depends on the validity of its assumptions about the data-generating process**

The project therefore emphasizes not only empirical performance, but also the relationship between:
- model assumptions,
- structural regimes,
- and generalization behavior.

---

### 7. Few-Shot Learning for Structured Signal Classification

📁 `Few shot pour la classification de signaux`

This project investigates **learning from extremely limited labeled data** in high-dimensional temporal signals using metric-based representations.

#### Objective
Train a model on a set of base classes, then generalize to entirely new classes with only a handful of examples per class.

#### Approach

The project explores three complementary strategies:

- **Supervised representation learning**
  - Train a convolutional encoder on base classes
  - Use the learned embedding space for downstream generalization

- **Prototype-based inference**
  - Compute class representatives (prototypes) from few samples
  - Classify by nearest-prototype distance in embedding space

- **Episodic training (Prototypical Networks)**
  - Simulate low-data scenarios during training
  - Learn representations explicitly optimized for few-shot transfer

#### Key components

- 1D CNN encoders for multichannel temporal signals
- Metric learning using Euclidean distances in embedding space
- Prototype construction via class-wise averaging
- Episodic sampling (N-way, K-shot tasks)
- Evaluation across multiple shot regimes (1, 3, 5, 10)

#### Findings

- Strong generalization to unseen classes with minimal data
- Performance depends primarily on the **structure of the embedding space**
- Simple distance-based classifiers outperform complex parametric heads in low-data regimes
- Episodic training significantly improves robustness to distribution shifts

#### Insight

> When data is scarce, **learning a good geometry is more important than learning a complex decision boundary**

This project highlights that classification can be reframed as:
- learning a representation space,
- where similarity directly encodes semantic structure.

#### Extensions explored

- Deep prototypical networks with regularization
- Embedding space visualization (t-SNE)
- Distance distribution analysis (intra vs inter-class)
- Residual architectures for segment-based encoding

#### Relevance

This work emphasizes:
- fast adaptation to new patterns,
- robustness under limited supervision,
- and efficient representation learning in high-dimensional settings.


---



## Key Takeaways

- High-dimensional time series exhibit **hidden structure**
- Latent representations are powerful but often **entangled**
- Geometry plays a crucial role in comparing temporal data
- A small number of components can explain complex signals
- Rare events require dedicated modeling beyond standard assumptions
- Generalization under limited data is a central challenge

---

## Author

**Théo Basséras**

Background in mathematics, machine learning, and engineering.  
Interested in:
- stochastic systems
- generative modeling
- representation learning
- high-dimensional data

---

## Final Remark

This repository reflects an effort to move from:

> *modeling observations*

to

> **understanding the structure that generates them**