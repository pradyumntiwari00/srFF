import time
import matplotlib.pyplot as plt
class SRFlipFlop:
    def __init__(self):
        self.Q = 0  
        self.Q_not = 1  
    def update(self, S, R):
        if S == 1 and R == 0:
            self.Q = 1
            self.Q_not = 0
        elif S == 0 and R == 1:
            self.Q = 0
            self.Q_not = 1
        elif S == 0 and R == 0:
            pass
        else:
            print("Invalid state (S=1, R=1) - Undefined behavior")
    def output(self):
        return self.Q, self.Q_not
def clock_signal(frequency=1):
    while True:
        yield 1  
        time.sleep(1 / (2 * frequency))  
        yield 0  
        time.sleep(1 / (2 * frequency)) 
def plot_timing_diagram(clock_values, s_values, r_values, q_values, q_not_values):
    time_steps = range(len(clock_values))

    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)  
    plt.step(time_steps, clock_values, label='Clock', where='mid')
    plt.title('Clock Signal')
    plt.ylabel('Clock')
    plt.grid(True)
    plt.subplot(3, 1, 2)  # Second plot
    plt.step(time_steps, s_values, label='S Input', where='mid')
    plt.step(time_steps, r_values, label='R Input', where='mid')
    plt.title('Inputs (S and R)')
    plt.ylabel('Input Values')
    plt.legend()
    plt.grid(True)
    plt.subplot(3, 1, 3)  
    plt.step(time_steps, q_values, label='Q Output', where='mid')
    plt.step(time_steps, q_not_values, label='Q_not Output', where='mid')
    plt.title('Outputs (Q and Q_not)')
    plt.ylabel('Output Values')
    plt.legend()
    plt.grid(True)

    plt.xlabel('Time (Clock Cycles)')
    plt.tight_layout()
    plt.show()
def simulate_sr_flipflop():
    sr_flipflop = SRFlipFlop()  
    clock = clock_signal(frequency=1)  
    

    clock_values = []
    s_values = []
    r_values = []
    q_values = []
    q_not_values = []
    
    num_cycles = 10
    
    for _ in range(num_cycles):  
        clk = next(clock)  
        if clk == 1:
            # Ask user for inputs S and R
            S = int(input("Enter S (0 or 1): "))
            R = int(input("Enter R (0 or 1): "))
            sr_flipflop.update(S, R)  # Update the flip-flop based on the inputs only when clock is high
        else:
            # If clock is low, no changes to S and R inputs
            S = s_values[-1] if s_values else 0
            R = r_values[-1] if r_values else 0
        
        q, q_not = sr_flipflop.output()
        print(f"Clock: {clk}, S: {S}, R: {R}, Q: {q}, Q_not: {q_not}")
        
        
        clock_values.append(clk)
        s_values.append(S)
        r_values.append(R)
        q_values.append(q)
        q_not_values.append(q_not)
        
        
        time.sleep(1)

    plot_timing_diagram(clock_values, s_values, r_values, q_values, q_not_values)


# Main Execution
if __name__ == "__main__":
    simulate_sr_flipflop()
