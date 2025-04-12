import pygame
from text import Text
import random

class ScoreBoard():
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore: int = 0
        self.mRightScore: int = 0
        self.mServeStatus: int = 1
        self.mScored = 0

    def getX(self) -> float:
        return self.mX

    def getY(self) -> float:
        return self.mY

    def getWidth(self) -> float:
        return self.mWidth

    def getHeight(self) -> float:
        return self.mHeight

    def getLeftScore(self) -> int:
        return self.mLeftScore

    def getRightScore(self) -> int:
        return self.mRightScore

    def getServeStatus(self) -> int:
        return self.mServeStatus

    def isGameOver(self) -> bool:
        if self.getServeStatus() == 3 or self.getServeStatus() == 4:
            return True
        return False

    def scoreLeft(self) -> None:
        if self.isGameOver() == True:
            return
        self.mLeftScore += 1
        self.mScored = 1
        if self.mLeftScore == 9:
            self.mServeStatus = 3
            self.mScored = 3


    def scoreRight(self) -> None:
        if self.isGameOver() == True:
            return
        self.mRightScore += 1
        self.mScored = 2
        if self.mRightScore == 9:
            self.mServeStatus = 4
            self.mScored = 4

    def swapServe(self) -> None:
        if self.isGameOver() == True:
            return
        if self.getServeStatus() == 1:
            self.mServeStatus = 2
            self.mScored = 0
        elif self.getServeStatus() == 2:
            self.mServeStatus = 1
            self.mScored = 0

    def draw(self, surface):
        text_color: tuple[int, int, int] = (255, 255, 255)
        leftScoreText = Text(str(self.getLeftScore()), self.getX() + (self.getWidth() / 3.5), self.getY() + (self.getHeight() / 2), text_color, 32)
        rightScoreText = Text(str(self.getRightScore()), self.getX() + (self.getWidth() / 1.4), self.getY() + (self.getHeight() / 2), text_color, 32)
        
        color = pygame.Color(0, 0, 0)
        rect = pygame.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())
        pygame.draw.rect(surface, color, rect)

        leftScoreText.draw(surface)
        rightScoreText.draw(surface)

        leftHasScored1 = Text("LEFT HAS SCORED", self.getX() + 30, self.getY() + 80, (208, 33, 33), 80)
        #leftHasScored2 = Text("LEFT HAS SCORED", self.getX() + 30, self.getY() + 80, (248, 73, 73), 80)

        rightHasScored = Text("RIGHT HAS SCORED", self.getX() + 30, self.getY() + 80, (33, 37, 208), 80)

        leftHasWon = Text("LEFT HAS WON", self.getX() + 30, self.getY() + 80, (random.choice([208, 248]), random.choice([33, 73]), random.choice([33, 73])), 80)

        rightHasWon = Text("RIGHT HAS WON", self.getX() + 30, self.getY() + 80, (random.choice([33, 73]), random.choice([37, 77]), random.choice([208, 248])), 80)

        if self.mScored == 1:
            leftHasScored1.draw(surface)
        elif self.mScored == 2:
            rightHasScored.draw(surface)
        elif self.mScored == 3:
            leftHasWon.draw(surface)
        elif self.mScored == 4:
            rightHasWon.draw(surface)
            
            
