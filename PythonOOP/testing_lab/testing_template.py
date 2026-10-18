from unittest import TestCase, main


class TestClassName(TestCase):
    def test_init(self):
        pass


if __name__ == '__main__':
    main()

# The possible outcomes are
# ▪ OK – all tests passed
# ▪ FAIL – one or more tests failed, and an AssertionError
# exception is raised
# ▪ ERROR – the tests raised an exception other
# than AssertionError

#
# unittest.TestCase – create test cases by subclassing it

# ▪ assertEqual() / assertNotEqual() – tests that the two
# arguments are equal / unequal in value

# ▪ assertTrue() / assertFalse() – tests that the
# argument has a Boolean value of True/False

# ▪ assertIn() / assertNotIn() – tests that the first
# argument is in / is not in the second

# assertRaises() – raises a specific exception

# ▪ unittest.main() – provides a command-line interface to
# the test script

# ▪ setUp() – prepares the test fixture
# ▪ The method is called immediately before the test method
