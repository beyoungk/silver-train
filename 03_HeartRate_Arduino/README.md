# Heart Rate Monitor & HRV Analysis

This project simulates signal and analyzes heart rate variability (HRV) metrics such as SDNN and RMSSD using Python.

**Note:** This project does **not use Arduino or any physical hardware**. The heartbeat signal is fully simulated in Python to mimic the type of data typically captured from a pulse sensor connected to an Arduino.

## What it Does

- Generates a simulated heartbeat signal with realistic variability.
- Plots and exports the heartbeat signal to a `.png` file
- Analyzes RR intervals to calculate HRV metrics
- Outputs results in the terminal (Summary report is written based on the results)

## Why it Matters

Heart Rate Variability (HRV) is used in health, wellness, and sports science to assess cardiovascular stress and autonomic nervous system activity. This project shows:
- How biosignals can be simulated, stored, and visualized
- Extraction of biologically relevant metrics using Python
- Foundational signal processing techniques

## Tools Used

- Python
- NumPy 
- Pandas
- Matplo
- Jupyter Notebook

## Files

- `signal_plot.ipynb` - main script
- `simulated_heart_signal.csv` - output CSV with time-series heart signal
- `HRV_analysis.py` - script to analyze HRV metrics from the CSV
- `output.png` - image of the simulated heartbeat
- `report.md` - project summary and results
- `README.md` - this file

## How to Run

1. Make sure you have Python installed.
2. Install required packages:
    pip install numpy pandas matplotlib

3. Run the Jupyter notebook:
    jupyter notebook signal_plot.ipynb

4. After the CSV file is generated, run the analysis script:
    python HRV_analysis.py

5. View results in the terminal.

## Biological Note

This simulation adds realistic biological noise to model naturally occurring HRV. While the logistics of this model is simplified, the model demonstrates the foundational techniques used in real biosignal monitoring systems for wearable devices, clinical assessments, and research.