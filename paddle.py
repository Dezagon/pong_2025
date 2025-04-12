import pygame

class Paddle():
    def __init__(self, x, y, width, height, speed, min_y, max_y, color: pygame.Color):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mSpeed = speed
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mColor = color

    def getX(self) -> float:
        return self.mX

    def getY(self) -> float:
        return self.mY

    def getWidth(self) -> float:
        return self.mWidth

    def getHeight(self) -> float:
        return self.mHeight

    def getRightX(self) -> float:
        return self.getX() + self.getWidth()

    def getBottomY(self) -> float:
        return self.getY() + self.getHeight()

    def getSpeed(self) -> float:
        return self.mSpeed

    def getMinY(self) -> float:
        return self.mMinY

    def getMaxY(self) -> float:
        return self.mMaxY

    def getColor(self) -> pygame.Color:
        return self.mColor

    def setPosition(self, y) -> None:
        if y > self.getMaxY() - self.getHeight() or y < self.getMinY():
            return
        self.mY = y

    def moveUp(self, dt) -> None:
        self.mY -= dt * self.getSpeed()
        if self.mY <= self.getMinY():
            self.mY = self.getMinY()

    def moveDown(self, dt) -> None:
        self.mY += dt * self.getSpeed()
        if self.mY >= self.getMaxY() - self.getHeight():
            self.mY = self.getMaxY() - self.getHeight()

    def draw(self, surface) -> None:
        rect = pygame.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())
        pygame.draw.rect(surface, self.getColor(), rect)

