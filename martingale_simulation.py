import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.animation import FuncAnimation


# Probability of a single chance (e.g. red or black) in European roulette
ROULETTE_WIN_PROB = 18 / 37

class Martingale:
    """Simulates the Martingale betting strategy with configuration parameters."""

    def __init__(self, initial_balance, initial_bet, win_prob, table_limit):

        """
        Initializes the Martingale simulation
        
        Parameters:
        initial_balance (float)
        initial_bet (float)
        win_prob (float)
        table_limit (float)
        max_rounds (int)
        """

        self.initial_balance = initial_balance
        self.initial_bet = initial_bet
        self.win_prob = win_prob
        self.table_limit = table_limit
        

        self.reset()

        

    def reset(self):
        """Resets the simulation to the initial state"""
        self.balance = self.initial_balance
        self.current_bet = self.initial_bet
        self.balance_history = [self.initial_balance]
        self.rounds_played = 0

        

    def simulate(self):


        while (self.balance >= self.current_bet and self.table_limit >= self.current_bet):

            self.balance -= self.current_bet          # Set current bet

            if random.random() <= self.win_prob:
                self.balance += 2 * self.current_bet  # Collect profit
                self.current_bet = self.initial_bet   # Reset to initial bet
            else: 
                self.current_bet *= 2


            self.balance_history.append(self.balance)
            self.rounds_played += 1

        
        return self
    





    

    
def validate_input(prompt, min_val = 0.01, input_type = float):
    while True:
        try:
            value = input_type(input(prompt))
            if value < min_val:
                print("The value must be >= {min_val}!")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")





def run_simulations(initial_balance, initial_bet, win_prob, table_limit, sim_count):
    """Create multiple simulations"""
    
    return [Martingale(initial_balance, 
                             initial_bet, 
                             win_prob,              
                             table_limit
                             ).simulate()
                             for _ in range(sim_count)
                             ] 





def animate_simulations(simulators, initial_balance, initial_bet, table_limit, filename="animation.gif"):
    """Visualize multiple Martingale simulations as an animated chart"""
    
    balance_histories = [sim.balance_history 
                         for sim in simulators]

    
    max_rounds = max([sim.rounds_played  for sim in simulators])

    max_balance = max([max(hist) for hist in  balance_histories])
    min_balance = min([min(hist) for hist in  balance_histories])
    x = [i for i in range(0, max_rounds + 1)]  

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.set_xlim([0,  max_rounds + 20])
    ax.set_ylim([min_balance - initial_balance, max_balance + initial_balance])

    plt.axhline(initial_balance, 
                color='red',
                linewidth = 3, 
                linestyle='--', 
                label='Initial balance')

    lines = []
    texts = []
    colors = plt.cm.viridis(np.linspace(0, 1, len(simulators)))  # Color from Colormap


    for i in range(len(simulators)):
        line, = ax.plot([], [], lw=1.5, color=colors[i], label=f'Game process {i+1}')
        text = ax.text(0, 0, '', color= 'white', fontweight='bold',
                      bbox=dict(facecolor= colors[i], alpha=0.7, edgecolor='none', pad=3))
        lines.append(line)
        texts.append(text)
        
        
        def init():
            for line in lines:
                line.set_data([], [])
                text.set_alpha(0)
            return lines + texts
        
        def update(frame):
            for i, (line, text) in enumerate(zip(lines, texts)):
            # Current data up to the frame (limited to the length of the respective history)
                max_frame_data = min(frame + 1, len(balance_histories[i]))
                current_x = list(range(max_frame_data))  # Dynamic x value per graph
                current_y = balance_histories[i][:max_frame_data]
                line.set_data(current_x, current_y) 

                if frame > 0:
                    text.set_position((current_x[-1] + 1.5, current_y[-1]))
                    text.set_text(f'{current_y[-1]:.2f} €')
                    text.set_alpha(1)

            return lines + texts
    
    animation = FuncAnimation(fig, 
                              func = update, 
                              frames=len(x), 
                              init_func=init, 
                              interval = 80, 
                              repeat = False)
    
    # Modify layout
    ax.set_xlabel('Rounds')
    ax.set_ylabel('Balance in €')
    ax.set_title('Martingale system simulations')


    # Create legends
    ax.legend(loc = 'upper left')
    
    custom_legend = [
    Patch(color = 'none', label='Initial balance: ' + str(initial_balance) + ' €' ),
    Patch(color = 'none', label='Initial bet: ' + str(initial_bet) + ' €' ),
    Patch(color = 'none', label='Table limit: ' + str(table_limit) + ' €' ),
]
    plt.gca().add_artist(ax.legend(loc='upper left'))
    plt.legend(handles=custom_legend, loc='lower right')
    



    plt.grid(True)


    # Save and display animation
    
    animation.save(filename, writer='imagemagick', fps=60)
    plt.show()









def main():

    """Main function for running the simulation."""

    initial_balance = validate_input("Initial balance: ")
    initial_bet = validate_input("Initial bet: ")
    table_limit = validate_input("Table limit ", min_val=1, input_type=int)
    sim_count = validate_input("Number of simulations: ", min_val=1, input_type=int)

    simulators = run_simulations(initial_balance, initial_bet, ROULETTE_WIN_PROB, table_limit, sim_count)
    animate_simulations(simulators, initial_balance, initial_bet, table_limit, filename="animation1.gif")

    



            
        


if __name__ == "__main__":
    main()

    