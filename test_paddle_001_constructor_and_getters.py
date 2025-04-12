"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import paddle

class TestPaddleConstructor( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 125
        self.expected_y = 250
        self.expected_width = 25
        self.expected_height = 100
        self.expected_speed = 90
        self.expected_min_y = 200
        self.expected_max_y = 800

        self.paddle = paddle.Paddle( self.expected_x, self.expected_y, self.expected_width, self.expected_height, self.expected_speed, self.expected_min_y, self.expected_max_y )

        return

    def tearDown( self ):
        return

    def test001_XIsSet( self ):
        self.assertEqual( self.paddle.getX( ), self.expected_x )
        return

    def test002_YIsSet( self ):
        self.assertEqual( self.paddle.getY( ), self.expected_y )
        return

    def test003_WidthIsSet( self ):
        self.assertEqual( self.paddle.getWidth( ), self.expected_width )
        return

    def test004_HeightIsSet( self ):
        self.assertEqual( self.paddle.getHeight( ), self.expected_height )
        return

    def test005_SpeedIsSet( self ):
        self.assertEqual( self.paddle.getSpeed( ), self.expected_speed )
        return

    def test006_RightXIsCorrect( self ):
        self.assertEqual( self.paddle.getRightX( ), self.expected_x + self.expected_width )
        return

    def test007_BottomYIsCorrect( self ):
        self.assertEqual( self.paddle.getBottomY( ), self.expected_y + self.expected_height )
        return

    def test008_MinYIsSet( self ):
        self.assertEqual( self.paddle.getMinY( ), self.expected_min_y )
        return

    def test009_MaxYIsSet( self ):
        self.assertEqual( self.paddle.getMaxY( ), self.expected_max_y )
        return

def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestPaddleConstructor )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
