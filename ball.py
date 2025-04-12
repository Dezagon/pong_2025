import pygame
import random

class Ball():
    def __init__(self, size: float, min_x: float, max_x: float, min_y: float, max_y: float, left_paddle_x: float, right_paddle_x: float):
        self.mX: float = min_x
        self.mY: float = min_y
        self.mSize: float = size
        self.mTopRight: tuple[float, float] = (self.mX + self.mSize, self.mY)
        self.mBottomRight: tuple[float, float] = (self.mX + self.mSize, self.mY + self.mSize)
        self.mBottomLeft: tuple[float, float] = (self.mX, self.mY + self.mSize)
        self.mRectBall: pygame.Rect = pygame.Rect(self.mX, self.mY, self.mSize, self.mSize)
        self.mDX: float = 0
        self.mDY: float = 0
        self.mMaxDX: float = 6.0
        self.mMaxDY: float = 4.0
        self.mMinX: float = min_x
        self.mMaxX: float = max_x
        self.mMinY: float = min_y
        self.mMaxY: float = max_y
        self.mLeftPaddleX: float = left_paddle_x
        self.mLeftPaddleMinY: float = min_y
        self.mLeftPaddleMaxY: float = max_y
        self.mRightPaddleX: float = right_paddle_x
        self.mRightPaddleMinY: float = min_y
        self.mRightPaddleMaxY: float = max_y

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getTopRight(self):
        return self.mTopRight

    def getBottomRight(self):
        return self.mBottomRight

    def getBottomLeft(self):
        return self.mBottomLeft

    def getSize(self):
        return self.mSize

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getMinX(self):
        return self.mMinX

    def getMaxX(self):
        return self.mMaxX

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getLeftPaddleX(self):
        return self.mLeftPaddleX

    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY

    def getRightPaddleX(self):
        return self.mRightPaddleX

    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY

    def getRectBall(self):
        return self.mRectBall
    
    
    def setPosition(self, x: float, y: float) -> None:
        if self.getMinX() <= x <= self.getMaxX() - self.getSize() and self.getMinY() <= y <= self.getMaxY() - self.getSize():
            self.mX = x
            self.mY = y
        return

    def setSpeed(self, dx: int, dy: int) -> None:
        self.mDX = dx
        self.mDY = dy

    def setLeftPaddleY(self, paddle_min_y, paddle_max_y) -> None:
        if paddle_min_y < paddle_max_y and self.getMinY() <= paddle_min_y <= self.getMaxY() and self.getMinY() <= paddle_max_y <= self.getMaxY():
            self.mLeftPaddleMinY = paddle_min_y
            self.mLeftPaddleMaxY = paddle_max_y
        return

    def setRightPaddleY(self, paddle_min_y, paddle_max_y) -> None: 
        if paddle_min_y < paddle_max_y and self.getMinY() <= paddle_min_y <= self.getMaxY() and self.getMinY() <= paddle_max_y <= self.getMaxY():
            self.mRightPaddleMinY = paddle_min_y
            self.mRightPaddleMaxY = paddle_max_y
        return

    def checkTop(self, new_y) -> float:
        if new_y <= self.getMinY():
            self.mDY *= -1.01
            y2 = self.getMinY() - new_y
            new_y = self.getMinY() + y2
            return new_y

        return new_y

    def checkBottom(self, new_y) -> float:
        if new_y + self.getSize() >= self.getMaxY():
            self.mDY *= -1.01
            y2 = (self.getSize() + new_y) - self.getMaxY()
            new_y = self.getMaxY() - (y2 + self.getSize())
            return new_y

        return new_y
            

    def checkLeft(self, new_x) -> float:
        if new_x <= self.getMinX():
            self.mDX *= 0
            self.mDY *= 0
            new_x = self.getMinX()
            return new_x

        return new_x

    def checkRight(self, new_x) -> float:
        if new_x + self.getSize() >= self.getMaxX():
            self.mDX *= 0
            self.mDY *= 0
            new_x = self.getMaxX() - self.getSize()
            return new_x

        return new_x

    #working function
    '''
    def checkLeftPaddle(self, new_x, new_y) -> float:
        mid_y = (self.getY() + new_y) / 2
        if (new_x <= self.getLeftPaddleX() and self.getX() >= self.getLeftPaddleX()) and self.getLeftPaddleMinY() <= mid_y <= self.getLeftPaddleMaxY():
            self.mDX *= -1
            x2 = self.getLeftPaddleX() - new_x
            new_x = self.getLeftPaddleX() + x2
            return new_x

        return new_x
    '''
    #testing new collision algorithm
    def checkLeftPaddle(self, new_x, new_y) -> float:
        midTopLeftY = (self.getY() + new_y) / 2
        midBottomLeftY = ((self.getY() + self.getSize()) + new_y) / 2
        if (new_x <= self.getLeftPaddleX() and self.getX() >= self.getLeftPaddleX()) and (self.getLeftPaddleMinY() <= midTopLeftY <= self.getLeftPaddleMaxY() or self.getLeftPaddleMinY() <= midBottomLeftY <= self.getLeftPaddleMaxY()):
            self.mDX *= -1.02
            x2 = self.getLeftPaddleX() - new_x
            new_x = self.getLeftPaddleX() + x2
            return new_x

        return new_x

    #testing new collision algorithm
    def checkRightPaddle(self, new_x, new_y) -> float:
        midTopRightY = (self.getY() + new_y) / 2
        midBottomRightY = ((self.getY() + self.getSize()) + new_y) / 2
        if (new_x + self.getSize() >= self.getRightPaddleX() and self.getX() + self.getSize() <= self.getRightPaddleX()) and (self.getRightPaddleMinY() <= midTopRightY <= self.getRightPaddleMaxY() or self.getRightPaddleMinY() <= midBottomRightY <= self.getRightPaddleMaxY()):
            self.mDX *= -1.02
            x2 = (new_x + self.getSize()) - self.getRightPaddleX()
            new_x = self.getRightPaddleX() - x2 - self.getSize()
            return new_x

        return new_x

    #working function
    '''
    def checkRightPaddle(self, new_x, new_y) -> float:
        mid_y = (self.getY() + new_y) / 2
        if (new_x + self.getSize() >= self.getRightPaddleX() and self.getX() + self.getSize() <= self.getRightPaddleX()) and self.getRightPaddleMinY() <= mid_y <= self.getRightPaddleMaxY():
            self.mDX *= -1
            x2 = (new_x + self.getSize()) - self.getRightPaddleX()
            new_x = self.getRightPaddleX() - x2 - self.getSize()
            return new_x

        return new_x
    '''            
            
    def move(self, dt) -> None:
        new_x = self.getX() + (self.getDX() * dt)
        new_y = self.getY() + (self.getDY() * dt)
        
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)

        new_x = self.checkLeft(new_x)
        new_x = self.checkLeftPaddle(new_x, new_y)
        
        new_x = self.checkRight(new_x)
        new_x = self.checkRightPaddle(new_x, new_y)
        
        self.mX = new_x
        self.mY = new_y


    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy) -> None:
        self.mX = x
        self.mY = random.uniform(min_y, max_y)

        self.mDX = random.uniform(min_dx, max_dx)
        self.mDY = random.uniform(min_dy, max_dy)
        

    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy) -> None:
        self.mX = x
        self.mY = random.uniform(min_y, max_y)

        self.mDX = random.uniform(-min_dx, -max_dx)
        self.mDY = random.uniform(min_dy, max_dy)



    def draw(self, surface):
        ball = pygame.Rect(self.getX(), self.getY(), self.getSize(), self.getSize())
        color = pygame.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        pygame.draw.rect(surface, color, ball)






