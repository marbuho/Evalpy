# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:37:01 2021

@author: Tincho
"""
import unittest

class test_evaluacion(unittest.TestCase):

   def test_balancecorchetes(self):
        from evalpy.bala_corch  import bala_corch
        self.assertTrue(bala_corch(""))
        # self.assertTrue(bala_corch("[]"))
        # self.assertFalse(bala_corch("[[]["))
        # self.assertTrue(bala_corch("[][]"))
        # self.assertTrue(bala_corch("[[]]"))
        # self.assertTrue(bala_corch("[[[][]]]"))
        # self.assertFalse(bala_corch("]["))
        # self.assertFalse(bala_corch("]"))
        # self.assertFalse(bala_corch("["))
        # self.assertTrue(bala_corch(""))
        # self.assertFalse(bala_corch("][]["))
        # self.assertFalse(bala_corch("[][]]["))
    
   def test_dar_cambio(self):
       from evalpy.darcambio  import  darcambio
       self.assertEqual([100,50],  darcambio(250,100),"Debe ser 150$")
       self.assertEqual([100],  darcambio(200,100),"Debe ser 100$")
    #     self.assertEqual([200, 200, 50, 20, 20, 5, 2, 2],  darcambio(500,1),"Debe ser 499")
    #     self.assertEqual([1-100], darcambio(1,100),"debe indicar que faltan 99")
        

if __name__ == '__main__':
    unittest.main()
