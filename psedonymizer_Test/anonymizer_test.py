from pseudonymizer import anonymizer
import pandas as pd
import unittest

class TestAnonymizer(unittest.TestCase):
    
    i=0
    
    def setUp(self):
        print ("Run the setUp for each testcase")
        self.df = pd.read_csv("psedonymizer_Test/testDataset.csv")   # sample testfile 
        self.classes = self.iden.suggest(self.df.columns)
        self.quasis = self.classes['qId']
        self.sensitives = self.classes["sensId"]
        TestAnonymizer.i = TestAnonymizer.i + 1
        
    def tearDown(self):
        print ("Completed running test_" + str(TestAnonymizer.i) + " for the Anonymizer class")
        
    @classmethod    
    def setUpClass(self):
        print ("Set up the class once for running all the tests")
        self.iden = anonymizer.Anonymizer("k_anon", "counter")
        
    @classmethod
    def tearDownClass(cls):
        print ("Completed running all testcases for the Anonymizer class")
        
    def test_anonymizer(self):
        
        self.assertIn('DOB', self.quasis)
        self.assertIn('postal_code', self.quasis)
        self.assertIn('income', self.sensitives)
        self.assertNotIn('companies', self.quasis)
        self.assertNotIn('color', self.sensitives)
    
    def test_anonymizer_error(self):
        dfColumns = [1, 2, 3]
        classes = self.iden.suggest(dfColumns)
        self.assertEqual(classes, -1)
        
    def test_kval(self):
        kval = self.iden.kcounter(self.df, self.quasis)
        self.assertEqual(kval, 3)

    def test_kval_errors1(self):
        self.quasis = [1, 2, 3] # set random value to quasis
        kval = self.iden.kcounter(self.df, self.quasis)
        self.assertEqual(kval, -1)
            
    def test_kval_errors2(self):
        self.quasis = list() # set random value to quasis
        kval = self.iden.kcounter(self.df, self.quasis)
        self.assertEqual(kval, -1)
        
unittest.main(argv=[''], verbosity=2, exit=False)