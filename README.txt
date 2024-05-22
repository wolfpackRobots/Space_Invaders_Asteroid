# Space Dodge

Space Dodge is an exciting arcade-style game where the player must navigate a spaceship to avoid incoming asteroids while shooting projectiles to destroy them. The game gets progressively more challenging as time goes on, and players can aim to achieve high scores.

## Table of Contents

- Introduction
- Installation
- How to Play
- Game Features
- Code Structure
- Credits
- Acknowledgements

## Introduction

Our primary goal was to create a 2D shooter video game in the style of a "shoot 'em up" game. The project, Space Dodge, inspired by Space Invaders, commenced in mid-January and reached completion on May 20th, 2024. Throughout the development process, we encountered various challenges, all of which were eventually overcome, albeit with the need for numerous revisions and adjustments. Despite the final result differing from our initial vision, we acquired invaluable knowledge and are proud of the outcome.

Some of the challenges we encountered included:

- Transitioning from a Simple Design: Initially, our game featured a simple white rectangle on a black screen. Transitioning to a more complex spinning PNG image was challenging, as finding a suitable PNG that met our requirements took considerable time and effort. This was resolved in the final weeks of the project.
- Exploding Sprites: Creating and implementing exploding sprites when asteroids are destroyed also presented challenges.
- Sound: Some earlier issues we had with the sound function was that it would continuously repeat itself even after using the shoot button but all we had to do was reformat the sound function.

## How to Play

- Movement: Use the arrow keys to move your spaceship.
- Shoot: Press the spacebar to shoot projectiles at the incoming asteroids.
- Pause: Press the ESC key to pause the game.
- Restart: After dying, press Y to play again or N to exit.

Avoid colliding with asteroids while trying to shoot them down to increase your score. The game gets more difficult as more asteroids appear and move faster.

## Game Features

- Dynamic Difficulty: Asteroids increase in number and speed as the game progresses.
- High Scores: Top scores are saved and displayed at the end of each game.
- Explosions: Visual effects for when asteroids are destroyed.
- Background Stars: Animated stars in the background to enhance the visual experience.
- Sound Effects: Realistic sounds for shooting and explosions.

### Initialization

- Game Window: Set up with dimensions 1500x768.
- Player and Projectile: Dimensions and velocities defined for smooth gameplay.
- Asteroids: Random sizes and velocities for dynamic obstacles.
- Assets: Player and asteroid images loaded, and sound effects initialized.

### Classes

- Star: Represents background stars with movement and drawing methods.
- Explosion: Manages explosion animations when asteroids are destroyed.

### Main Functions

- draw(): Handles all rendering for the game window, including player, asteroids, projectiles, and stars.
- show_death_message(): Displays the death message and top scores, allowing the player to restart or exit.
- main(): The main game loop handling game logic, including player input, asteroid generation, collision detection, and scoring.

## Credits

- Images: Player and asteroid images (galaga.png and Asteroid.png) used in the game.
- Sounds: Explosion and shooting sounds (explosion.wav and shoot.wav).

## Acknowledgements

In the early stages, we found guidance from these helpful resources:
- CHATGPT: Assisted with asteroid sizes/movement, background design, and explosion sprite.
- Tech With Tim: [Tech With Tim YouTube Channel](https://www.youtube.com/watch?v=waY3LfJhQLY)

Feel free to fork this repository and contribute to improving the game. Enjoy playing Space Dodge!

## Future plans: we plan to add a 3d background (not a moving downwards png), power-ups, and a GUI (Graphics User Interface) 
