import unittest
from OfflineAlgo import *

class MyTestCase(unittest.TestCase):


    def test_reFill(self):
        arr1 = []
        arr2 = []
        arr3 = []
        expect1 = [0,1,2,3,4]
        notExpect1 = [0,1,2,3,4,5]
        expect2 = [0,1,0,1,0,1]
        expect3 = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
        reFill(arr1 ,1 , 5)
        reFill(arr2 , 3 , 2)
        reFill(arr3 , 2 , 10)
        self.assertEqual(expect1 , arr1)
        self.assertEqual(expect2, arr2)
        self.assertEqual(expect3 , arr3)
        self.assertNotEqual(notExpect1 , arr1)
