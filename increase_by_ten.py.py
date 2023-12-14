def increase_by_ten(numbers):
    return [number + 10 for number in numbers]
    
import unittest

class IncreaseByTenTest(unittest.TestCase):

    def test_increase_by_ten(self):
        numbers = [1, 2, 3, 4, 5]
        expected_results = [11, 12, 13, 14, 15]
        actual_results = increase_by_ten(numbers)
        self.assertEqual(actual_results, expected_results)

if __name__ == "__main__":
    unittest.main()
