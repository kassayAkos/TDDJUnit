from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):
    def TestRunning(self):
        test = WasRun("testMethod")
        assert(not test.WasRun)
        test.run()
        assert(test.WasRun)

TestCaseTest("TestRunning").run()
