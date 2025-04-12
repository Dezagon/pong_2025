"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import score_board

class TestScoreBoardConstructor( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 125
        self.expected_y = 250
        self.expected_width = 400
        self.expected_height = 200

        self.board = score_board.ScoreBoard( self.expected_x, self.expected_y, self.expected_width, self.expected_height )

        return

    def tearDown( self ):
        return

    def test001_XIsSet( self ):
        self.assertEqual( self.board.getX( ), self.expected_x )
        return

    def test002_YIsSet( self ):
        self.assertEqual( self.board.getY( ), self.expected_y )
        return

    def test003_WidthIsSet( self ):
        self.assertEqual( self.board.getWidth( ), self.expected_width )
        return

    def test004_HeightIsSet( self ):
        self.assertEqual( self.board.getHeight( ), self.expected_height )
        return

    def test005_LeftScoreIsZero( self ):
        self.assertEqual( self.board.getLeftScore( ), 0 )
        return

    def test006_RightScoreIsZero( self ):
        self.assertEqual( self.board.getRightScore( ), 0 )
        return

    def test007_StatusIsLeftServe( self ):
        self.assertEqual( self.board.getServeStatus( ), 1 )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestScoreBoardConstructor )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
