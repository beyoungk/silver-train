import numpy as np
import matplotlib.pyplot as plt

# Constants
ATP_PER_CYCLE = 30 # ATP molecules per mitochondrion per second under ideal conditions

def calculate_atp(glucose, oxygen, mitochondria, time_seconds):
    """
    Simulates ATP production based on glucose, oxygen, and mitochondria count.
    Returns a list of ATP values over time.
    """

    # Convert availability to efficiency multiplier
    glucose_factor = {'low': 0.3, 'medium': 0.6, 'high': 1.0}
    oxygen_factor = {'low': 0.5, 'normal': 1.0}

    if glucose not in glucose_factor or oxygen not in oxygen_factor:
        raise ValueError("Invalid input for glucose or oxygen levels.")
    
    g_factor = glucose_factor[glucose]
    o_factor = oxygen_factor[oxygen]

    atp_output = []
    for t in range(time_seconds):
        # Simulate biological variability using Gaussian noise (mean=1.0, std=0.1)
        # Adds a natural fluctuation to ATP output per second
        noise = np.random.normal(loc=1.0, scale=0.1)
        atp_this_second = mitochondria * ATP_PER_CYCLE * g_factor * o_factor * noise
        atp_output.append(atp_this_second)
    
    return atp_output

def plot_atp(atp_output):
    time = np.arange(len(atp_output))
    plt.figure(figsize=(10, 5))
    plt.plot(time, atp_output, marker='o', color='green', linewidth=2)
    plt.title("ATP Production Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("ATP Molecules Produced")
    plt.grid(True)
    plt.savefig("atp_output_plot.png")
    plt.show()

def main():
    print("Welcome to MitoPower: ATP Simulator")
    glucose = input("Enter glucose level (low / medium / high): ").lower()
    oxygen = input("Enter oxygen level (low / normal): ").lower()
    
    try:
        mitochondria = int(input("Enter number of mitochondria (e.g., 500): "))
        time_seconds = int(input("Enter simulation time in seconds (e.g., 10): "))
    except ValueError:
        print("Please enter valid numbers for mitochondria and time.")
        return
    
    try:
        atp_output = calculate_atp(glucose, oxygen, mitochondria, time_seconds)
        total_atp = sum(atp_output)
        print(f"\n Totaal ATP Produced: {int(total_atp)} molecules")
        plot_atp(atp_output)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
