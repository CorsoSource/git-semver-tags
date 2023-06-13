import unittest

from git_semver_tags import Version


class TupleCompareTestCase(unittest.TestCase):

    def setUp(self):
        # tuple comparison tests
        # left, right, expecation for >, <, ==
        self.cases = [
            [(1,0,0), (1,0,0), (0, 1, 0)],
            [(1,2,3), (1,2,3), (0, 1, 0)],
            [(1,0,),  (1,),    (0, 0, 1)],
            [(1,),    (1,0,),  (1, 0, 0)],
            
            [('asdf',   ),    ('qwer',   ), (1, 0, 0)],
            
            [(5, 'asdf',),    (5, 'qwer',), (1, 0, 0)],
            [(1, 'asdf',),    (2, 'qwer',), (1, 0, 0)],
            [(2, 'asdf',),    (1, 'qwer',), (0, 0, 1)],
            [(3, 'asdf',),    (3, 'asdf',), (0, 1, 0)],
        ]
    

    def tearDown(self):
        pass


    def test_cases(self):
        # grind over cases
        for left, right, (lt_ex, eq_ex, gt_ex) in self.cases:
            self.assertTrue( lt_ex == Version._compare_tuple__lt__(left, right), '<  (__lt__) failed for %r < %r ==> %r' % (left, right, lt_ex)  )
            self.assertTrue( eq_ex == Version._compare_tuple__eq__(left, right), '== (__eq__) failed for %r == %r ==> %r' % (left, right, eq_ex) )
            self.assertTrue( gt_ex == Version._compare_tuple__gt__(left, right), '>  (__gt__) failed for %r > %r ==> %r' % (left, right, gt_ex)  )



if __name__ == '__main__':
    unittest.main()