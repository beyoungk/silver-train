# CRISPR Design Explainer Notebook

This project explains how CRISPR-Cas9 uses guide RNAs (gRNAs) to locate specific DNA sequences. It simulates gRNA binding and PAM recognition in a simplified DNA sequence using Python. The notebook is designed to be part tutorial, part interactive biology demo.

> **Note:** This project is fully simulated.  No lab data or wet-lab results are used. The focus is on learning and demonstrating biological logic through code.

## What it Does

- Explains the biology behind CRISPR-Cas9 gene editing
- Lets users input a DNA sequence and a guide RNA
- Simulates target recognition and PAM site detection
- Visualizes matching target sites in the DNA

## Why it Matters

CRISPR is one of the most important breakthroughs in modern biology. This project demonstrates:
- Core concepts of gRNA targeting
- How PAM sequences guide Cas9 cutting
- The balance between biological accuracy and computational modeling

## Tools Used

- Python
- Matplotlib
- Jupyter Notebook

## Files

- `crispr_explainer.ipynb` — main notebook (text + code)
- `guide_match_plot.png` — separte plot image showing match locations
- `README.md` — this file

## How to Run

1. Make sure you have Python installed.
2. Install required packages:
    pip install matplotlib

3. Run the Jupyter notebook:
    jupyter notebook crispr_explainer.ipynb

4. Edit the DNA and gRNA values and re-run the notebook to test new matches.

## Results

- Accuracy: ~97–99% (may vary per run)
- Confusion matrix saved as `model_accuracy.png`

## Biological Note

- Cas9 binds where the gRNA perfectly complements the DNA target and is followed by a valid PAM (usually NGG).
- This simulation checks only for perfect matches with adjacent PAM motifs.
- Real-world tools consider mismatches, bulges, and genome-wide screening for off-target effects.