import unittest
from tests.customer_service.newconsignment_fh_tests import NewConsignmentFHTests
from tests.customer_service.newconsignment_sh_tests import NewConsignmentSHTests
from tests.customer_service.newconsignment_ddt_tests import NewConsignmentDDTTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(NewConsignmentFHTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NewConsignmentSHTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(NewConsignmentDDTTests)

# create a test suite combining all test classes - end to end test

endtoendTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(endtoendTest)
