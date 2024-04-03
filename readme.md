# Piano Tiles Automation

This project is an automation script designed to play Piano Tiles, a popular mobile game that challenges players to tap on the black tiles as they appear on the screen while avoiding the white tiles. Born out of a mix of fascination and frustration, this script aims to master the game by achieving high scores without manual intervention.

## Overview

Piano Tiles is deceptively simple but can quickly become challenging and, at times, frustrating. This project uses Python and several libraries to analyze the game's screen in real-time, identify the position of the black tiles, and simulate screen taps accordingly.

The automation script is capable of playing the game with impressive accuracy and speed, outperforming human reaction times. Whether you're interested in how automation can be applied to games, looking to learn more about image recognition and screen manipulation in Python, or simply want to set unbeatable high scores, this project offers a bit of everything.

## Features

- **Real-time Screen Analysis**: Quickly scans the game screen for black tiles.
- **Automated Gameplay**: Simulates clicks/taps on the correct tiles to play the game.
- **Customizable Settings**: Allows users to adjust the script's sensitivity and speed.
- **High Score Tracking**: Keeps track of and displays high scores achieved by the automation.

## Getting Started

### Prerequisites

Before you can run the script, you'll need to have Python installed on your machine along with a few libraries. This project was developed with Python 3.8, but it should be compatible with newer versions as well.

### Installation

1. Clone the repository to your local machine:
```sh
   git clone https://github.com/SidmoGoesBrrr/Piano-Tiles-Automation
```
2. Navigate to the project directory:
```sh
cd piano-tiles-automation
```
3. Install the required Python libraries:

```sh
pip install pyautogui keyboard pywin32
```

### Running the Script
To start the automation, ensure the Piano Tiles game is visible on your screen and run:

```sh
python game.py
```
### How It Works

The script operates by continuously capturing a portion of the screen where the game is expected to display the tiles. It analyzes these screenshots in real-time to detect the presence of black tiles and simulates mouse clicks or screen taps at these locations.