import unittestfrom main import *class AddTestCase(unittest.TestCase):    def setUp(self) -> None:        print('Ish boshlandi')    def tearDown(self) -> None:        print('tazalaydi')    def test_random(self):        self.assertEqual(add(4, 4), 8)if __name__ == '__main__':    unittest.main()