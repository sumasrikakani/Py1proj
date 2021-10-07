import unittest
import calc

class TestCalc(unittest.TestCase):
    '''
    Test the add function from the calc library
    '''

    def test_add_integers(self):
        """
        Test the addition of two integers returns the correct total
        """
        result=calc.add2(1,2)
        self.assertEqual(result,3)

    def test_add_floats(self):
        '''
        Test that the addition of two floats returns the correct result
        '''
        result=calc.add2('10.5',2)
        self.assertEqual(result,12.5)

    def test_add_string_number(self):
        '''
        Test that the addition of string and floats returns the correct result
        '''
        result = calc.add2('10.5', 'abc')
        self.assertEqual(result, '10.5abc')

if __name__ == "__main__":
    unittest.main()