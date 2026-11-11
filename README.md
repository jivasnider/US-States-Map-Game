# US States Map Game

A geography quiz game built with Python. Test your knowledge of US geography by identifying all 50 states and locating them on a map. Enter a state name, and its location will automatically appear on the map.

## Demo

<img width="964" height="842" alt="vlc-record-2026-11-11-21h15m23s-pycharm64_wQ9Hzh8pPg mp4-" src="https://github.com/user-attachments/assets/2a254313-55c0-4215-ab7f-68c85589dcab" />



## Features

* Interactive map of the United States using Python Turtle
* Guess and identify all 50 US states
* Correct guesses are displayed at their geographical coordinates
* Score tracking to keep track of identified states
* Prevents duplicate guesses
* Generates a CSV file containing the states you haven't identified

## Requirements

* Python 3.8 or newer
* Pandas library
* Turtle module (included with Python)

## Run locally

```bash
git clone https://github.com/jivasnider/US-States-Map-Game.git
cd US-States-Map-Game
pip install pandas
python main.py
```

## Project structure

```text
US-States-Map-Game/
├── main.py                 # Main game logic
├── scoreboard.py           # Score tracking
├── 50_states.csv           # US states and geographical coordinates
├── blank_states_img.gif    # Blank US map
└── states_to_learn.csv     # States not identified
```

## What I learned

* Working with CSV files and data manipulation using Pandas
* Creating graphical interfaces with Python Turtle
* Using geographical coordinates to position elements on a map
* Implementing object-oriented programming
* Handling user input and managing game logic
* Reading and writing CSV files to store game results
