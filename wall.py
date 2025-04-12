import pygame

class Wall():
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height

    def getX(self) -> float:
        return self.mX

    def getY(self) -> float:
        return self.mY

    def getWidth(self) -> float:
        return self.mWidth

    def getHeight(self) -> float:
        return self.mHeight

    def getRightX(self) -> float:
        return self.mX + self.mWidth

    def getBottomY(self) -> float:
        return self.mY + self.mHeight

    def draw(self, surface):
        color = pygame.Color(255, 255, 255)
        rect = pygame.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())
        pygame.draw.rect(surface, color, rect)
