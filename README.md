# Squash Referee Program

A simple command-line program to help keep score and manage a squash match, designed for use by referees or players. Can be run locally in your terminal.

(PS: This is a basic prototype version for a first project, planning on improving it later with more useful features not seen elsewhere in other apps)

## Features

- Track player names, scores, and games won
- Supports Best of 3 and Best of 5 match formats
- Visual scoreboard with serve indicators
- Undo last point, change server, and reset match
- Simple keyboard controls for fast operation

## Getting Started

### Requirements

- Python 3.7 or higher

### Running the Program

1. Clone this repository:
   ```sh
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
2. Run the main program:
   ```sh
   python main.py
   ```

## Usage

- Enter player names when prompted (or press Enter for defaults)
- Select match format (Best of 3 or Best of 5)
- Use the on-screen controls to score points, change server, or reset the match
- Quit at any time with `Q`

## Controls

- `1` - Point to Player 1
- `2` - Point to Player 2
- `U1` - Undo last point for Player 1
- `U2` - Undo last point for Player 2
- `S1` - Set Player 1 as server
- `S2` - Set Player 2 as server
- `L` - Serve from Left
- `R` - Serve from Right
- `RESET` - Reset match
- `Q` - Quit
