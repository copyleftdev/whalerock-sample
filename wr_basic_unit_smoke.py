import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SmokeTestWhaleRockCorpSite(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Firefox()

    def test_landing_page_title(self):
        driver  = self.driver
        driver.get("http://www.whalerockindustries.com/")
        self.assertEquals(driver.title, "Whalerock Industries")

    def test_about_link(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/about")
        self.assertEquals(driver.title, "About Whalerock Industries")

    def test_new_link(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/news/")
        self.assertEquals(driver.title, "Whalerock Industries - News")

    def test_career_apply_link(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/apply/")
        self.assertEquals(driver.title, "Careers at Whalerock Industries")

    def test_scroll_down(self):
        driver = self.driver
        driver.get

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
