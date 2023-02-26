import unittest
from a_accesslocationpage import Testaccessloginpage
from b_adddata import Testadddata
from c_searchdata import Testsearchdata
from d_canceldelete import Testcanceldelete
from e_deletedata import Testdeletedata

# get all tests from all test case class
a_accesslocationpage = unittest.TestLoader().loadTestsFromTestCase(Testaccessloginpage)
b_adddata = unittest.TestLoader().loadTestsFromTestCase(Testadddata)
c_searchdata = unittest.TestLoader().loadTestsFromTestCase(Testsearchdata)
d_canceldelete = unittest.TestLoader().loadTestsFromTestCase(Testcanceldelete)
e_deletedata = unittest.TestLoader().loadTestsFromTestCase(Testdeletedata)

# create a test suite combining test cases
test_suite = unittest.TestSuite([a_accesslocationpage,b_adddata,c_searchdata,d_canceldelete,e_deletedata ])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)