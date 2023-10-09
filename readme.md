# Hand-Controlled Snake Game with OpenCV and Python

![Snake Game Demo](demo.gif)

## Overview

This project is a hand-controlled Snake Game implemented using OpenCV and Python. It allows you to play the classic Snake Game by moving your hand in front of a webcam, making it a fun and interactive experience. The snake follows your hand gestures as you navigate it to collect food items and increase your score.

## Features

- Hand tracking using OpenCV
- Real-time snake movement control
- Score tracking and game over conditions
- Responsive food item placement
- Easy-to-use and interactive gameplay

## Demo

Watch a short demo of the game in action [here](demo.gif).

## Requirements

To run the game, you'll need the following libraries and tools:

- Python 3.x
- OpenCV
- NumPy
- cvzone
- A webcam

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
   ```

2. Install the required libraries:

   ```shell
   pip install opencv-python numpy cvzone
   ```

3. Run the game:

   ```shell
   python snake_game.py
   ```

4. Follow the on-screen instructions to control the snake with your hand.

## How it Works

The game uses OpenCV for hand tracking, detecting landmarks on your hand, and calculating the snake's movement based on your hand's position. When the snake eats food, your score increases. If the snake collides with its own body, the game ends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [cvzone](https://github.com/cvzone/cvzone) - A computer vision library that simplifies working with OpenCV.
- [OpenCV](https://opencv.org/) - An open-source computer vision library.

## Author

- [Abhishek Gupta](https://github.com/1abhi6)

Feel free to contribute to this project or reach out for questions and collaborations.

Enjoy playing the Hand-Controlled Snake Game!

![Snake Game](game_screenshot.png)