# Fundamental Frequency Estimation under Noise  
### Classical Signal Processing vs Learned Models

This project studies the problem of **recovering periodic structure in noisy temporal signals**, 
through a comparative analysis of classical signal processing methods and deep learning models.

---

## Overview

Given a time-dependent signal \( x(t) \), the objective is to estimate its **fundamental frequency** \( f_0 \), 
which corresponds to its dominant periodic component.

While conceptually simple, this problem becomes challenging in practice due to:
- noise,
- non-stationarity,
- regime changes,
- and interference from competing sources.

---

## Methods

Three fundamentally different approaches are evaluated:

### 1. Autocorrelation
- Direct exploitation of periodicity
- Detects repeating patterns via lag similarity

### 2. YIN Algorithm
- Refined difference-based method
- Reduces bias and improves stability over autocorrelation

### 3. CREPE (Deep Learning)
- Convolutional neural network operating on raw waveforms
- Learns representations of periodic structure from data

---

## Experimental Design

The methods are evaluated under controlled degradations:

### Noise models
- White noise (fully stochastic)
- Pink noise (1/f structure)
- Brown noise (low-frequency dominant)
- Structured harmonic interference

### Evaluation criteria
- Stability (variance of estimates)
- Accuracy (MSE, RPA)
- Robustness across signal-to-noise ratios
- Binary structure detection (voiced vs unvoiced)

---

## Key Results

### 1. Stability vs Noise

- **CREPE** shows strong stability under stochastic noise  
- **YIN** degrades progressively  
- **Autocorrelation** becomes highly unstable  

However:

- Structured interference (harmonic noise) causes **catastrophic failure** in learned models

---

### 2. Precision vs Structure

- CREPE achieves near-perfect precision on clean signals  
- Classical methods exhibit higher variance but more predictable behavior  

---

### 3. Regime Transitions

All methods fail to correctly resolve **short transitions** between structured and unstructured regimes:

> Window-based estimation introduces intrinsic latency and contamination effects

---

### 4. Binary Structure Detection

Surprisingly:

- Autocorrelation performs best for detecting the **presence of periodicity**
- Learned models are more accurate but less reliable near decision boundaries

---

## Key Insights

### 1. Structure vs Noise

Accurate estimation relies less on model complexity than on:
- the presence of a stable periodic structure,
- and its separation from noise.

---

### 2. Learned vs Analytical Models

- Learned models capture complex structure but are **sensitive to distribution shifts**
- Analytical methods are less precise but more **robust to unexpected regimes**

---

### 3. Failure Modes Matter

All methods exhibit systematic failures:

- transition regions (temporal mixing)
- multi-source interference
- purely stochastic inputs

These are not implementation issues but **intrinsic limitations of the modeling assumptions**

---

## Takeaway

This project reframes pitch estimation as a more general problem:

> **inferring hidden structure in noisy, non-stationary signals**

and highlights the trade-offs between:
- accuracy,
- robustness,
- and interpretability.

---

## Contents

- Implementation of Autocorrelation, YIN, and CREPE
- Experimental framework with multiple noise models
- Statistical evaluation (variance, MSE, RPA)
- Analysis of failure modes and regime transitions
- Report with full derivations and experiments

---

## Author

Théo Basséras