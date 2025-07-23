# PCR Simulator

This project simulates ATP production in mitochondria over time based on the given glucose and oxygen levels.

## What it Does

- Takes user input for glucose, oxygen, number of mitochondria, and time
- Calculates ATP output using simple simulation logic
- Adds natural-looking fluctuations to mimic biological variability
- Generates a plot based on the ATP produced over time

## Why it Matters

Mitochondria are essential for cellular energy production, and this project shows:
- How user inputs can drive biological simulations
- Use of random variability to mimic real biological systems
- Data visualization with `matplotlib`
- Beginner-friendly simulation of metabolic activity

## Tools Used

- Python
- NumPy 
- Matplotlib
- Simulation logic

## Files

- `mito_power.py` - main script
- `atp_output_plot.png` - plot of ATP output over time (generated at runtime)
- `README.md` - this file

## How to Run

1. Make sure you have Python installed.
2. Download or close this repository.
3. Navigate to the folder:
    cd projects/02_MitoPower_ATP_Tracker
4. Run the script: 
    python mito_power.py
5. Follow the on-screen prompts to enter input values. The total ATP produced will be printed, and a line plot will be displayed and saved in the folder.

## Biological Note

This simulation includes random fluctuation using Gaussian noise to imitate natural variability in ATP output. While not a mechanistic model, it introduces basic ideas of energy fluctuation in a cell. For research-level accuracy, further biochemical modeling would be required.