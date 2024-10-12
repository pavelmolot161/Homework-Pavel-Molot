import unittest
import tests_12_3

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

TestSuite = unittest.TextTestRunner(verbosity=2)

TestSuite.run(calcST)

### - 'это задание помогло мне понять принципы работы методов тестирования, спасибо разработчикам !!!!!!!!!