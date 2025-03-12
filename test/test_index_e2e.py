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
        heading = self._find('data-test-heading').text
        self.assertEqual(heading, "Text Entities Finder")

    def test_input_element_is_not_empty(self):
        input_element = self._find('data-test-input')
        self.assertIsNotNone(input_element)


    def test_page_has_submit_button_for_submitting_text(self):
        submit_button = self._find('data-test-submit')
        self.assertIsNotNone(submit_button)


    def test_ter_table_table_exists(self):
        input_element = self._find('data-test-input')
        submit_button = self._find('data-test-submit')
        input_element.send_keys('Eugene is in Cameroon')
        table = self._find('data-test-ner-table')
        self.assertIsNotNone(table)


    def _find(self, name):
        return self.driver.find_element(By.NAME, name)
        