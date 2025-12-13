
# Wandering in the Woods

Wandering in the Woods is an educational computer simulation built using Python and Pygame.  
The simulation allows users to configure a grid-based environment, place multiple players, and observe how random movement eventually leads players to meet.

The project is designed to demonstrate core ideas in computation, randomness, and data collection through an interactive, game-like interface.

---

## Features

- Configurable grid size (rows and columns)
- Support for 2 to 4 players
- Click-based player placement
- Randomized movement simulation
- Detection of player meetings
- Statistical feedback including:
  - Number of runs
  - Minimum steps
  - Maximum steps
  - Average steps
- Visual grid layered on a background image
- Simple and user-friendly interface

---

## Project Structure
wandering_in_the_woods/
│
├── assets/
│ ├── images/
│ │ ├── background.png
│ │ └── sprite.png
│ └── sounds/
│ └── meet.wav
│
├── src/
│ ├── main.py
│ ├── config.py
│ ├── grid.py
│ ├── player.py
│ ├── simulation.py
│ └── stats.py
│
├── docs/
│ ├── Wandering_in_the_Woods_User_Guide.pdf
│ └── Wandering_in_the_Woods_Design_Document.pdf
│
├── requirements.txt
└── README.md



---

## Installation

1. Install **Python 3.10 or higher**  
   https://www.python.org

2. Clone or download this repository.

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt


## How to Run

Navigate to the project root and run:

python src/main.py

## How to Use

1. Use arrow keys to configure grid size.
2. Choose number of players using keys 2, 3, or 4.
3. Press ENTER to continue.
4. Click on grid cells to place players.
5. Press ENTER to start the simulation.
6. Observe player movement and statistics after each run.

## Documentation
User Guide: Explains installation and usage.
Design Document: Contains requirements and software design details.
Both documents are located in the docs/ folder.

