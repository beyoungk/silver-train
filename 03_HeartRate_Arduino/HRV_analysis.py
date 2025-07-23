import pandas as pd
import numpy as np

def load_heartbeat_data(file_path):
    df = pd.read_csv(file_path)
    beat_times = df[df["Signal"] == 1.0]["Time (s)"].values
    return beat_times

def calculate_rr_intervals(beat_times):
    rr_intervals = np.diff(beat_times) # time between each beat
    return rr_intervals

def calculate_sdnn(rr_intervals):
    return np.std(rr_intervals) * 1000 # convert to ms

def calculate_rmssd(rr_intervals):
    successive_diffs = np.diff(rr_intervals)
    return np.sqrt(np.mean(successive_diffs**2)) * 1000 # convert to ms

def main():
    print("Analyzing HRV from simulated heartbeat signal...")
    beat_times = load_heartbeat_data("simulated_heart_signal.csv")

    if len(beat_times) < 2:
        print("Not enough beats to calculate HRV.")
        return
    
    rr_intervals = calculate_rr_intervals(beat_times)
    sdnn = calculate_sdnn(rr_intervals)
    rmssd = calculate_rmssd(rr_intervals)

    print(f"Beats Detected: {len(beat_times)}")
    print(f"RR Intervals (sec): {np.round(rr_intervals, 3)}")
    print(f"SDNN: {sdnn:.2f} ms")
    print(f"RMSSD: {rmssd:.2f} ms")

if __name__ == "__main__":
    main()