import unittest
from a_job_titles_page import TestViewJobTitlesPage
from b_add_job_title_success import TestAddJobTitlesSuccess
from c_add_job_title_failed import TestAddJobTitlesFailed
from d_cancel_add_job import TestCancelAddJobTitles
from e_update_job_title_success import TestUpdateJobTitlesSuccess
from f_update_job_title_failed import TestUpdateJobTitlesFailed
from g_delete_job_success import TestDeleteJobSuccess
from h_cancel_delete_job_success import TestCancelDeleteJobSuccess
from i_cancel_delete_multiple_job import TestCancelDeleteMultipleJob
from j_button_delete_selected_job import TestButtonDeleteSelected
from k_delete_multiple_job import TestDeleteMultipleJob

# get all tests from all test case class
a_job_titles_page = unittest.TestLoader().loadTestsFromTestCase(TestViewJobTitlesPage)
b_add_job_title_success = unittest.TestLoader().loadTestsFromTestCase(TestAddJobTitlesSuccess)
c_add_job_title_failed = unittest.TestLoader().loadTestsFromTestCase(TestAddJobTitlesFailed)
d_cancel_add_job = unittest.TestLoader().loadTestsFromTestCase(TestCancelAddJobTitles)
e_update_job_title_success = unittest.TestLoader().loadTestsFromTestCase(TestUpdateJobTitlesSuccess)
f_update_job_title_failed = unittest.TestLoader().loadTestsFromTestCase(TestUpdateJobTitlesFailed)
g_delete_job_success = unittest.TestLoader().loadTestsFromTestCase(TestDeleteJobSuccess)
h_cancel_delete_job_success = unittest.TestLoader().loadTestsFromTestCase(TestCancelDeleteJobSuccess)
i_cancel_delete_multiple_job = unittest.TestLoader().loadTestsFromTestCase(TestCancelDeleteMultipleJob)
j_button_delete_selected_job = unittest.TestLoader().loadTestsFromTestCase(TestButtonDeleteSelected)
k_delete_multiple_job = unittest.TestLoader().loadTestsFromTestCase(TestDeleteMultipleJob)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [a_job_titles_page, b_add_job_title_success, c_add_job_title_failed, d_cancel_add_job, 
     e_update_job_title_success, f_update_job_title_failed, g_delete_job_success, 
     h_cancel_delete_job_success, i_cancel_delete_multiple_job, j_button_delete_selected_job, 
     k_delete_multiple_job]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)