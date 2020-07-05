import os
import unittest

from code_template import cd


class TestCdAssignment(unittest.TestCase):

    test_dir_name = './my_tmp_dir'
    curr_dir_name = os.getcwd()

    @classmethod
    def setUpClass(cls) -> None:
        if not os.path.isdir(cls.test_dir_name):
            os.mkdir(cls.test_dir_name)

    @classmethod
    def tearDownClass(cls) -> None:
        if os.path.isdir(cls.test_dir_name):
            os.rmdir(cls.test_dir_name)

    def test_enter_implemented(self):
        self.assertIn('__enter__', dir(cd),
                      '__enter__ method not implemented')

    def test_exit_implemented(self):
        self.assertIn('__exit__', dir(cd),
                      '__exit__ method not implemented')

    def test_dir_check_implemented(self):
        with self.assertRaises(ValueError, msg='ValueError should be raised if dir does not exist'):
            cd('ajdfjd')

    def test_enter(self):
        with cd(self.test_dir_name):
            self.assertEqual(os.getcwd(), self.curr_dir_name + self.test_dir_name[1:],
                             'Current dir is wrong after context enter')

    def test_exit(self):
        with cd(self.test_dir_name):
            pass
        self.assertEqual(os.getcwd(), self.curr_dir_name,
                         'Previous dir was not restored after context exit')


if __name__ == '__main__':
    unittest.main()
