# Adaptive Representation Learning for Sparse Signal Classification under Distribution Shifts

## Overview

This project investigates how to design robust classification systems when **new classes appear with extremely limited data** and **data distributions evolve over time**.

The core challenge is to build models that:

* generalize beyond their training distribution,
* adapt rapidly to unseen classes,
* remain stable under low-sample regimes.

We explore this through a **few-shot learning framework applied to raw time-series signals**.

---

## Problem Setting

A model is first trained on a set of base classes with abundant data.
At inference time, **previously unseen classes appear**, with only a handful of labeled examples available.

This creates three major challenges:

* **Distribution shifts**: new classes follow different statistical patterns
* **Sparse supervision**: only 1–10 samples per new class
* **Representation mismatch**: standard classifiers fail due to overfitting

---

## Approaches

### 1. Supervised Baseline + Prototype Inference

* CNN encoder trained on base classes
* Embedding space reused for unseen classes
* Classification via **nearest prototype (Euclidean distance)**

→ Highlights limitations of standard supervised pipelines under shift

---

### 2. Prototypical Networks (Episodic Training)

* Training mimics inference conditions via episodes
* Each episode:

  * samples classes
  * builds support/query sets
* Learns a **metric space where class means are optimal decision boundaries**

→ Enables rapid adaptation with minimal data

---

### 3. Segment-based Residual Architecture

* Signal divided into temporal segments
* Each segment encoded independently
* Aggregated representation improves robustness to:

  * local noise
  * temporal misalignment

---

## Key Results

* Performance improves significantly with **metric-based learning vs standard classification**
* Accuracy scales smoothly with number of shots (1 → 10)
* Embedding visualizations show:

  * clear clustering of unseen classes
  * meaningful geometric structure

---

## Interpretation & Insights

This project highlights several fundamental phenomena:

### Distribution Shifts

Models trained on a fixed distribution struggle when new classes exhibit different signal characteristics.

### Rapid Regime Transitions

Few-shot settings simulate abrupt changes where the model must adapt instantly with minimal data.

### Multi-source Interference

Signals from different classes may overlap in feature space, making separation non-trivial without learned representations.

### Representation Learning as the Bottleneck

The quality of the embedding space—not the classifier—is the key driver of performance.

---

## Tech Stack

* PyTorch
* NumPy / SciPy
* h5py
* scikit-learn
* Matplotlib / Seaborn

---

## Structure

* `baseline/` → supervised encoder + prototype inference
* `prototypical/` → episodic training pipeline
* `resnet_segment/` → segment-based architecture
* `utils/` → data loading, visualization, benchmarking

---

## Takeaway

Rather than optimizing for accuracy on a fixed dataset, this project focuses on:

> **building systems that remain reliable when the world changes and data is scarce.**

This shift in perspective is critical for real-world machine learning systems.
