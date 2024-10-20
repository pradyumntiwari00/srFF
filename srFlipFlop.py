import time
import matplotlib.pyplot as plt

# SR Flip-Flop Class Definition
class SRFlipFlop:
    def __init__(self):
        self.Q = 0  # Initial output state
        self.Q_not = 1  # Complement of Q
    
    # Method to update the state of the flip-flop based on inputs S and R
    def update(self, S, R):
        if S == 1 and R == 0:
            self.Q = 1
            self.Q_not = 0
        elif S == 0 and R == 1:
            self.Q = 0
            self.Q_not = 1
        elif S == 0 and R == 0:
            # Retain the current state
            pass
        else:
            print("Invalid state (S=1, R=1) - Undefined behavior")
    
    # Method to return the current output state (Q and Q_not)
    def output(self):
        return self.Q, self.Q_not


# Clock Signal Generator
def clock_signal(frequency=1):
    """
    Generator that alternates between 1 (HIGH) and 0 (LOW) to simulate a clock signal.
    frequency: The number of cycles per second (Hertz).
    """
    while True:
        yield 1  # HIGH state (clock rising edge)
        time.sleep(1 / (2 * frequency))  # Pause for half the clock period
        yield 0  # LOW state (clock falling edge)
        time.sleep(1 / (2 * frequency))  # Pause for half the clock period


# Plotting function with 3 separate graphs
def plot_timing_diagram(clock_values, s_values, r_values, q_values, q_not_values):
    time_steps = range(len(clock_values))

    plt.figure(figsize=(10, 10))

    # Plot Clock signal
    plt.subplot(3, 1, 1)  # First plot
    plt.step(time_steps, clock_values, label='Clock', where='mid')
    plt.title('Clock Signal')
    plt.ylabel('Clock')
    plt.grid(True)

    # Plot Input S and R values
    plt.subplot(3, 1, 2)  # Second plot
    plt.step(time_steps, s_values, label='S Input', where='mid')
    plt.step(time_steps, r_values, label='R Input', where='mid')
    plt.title('Inputs (S and R)')
    plt.ylabel('Input Values')
    plt.legend()
    plt.grid(True)

    # Plot Q and Q_not outputs
    plt.subplot(3, 1, 3)  # Third plot
    plt.step(time_steps, q_values, label='Q Output', where='mid')
    plt.step(time_steps, q_not_values, label='Q_not Output', where='mid')
    plt.title('Outputs (Q and Q_not)')
    plt.ylabel('Output Values')
    plt.legend()
    plt.grid(True)

    plt.xlabel('Time (Clock Cycles)')
    plt.tight_layout()
    plt.show()


# Simulation of SR Flip-Flop with Clock and Graphs
def simulate_sr_flipflop():
    sr_flipflop = SRFlipFlop()  # Initialize the SR flip-flop
    clock = clock_signal(frequency=1)  # Create a 1 Hz clock generator
    
    # Lists to store values for plotting
    clock_values = []
    s_values = []
    r_values = []
    q_values = []
    q_not_values = []
    
    # Number of clock cycles for the simulation
    num_cycles = 10
    
    for _ in range(num_cycles):  # Simulate 10 clock cycles
        clk = next(clock)  # Get the current clock value (1 or 0)
        
        # Check if the clock is HIGH (1), to simulate rising edge
        if clk == 1:
            # Ask user for inputs S and R
            S = int(input("Enter S (0 or 1): "))
            R = int(input("Enter R (0 or 1): "))
            sr_flipflop.update(S, R)  # Update the flip-flop based on the inputs only when clock is high
        else:
            # If clock is low, no changes to S and R inputs
            S = s_values[-1] if s_values else 0
            R = r_values[-1] if r_values else 0
        
        # Get the current outputs
        q, q_not = sr_flipflop.output()
        print(f"Clock: {clk}, S: {S}, R: {R}, Q: {q}, Q_not: {q_not}")
        
        # Append values to the lists for plotting
        clock_values.append(clk)
        s_values.append(S)
        r_values.append(R)
        q_values.append(q)
        q_not_values.append(q_not)
        
        # Sleep to simulate real-time clock cycles
        time.sleep(1)

    # Plot the timing diagram
    plot_timing_diagram(clock_values, s_values, r_values, q_values, q_not_values)


# Main Execution
if __name__ == "__main__":
    simulate_sr_flipflop()
