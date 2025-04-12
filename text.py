import pygame
from pygame import Surface

class Text:

    def __init__(self, string: str, x: float, y: float, color: tuple[int, int, int], height: int) -> None:
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor = color
        font_height = height
        self.mFont = pygame.font.Font('font/Gamer.ttf', font_height)

    def setText(self, string: str) -> None:
        self.mString = string

    def setColor(self, color: tuple[int, int, int]) -> None:
        self.mColor = color

    def setSize(self, size: int) -> None:
        self.mFont = pygame.font.Font("font/Gamer.ttf", size)

    def draw(self, surface: Surface) -> None:
        text_object = self.mFont.render(self.mString, False, self.mColor)
        text_rect = text_object.get_rect()
        text_rect.center = (int(self.mX), int(self.mY))
        surface.blit(text_object, text_rect)
