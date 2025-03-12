import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class E2ETests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')
    

    def tearDown(self):
        self.driver.quit
    

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entities', self.driver.title)


    def test_page_heading_is_text_entity_finder(self):
        heading = self._find('data-test-heading')
        self.assertEqual(heading, "Text Entities Finder")

    
    def _find(self, name):
        return self.driver.find_element(By.NAME, name).text
        