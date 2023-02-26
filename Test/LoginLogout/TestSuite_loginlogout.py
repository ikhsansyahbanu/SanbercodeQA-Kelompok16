import unittest
from loginhrm import TestLogin
from logout_success import TestLogoutSuccess

# get all tests from all test case class
test_login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
test_logout = unittest.TestLoader().loadTestsFromTestCase(TestLogoutSuccess)

# create a test suite combining test cases
test_suite = unittest.TestSuite([
    test_login, test_logout
])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)