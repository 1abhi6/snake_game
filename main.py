"""
Snake Game using Hand Tracking with OpenCV and Python

This code implements a simple Snake Game that is controlled using hand gestures
captured by a webcam. It uses the Hand Tracking Module from the cvzone library
to detect hand landmarks and control the movement of the snake.

The game consists of a snake that moves around the screen and tries to eat
food items. The player's hand is used to control the snake's direction.

Usage:
1. Run the script, and it will open the webcam to start the game.
2. Move your hand in the webcam frame to control the snake.
3. Try to make the snake eat the food items to increase your score.
4. Press 'q' to quit the game.
5. Press 'r' to restart the game if you lose.

Requirements:
- OpenCV
- NumPy
- cvzone

Note: Make sure to have the "Donut.png" image file in the "resources" directory
for the food item.

Author: Abhishek Gupta
Date: 09 Oct, 2023
"""

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone
import math
import random

detector = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGameClass:
    def __init__(self, pathFood):
        self.points = []  # All points of the snake
        self.lengths = []  # Distance between each point
        self.currentLength = 0  # Total Length of the snake
        self.allowedLength = 150  # Total allowed length
        self.previousHead = 0, 0  # Previous head point
        self.score = 0  # Keep track of score
        self.gameOver = False  # Keep track of game over

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 550), random.randint(100, 500)

    def update(self, imgMain, currentHead):
        if self.gameOver:
            cvzone.putTextRect(imgMain, 'Game Over', [100, 150], scale=7, thickness=5)
            cvzone.putTextRect(imgMain, f'Your Score {self.score}', [100, 150], scale=7, thickness=5)
        else:

            px, py = self.previousHead
            cx, cy = currentHead

            self.points.append([cx, cy])
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length Reduction
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)

                    if self.currentLength < self.allowedLength:
                        break

            # Check if snake ate the food
            rx, ry = self.foodPoint
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                print(self.score)

            # Draw snake
            if self.points:
                for i, point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            # Draw Food
            rx, ry = self.foodPoint
            imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))
            cvzone.putTextRect(imgMain, f'Score {self.score}', [5, 10], scale=1, thickness=1)

            # Check for Collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            print(minDist)

            if -1 <= minDist <= 1:
                print('Hit')
                self.gameOver = True
                # Reset the values
                self.points = []
                self.lengths = []
                self.currentLength = 0
                self.allowedLength = 150
                self.previousHead = 0, 0
                self.randomFoodLocation()

        return imgMain


game = SnakeGameClass("resources/Donut.png")

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) == ord('r'):
        game.gameOver = False

    cv2.imshow('Image', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
