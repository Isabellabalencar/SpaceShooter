# Space Shooter Game

This is a simple **Space Shooter** game developed using **Pygame**, where the player controls a spaceship and must destroy enemies by shooting bullets. The game includes basic mechanics like movement, shooting, and scoring, with enemies randomly appearing on the screen.


## Features

- **Player Movement**: The player can move left and right using the arrow keys.
- **Shooting Bullets**: The player can shoot bullets by pressing the `SPACE` key. Each shot is unique and can only be repeated after releasing the key.
- **Enemies**: Enemies appear randomly at the top of the screen and move downward. If an enemy reaches the bottom of the screen, the player loses a life.
- **Scoring**: The player earns points by destroying enemies with the bullets.
- **Lives**: The player starts with 3 lives. If all lives are lost, the game ends.
- **Main Menu**: Before starting the game, the player can press `UP` to begin.
- **Restarting the Game**: After losing, the player can press `R` to restart the game.


## Controls

- `←` **Left Arrow**: Move the spaceship to the left.
- `→` **Right Arrow**: Move the spaceship to the right.
- `SPACE` **Space Bar**: Shoot a bullet.
- `UP` **Up Arrow**: Start the game from the main menu.
- `R` **R Key**: Restart the game after losing.

## How to Play

1. When the game starts, a menu screen will appear. Press the `UP` arrow to start playing.
2. Use the arrow keys `←` and `→` to move your spaceship sideways.
3. Press `SPACE` to shoot bullets and destroy enemies appearing at the top of the screen.
4. Each time an enemy reaches the bottom of the screen, you lose a life. The game ends when all lives are lost.
5. After losing, you can press `R` to restart the game.


## Requirements

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **Pygame**: The game uses the Pygame library. You can install it by running the following command:

```bash
pip install pygame


##Project Structure

/SpaceShooter
│
├── assets/                # Folder containing player and enemy images
│   ├── player.png         # Player's spaceship image
│   └── enemy.png          # Enemy's image
│
├── main.py                # Main game file
└── README.md              # This documentation file
