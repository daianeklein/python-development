def setUpModule():             # runs once before any tests
def tearDownModule():          # runs once after all tests
# 
class MyTestCases(TestCase):   # the start of a test case

    @classmethod
    def setUpClass(cls):       # runs once before test case
# 
    @classmethod
    def tearDownClass(cls):    # runs once after test case
# 
    def setUp(self):           # runs before each test

    def tearDown(self):        # runs after each test