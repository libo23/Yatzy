import unittest
import app



class TestApp(unittest.TestCase):

    def test_throwDice(self):
        result = app.throwDice()
        self.assertIn(result, [1,2,3,4,5,6])    

    def test_getPlayersApi(self):
        result = app.getPlayersApi(3)
        self.assertEqual(result, 200)



if __name__ == '__main__':
    unittest.main()