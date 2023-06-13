import unittest

from git_semver_tags import Version


class BasicTestCase(unittest.TestCase):


    def setUp(self):
        # brute forced base cases
        self.cases = [
            ['1.0.0', '1.0.0', (0, 1, 0)],
            ['0.0.0', '0.0.0', (0, 1, 0)],
            ['0.0.1', '0.0.1', (0, 1, 0)],
            ['0.1.0', '0.1.0', (0, 1, 0)],
            ['1.0.0', '1.0.0', (0, 1, 0)],
        
            ['0.0.1', '0.0.0', (0, 0, 1)],
            ['0.1.0', '0.0.1', (0, 0, 1)],
            ['1.0.0', '0.1.0', (0, 0, 1)],
            ['1.0.1', '1.0.0', (0, 0, 1)],
            ['1.1.0', '1.0.1', (0, 0, 1)],
            ['2.0.0', '1.1.0', (0, 0, 1)],
            ['2.0.0', '1.5.5', (0, 0, 1)],
        
            ['0.0.0', '0.0.1', (1, 0, 0)],
            ['0.0.1', '0.1.0', (1, 0, 0)],
            ['0.1.0', '1.0.0', (1, 0, 0)],
            ['1.0.0', '1.0.1', (1, 0, 0)],
            ['1.0.1', '1.1.0', (1, 0, 0)],
            ['1.1.0', '2.0.0', (1, 0, 0)],
            ['1.5.5', '2.0.0', (1, 0, 0)],
        ]
    

    def tearDown(self):
        pass


    def test_cases(self):
        # grind over cases
        for left, right, (lt_ex, eq_ex, gt_ex) in self.cases:
            left = Version(left)
            right = Version(right)
            
            self.assertTrue( lt_ex == (left < right),  '<  (__lt__) failed for %r < %r ==> %r' % (left, right, lt_ex)  )
            self.assertTrue( eq_ex == (left == right), '== (__eq__) failed for %r == %r ==> %r' % (left, right, eq_ex) )
            self.assertTrue( gt_ex == (left > right),  '>  (__gt__) failed for %r > %r ==> %r' % (left, right, gt_ex)  )


    def test_release(self):
        # v1 v1.2.3 v2.3 are obviously releases
        # v1.2.1-alpha is obviously a prerelease
        # v1.2-5-galb2 is 5 commits ahead of release v.1.2 
        #   and thus is NOT a release, since, well, it's not the release
        #   ... it's _after_ the release
        self.assertTrue( len([Version(v) 
                    for v 
                    #    O      O            X            X    O
                    in "v1 v1.2.3 v1.2-5-ga1b2 v1.2.1-alpha v2.3".split()
                    if Version(v)
            ]) == 3 )
        
        v2 = Version('v2.x')
        self.assertTrue( Version('v2.1') in v2       )
        self.assertTrue( Version('v1.2.3') not in v2 )



if __name__ == '__main__':
    unittest.main()