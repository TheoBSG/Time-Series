# Scalable Shape Discovery in Time Series  
## Interpretable Pattern Extraction vs Deep Learning at Scale

---

## Overview

This project investigates a fundamental problem in high-dimensional sequential data:

> How can we extract **interpretable, discriminative patterns** from time series while remaining computationally scalable?

We focus on **shapelet-based modeling**, a framework where classification is driven by the presence of **localized patterns** rather than global similarity.

The work combines:

- **algorithmic efficiency** (FastShapelet)
- **statistical learning** (information gain optimization)
- **representation learning** (pattern-based embeddings)
- **comparative modeling** (against deep learning approaches)

---

## Why This Matters

Most modern pipelines treat time series as raw vectors or rely on deep architectures that:

- require large amounts of data
- lack interpretability
- are expensive to train and deploy

This project explores an alternative:

> Represent time series using a **small set of highly informative patterns**.

This leads to:

- faster inference  
- compact representations  
- interpretable decision rules  
- strong performance in low-data regimes  

---

## Project Structure

- `fast-shapelet-main/starlight_exp.ipynb`  
  → Implementation and experiments for **FastShapelet-based pattern extraction** on real-world time series

- `Deep_Learning.ipynb`  
  → Custom deep learning baseline for comparison (pattern-based architecture)

- `Report.pdf`  
  → Full theoretical derivation, algorithmic details, and experimental analysis

---

## Core Concepts

### Shapelets

A **shapelet** is a short subsequence that is maximally discriminative for classification.

Instead of comparing full signals, we evaluate:

> distance to a small set of key patterns

This transforms time series into a **feature space of distances to shapelets**.

---

### Objective Function

The quality of a pattern is measured via **Information Gain**:

:contentReference[oaicite:0]{index=0}

A good shapelet produces:

- low entropy subsets  
- clear class separation  
- strong decision boundaries  

---

## Algorithmic Contribution: FastShapelet

Brute-force search is intractable:

- Complexity: **O(n² m⁴)**

FastShapelet introduces a scalable alternative:

### Phase 1 — Candidate Filtering
- SAX (Symbolic Aggregate Approximation)
- Random projections
- Hash-based collision counting
- Ranking via **distinguishing power**

### Phase 2 — Exact Evaluation
- Recover real subsequences
- Compute exact distances
- Select optimal shapelet via information gain

---

## Key Insight

> Approximation is used only to **reduce the search space**,  
> while final selection remains **exact and statistically grounded**.

This hybrid design is critical for:

- scalability  
- robustness  
- reproducibility  

---

## Dataset: Starlight Curves

- ~9,000 time series  
- length: 1024  
- 3 classes of periodic behaviors  

Challenges:

- high dimensionality  
- noise  
- class imbalance  
- pattern ambiguity  

---

## Results

### Small-scale setting

| Method        | Time        | Accuracy |
|---------------|------------|----------|
| Barycenter    | 120 min     | 0.97     |
| Deep Learning | 5 s         | 0.78     |
| Shapelets     | 40 s        | 0.97     |

---

### Large-scale setting

| Method        | Time        | Accuracy |
|---------------|------------|----------|
| Deep Learning | 1m30        | 0.84     |
| Shapelets     | 20 min      | **0.91** |

---

## Interpretation

### 1. Pattern-based models compete with deep learning

- Comparable or better accuracy
- No need for large-scale training
- More stable in noisy environments

---

### 2. Interpretability is a structural advantage

Each decision can be traced to:

- a specific subsequence  
- a distance threshold  

This enables:

- debugging  
- model understanding  
- feature-level reasoning  

---

### 3. Efficiency through structure

The key bottleneck is not learning—but **search**.

FastShapelet shows that:

> careful algorithm design can outperform brute-force and heavy models

---

## Representation Perspective

This project suggests a broader idea:

> Time series can be represented by a **small set of patterns + distances**

This creates a **compressed representation space**:

- dimension ≪ raw signal
- preserves discriminative information
- removes redundancy

---

## Extensions & Insights

### Compression via Patterns

Instead of storing full time series:

- store shapelets + distances
- reconstruct approximate signals
- drastically reduce memory footprint

---

### Toward Event-Based Modeling

The shapelet framework connects naturally with:

- rare pattern detection  
- anomaly detection  
- regime identification  

---

### Link to Structured Modeling

This approach aligns with a deeper principle:

> Complex signals are governed by **reusable local structures**

---

## Skills Demonstrated

- algorithm design under complexity constraints  
- probabilistic modeling and entropy-based criteria  
- time series analysis and pattern discovery  
- scalable approximation techniques  
- deep learning benchmarking  
- high-dimensional data representation  

---

## Author

**Yani HAMMACHE**

**Théo BASSERAS**

Mathematics, machine learning, and structured data modeling.

---

## Key Takeaway

> High-dimensional time series do not need to be modeled globally.

They can be understood through:

**a small number of well-chosen local patterns**

which leads to:

- efficient computation  
- interpretable models  
- strong generalization  

---