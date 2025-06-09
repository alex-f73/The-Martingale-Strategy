# The Martingale Strategy 🎰

Doubling your bet when you lose.

<video controls src="martingale_simulation.MP4" title="Simulation"></video>

## How the Martingale System Works 📘

This simulation models the Martingale betting strategy using European roulette as the game.

The classic Martingale ("doubling") system works as follows:
1. The player starts by betting one unit on a simple chance (e.g., Red/Black, Even/Odd, or 1–18).
2. If the player **loses**, they double the previous bet.
3. If the player **wins**, they get back all previous losses and earn a net profit of one unit.
4. After a win, the process resets to a one-unit bet.

## Install Dependencies :gear:
Install important packages for scientific work (`scipy`, `numpy`, `matplotlib`, `pandas`) using:

```bash
conda install -c conda-forge scipy numpy matplotlib pandas
```  
Alternativively, using pip:
```bash
pip install scipy numpy matplotlib pandas
```  

## Usage :rocket:

 To start the program, run:
 ```bash
python martingale_simulation.py
```  

You’ll be prompted to enter the following parameters in the terminal:

 1. Initial balance (float)
 2. Initial bet (float)
 3. Table limit (float)
 4. Number of simulations: (int)










