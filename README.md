# EUPG: Efficient Unlearning with Privacy Guarantees

This is the official repository containing the code needed to replicate the results from "EUPG: Efficient Unlearning with Privacy Guarantees."

## Paper

[EUPG: Efficient Unlearning with Privacy Guarantees]()

## Usage

The repository includes a Jupyter notebook for each benchmark. These notebooks can be used to reproduce the experiments reported in the paper for their respective benchmarks.

## Datasets

The three datasets used are publicly available and located in the data folder:
- [Adult Income](https://archive.ics.uci.edu/ml/datasets/Adult)
- [Heart Disease](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)
- [Credit Information](https://www.kaggle.com/c/GiveMeSomeCredit)

## Dependencies

- **Python**: 3.8.16
- **TensorFlow**: 2.13.0
- **Torch**: 1.12.0
- **Torchvision**: 0.13.0
- **NumPy**: 1.24.3
- **Pandas**: 1.5.3
- **SciPy**: 1.10.1
- **Scikit-learn**: 1.3.0
- **XGBoost**: 2.0.2

The required Anaconda environment can be installed using the `environment.yml` file.

## Main Results

### Before Unlearning

*The table below shows the performance of EUPG before forgetting.*  
![EUPG performance before unlearning](figures/before_ul.png)

### After Unlearning

*The table below shows the post-unlearning performance of EUPG after forgetting 5% of the training data.*  
![EUPG performance after unlearning](figures/after_ul.png)

## Citation

*Information to be added*

## Funding

Partial support received from the European Commission (projects H2020-871042 "SoBigData++" and H2020-101006879 "MobiDataLab"), the Spanish Government (project PID2021-123637NB-I00, "CURLING"), and the Government of Catalonia (ICREA Acadèmia Prize and grant 2021 SGR 00115).
