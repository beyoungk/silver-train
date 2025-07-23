# Cancer Classifier (Real-World ML Project)

This project builds a machine learning classifier to distinguish between malignant and benign tumors using a real-world breast cancer dataset from the UCI Machine Learning Repository.

> **Note:** This project uses a real dataset (`data.csv`), sourced from the Breast Cancer Wisconsin (Diagnostic) Data Set from the UCI Machine Learning Repository, not a built-in library. All data preprocessing, normalization, and model training are done from scratch.

## What it Does

- Loads and processes a real cancer dataset
- Encodes the diagnosis labels (M = 1, B = 0)
- Normalizes all features using `StandardScaler`
- Trains a Logistic Regression classifier
- Evaluates performance using accuracy and a confusion matrix
- Saves a visualization of the confusion matrix

## Why it Matters

Breast cancer diagnosis can be supported by predictive models that help identify patterns in tumor features. This project demonstrates:
- End-to-end data handling and modeling
- Real-world machine learning practices (cleaning, scaling, splitting)
- Core evaluation metrics used in medical informatics

## Tools Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib & Seaborn
- Jupyter Notebook

## Files

- `data.csv` — raw data file from UCI (569 samples, 30 features)
- `cancer_classifier.ipynb` — full Jupyter Notebook ML pipeline
- `model_accuracy.png` — confusion matrix visualization
- `README.md` — this file

## How to Run

1. Make sure you have Python installed.
2. Install required packages:
    pip install pandas numpy matplotlib seaborn scikit-learn

3. Run the Jupyter notebook:
    jupyter notebook cancer_classifier.ipynb

4.  Run all cells to load the data, train the model, and visualize results.

## Results

- Accuracy: ~97–99% (may vary per run)
- Confusion matrix saved as `model_accuracy.png`

## Biological Note

This simulation adds realistic biological noise to model naturally occurring HRV. While the logistics of this model is simplified, the model demonstrates the foundational techniques used in real biosignal monitoring systems for wearable devices, clinical assessments, and research.