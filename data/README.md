# Toy Dataset Description

This dataset is synthetically generated inside `partB/task_2_1.ipynb` using `numpy`. It creates a binary classification scenario following two continuous intertwined spirals that add nonlinear complexities.

- **How it is obtained**: Programmatically generated using polar equations adding random standard deviations (`numpy.random.randn`) mirroring real-world distributions.
- **How it is used**: Saved here uniquely as `toy_dataset.csv` exclusively. Subsequent notebooks (`task_2_2` and `task_2_3`) load this dataset dynamically iteratively to benchmark FaLK-SVM bounds.

Features are scaled continuously uniformly within the spatial metric array strictly restricted to boundary domains $[0,1]$ conforming entirely to the base FaLK-SVM paper settings for spatial continuity evaluation globally.
