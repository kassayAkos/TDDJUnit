from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 faild" == result.summary())
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 faild" == result.summary())
    def tastFailedResultFormatting(self):
        result = TestResukt()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 faild" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
TestCaseTest("tastFailedResultFormatting").run()
