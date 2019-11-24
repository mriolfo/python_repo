import unittest
from code.helloWorld import HelloWorld


class HelloWorldTest(unittest.TestCase):

    # function test name always must start with test_function_to_test

    def test_def_hello_world(self):
        self.assertEqual(HelloWorld.def_hello_world(self), "Hello World")


if __name__ == '__main__':
    unittest.main()
