import unittest
from tests.quoteCollection.quoteformFH_tests import NewQuoteFHTests
from tests.quoteCollection.quoteformSH_tests import NewQuoteSHTests

# Load test cases from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(NewQuoteFHTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NewQuoteSHTests)

# Create a test suite combining all quote form test classes
quoteTest = unittest.TestSuite()

# Add test cases to the test suite
quoteTest.addTests(tc1)
quoteTest.addTests(tc2)

# Run the test suite
unittest.TextTestRunner(verbosity=2).run(quoteTest)

#
# import pytest
# from tests.sales.quoteformFH_tests import NewQuoteFHTests
# from tests.sales.quoteformSH_tests import NewQuoteSHTests
#
# # Define a list of test classes
# test_classes = [NewQuoteFHTests, NewQuoteSHTests]
#
# # Use pytest's parametrize decorator to run each test class
# @pytest.mark.parametrize('test_class', test_classes)
# def test_class(test_class):
#     # Run each test method in the test class
#     for test_method in dir(test_class):
#         if test_method.startswith('test'):
#             getattr(test_class(), test_method)()
