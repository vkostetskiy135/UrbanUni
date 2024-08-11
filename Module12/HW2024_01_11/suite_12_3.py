import unittest
import tests_tournament
import tests_runner

almightyTS = unittest.TestSuite()
almightyTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_runner.RunnerTest))
almightyTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(almightyTS)