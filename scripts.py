import unittest
import math

class test_CalcMethods(unittest.TestCase):

    def test_calculateSum(self):
        self.assertEqual(calc.add(5, 25, 90))
        
    def test_calculateMean(self):
        self.assertEqual(calc.mean(5, 25, 90), 40)
        
    def test_calcuateGcd(self):
        self.assertEqual(calc.gcd(5, 25, 90), 5)        
                        
class test_InRange(unittest.TestCase):
    #input within range of parameters
    def  test_firstInputRange(self):
        self.assertTrue(input1 =(1, 10))
        self.assertFalse(input1 != (1, 10))

    def test_secondInputRange(self):
        self.assertTrue(input2 = (20, 30))
        self.assertFalse(input2 != (20, 30))

    def test_thirdInputRange(self):
        self.assertTrue(input3 = (70, 100))
        self.assertFalse(input3 != (70, 100))

class test_isInputNotNumber(unittest.TestCase):
    # input is not an integer
    def test_FirstInput(self):
        self.assertTrue (input1 = int)
        self.assertFalse (input1 != int)

    def test_SecondInput(self):
        self.assertTrue (input2 = int)
        self.assertFalse (input2 != int)

    def test_ThirdInput(self):
        self.assertTrue (input3 = int)
        self.assertFalse (input3 != int)
        
class test_isInputPresent(unittest.TestCase):
    # no input detected test
    def test_FirstInputPresent(self):
        self.assertTrue(input1 = "")
    def test_SecondInputPresent(self):
        self.assertTrue(input2 = "")
    def test_ThirdInputPresent(self):
        self.assertTrue(input3 = "")

class test_isResultChosen(unittest.TestCase):
    def test_isResultPicked(self):
        self.assertTrue(option1, option2, option3)

class test_userRecieves(unittest.TestCase):
    def test_isUserRecievingAlert(self):
        self.assertTrue(alert = userError)
        
if __name__ == '__main__':
    unittest.main()
