import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CalculatorUITest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless') # Necessary for Jenkins to run without a monitor
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=options)

    def test_title(self):
        self.driver.get("http://localhost:5000") # Jenkins will test local build
        self.assertIn("DevOps Calc", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
