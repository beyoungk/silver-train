# Heart Rate Monitoring and HRV Analysis Report

## Project Overview

This project simulates a heart rate monitoring system without hardware, using Python to generate synthetic heartbeat signals. The signal is then analyzed to extract heart rate variability (HRV) metrics such as SDNN and RMSSD, the indicators of autonomic nervous system activity and overall cardiovascular health.

This project includes:
- A simulated heart signal (`signal_plot.ipynb`)
- An HRV analysis script (`HRV_analysis.py`)
- A CSV file containing synthetic beat timing

## Simulated Signal Summary

- **Duration:** 10 seconds
- **Sampling rate:** 100 Hz
- **Target heart rate:** 72 BPM (approx. 0.83 seconds between beats)
- **Biological noise:** Gaussian jitter added to RR intervals (± 50 ms)
- **Output file:** `output.png`

## HRV Analysis Results

From the simulated data, the following HRV metrics were computed:

- **Beats detected:** 11
- *RR Intervals:** [0.821 0.811 0.821 0.801 0.801 0.921 0.861 0.831 0.931 0.771] seconds
- **SDNN:** 49.69 ms
- **RMSSD:** 78.32 ms

These values are within a healthy range for a resting state and demonstrate how minor variations in heartbeat timing reflect heart rate variability.

## Key Terms

- **RR Interval:** The time between consecutive heartbeats.
- **SDNN:** Standard deviation of NN (normal-to-normal) intervals. Reflects overall HRV.
- **RMSSD:** Root mean square of successive RR differences. Reflects short-term parasympathetic activity.

## Why This Matters

Heart Rate Variability (HRV) is used in:
- Fitness and recovery tracking
- Stress monitoring
- Early detection of cardiac abnormalities

By simulating, visualizing, and analyzing HRV without physical sensors, this project demonstrates key skills in:
- Data simulation
- Biosignal analysis
- Python coding
- Scientific communication

## Next Steps

- Incorporate real sensor input using an Arduino and pulse sensor
- Add HR zones (e.g., resting, moderate, intense)
- Visualize HRV over time with rolling windows

## Files used

- `signal_plot.ipynb` / Generates and visualizes heartbeat data
- `simulated_heart_signal.csv` / Data file used for analysis
- `HRV_analysis.py` / Computes RR intervals, SDNN, RMSSD
- `report.md` / This report
