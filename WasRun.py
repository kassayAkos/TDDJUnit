from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.WasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.WasRun = 1
