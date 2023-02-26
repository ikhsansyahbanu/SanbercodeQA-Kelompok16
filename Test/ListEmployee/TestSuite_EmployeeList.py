import unittest
from Success_Displayed_Employee_List import TestDisplayEmployeeList
from Success_Filter_by_Employe_id import TestFilterByEmployeeId
from Success_Filter_by_Employe_Name import TestFilterByEmployeeName
from Success_Filter_By_Supervisor_Name import TestFilterBySupervisorName

# get all tests from all test case class
Success_Displayed_Employee_List = unittest.TestLoader().loadTestsFromTestCase(TestDisplayEmployeeList)
Success_Filter_by_Employe_id  = unittest.TestLoader().loadTestsFromTestCase(TestFilterByEmployeeId)
Success_Filter_by_Employe_Name = unittest.TestLoader().loadTestsFromTestCase(TestFilterByEmployeeName)
Success_Filter_By_Supervisor_Name = unittest.TestLoader().loadTestsFromTestCase(TestFilterBySupervisorName)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [Success_Displayed_Employee_List, Success_Filter_by_Employe_id, Success_Filter_by_Employe_Name]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)