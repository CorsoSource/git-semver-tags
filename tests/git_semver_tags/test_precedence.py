import unittest

from git_semver_tags import Version


class PrecedenceTestCase(unittest.TestCase):

    def setUp(self):
        # given precedence test cases
        self.precedence_tests = [
            '1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0'.split(' < '),
            'v1 < 2.0 < v2.0.1 < 2.0.1-6-g345abcd123 < 2.0.1-8-g123cab < v2.1 < 2.1.0-1-ga1a1a < 3'.split(' < '),
        ]


    def tearDown(self):
        pass


    def test_cases(self):
        # check all against all subsequent
        for precedence_cases in precedence_tests:
            for i, case in enumerate(precedence_cases[:-1]):
                case = Version(case)
                for next_case in precedence_cases[i+1:]:
                    next_case = Version(next_case)
                    
                    self.assertTrue( case < next_case, 'Failed precedence check: %r < %r' % (case._raw, next_case._raw) )
            
            precedence_cases = list(reversed(precedence_cases))
            
            for i, case in enumerate(precedence_cases[:-1]):
                case = Version(case)
                for next_case in precedence_cases[i+1:]:            
                    next_case = Version(next_case)
                    
                    self.assertTrue( case > next_case, 'Failed precedence check: %r > %r' % (case._raw, next_case._raw) )



if __name__ == '__main__':
    unittest.main()