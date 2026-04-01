# Fast and Scalable Local Kernel Machines (FaLK-SVM)

## Overview
This repository contains a professional implementation and reproduction of the **FaLK-SVM** algorithm, a scalable solution to the computational limitations of classical Support Vector Machines (SVMs). The project explores the core architecture, mathematical assumptions, ablation studies, and edge-case failure modes of local kernel machines.

### Key Highlights
- **Core Architecture & Computational Analysis:** Structured step-by-step breakdown of the FaLK-SVM pipeline with explicit time/space complexity analysis mapping to paper equations, highlighting $\\mathcal{O}(N \\log N)$ inference.
- **Dynamic Geometric Subdivisions (Set Cover):** Implements the fundamental $k'$-neighborhood cover-set algorithm bounding uniformly and mitigating the curse of dimensionality locally.
- **Ablation Studies:** Evaluates native FaLK-SVM vs. Random Centres and pure Direct Nearest Centre mapping (FaLK-SVMc) across 5 random seeded validations to prove robust spatial boundary delineation.
- **Failure Mode Degradation Curve:** Extensively stress-tests global versus local kernel machine topology under extreme $\\mathcal{O}(3,000)$ dimensional feature limits, proving breakdown points of spatial heuristics vs. dense linear parameters.

## Repository Structure

- `notebooks/` - Core implementation and analysis
  - `01_Method_Architecture.ipynb` - Pipeline theory and complexity breakdown
  - `02_Key_Assumptions.ipynb` - Core statistical requirements and violation scenarios
  - `03_Baseline_Comparison.ipynb` - Benchmarking FaLK-SVM vs. Global Linear SVMs
  - `04_Data_Generation.ipynb` - Synthetic balanced toy dataset creation
  - `05_FaLKSVM_Implementation.ipynb` - Custom Set-Cover and local SVM fit logic
  - `06_Results_and_Validation.ipynb` - Empirical multi-seed cross-validation reporting
  - `07_Ablation_Studies.ipynb` - Critical component removal validation 
  - `08_Failure_Modes.ipynb` - Dimensional degradation and high-sparse data boundary tests
- `data/` - Cached synthetic spatial distributions
- `results/` - Model performance comparison plots
  - `raw_spiral_dataset.png` - 2-Spiral dataset topology
  - `falksvm_decision_boundary.png` - FaLK-SVM eager manifold boundary
  - `ablation_performance_analysis.png` - Comparative study vs. Random/Centred models
  - `dimensionality_failure_mode.png` - Analysis of performance decay in high dimensions
- `requirements.txt` - Python environment dependencies

## Getting Started

1. Set up your Python environment:
   ```bash
   pip install -r requirements.txt
   ```
2. Reproduce the pipeline sequentially starting from the `notebooks/` directory. Each notebook is numbered sequentially demonstrating the flow from theory -> math -> code -> validation -> profiling.

## Conclusions

FaLK-SVM dramatically accelerates large-scale non-linear optimizations. However, as proven in the ablation and failure mode experiments:
- Bypassing smart geometric centroid tracking severely destabilizes performance.
- Moving past $\\mathcal{O}(50-3,000)$ features rapidly degrades the relative effectiveness of local models, yielding lower accuracy profiles versus globally mapped linear equivalents. Integrating PCA dimensionality reduction is advised for extreme manifolds.
