import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



class SecuritySmokeTestMovieFone(unittest.TestCase):
    _miltiprocess_can_split_ = True

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.moviefone.com/"


    def test_landing_page(self):
        page_title = "Movies | Movie Times | Movie Trailers | Movie News | TV | TV Shows | TV News - Moviefone.com"
        driver = self.driver
        base_url = self.base_url
        driver.get(base_url)
        self.assertEquals(driver.title, page_title)

    @unittest.skip('Not ready for CI')
    def test_nav_to_theater_near_you_from_main(self):
        driver = self.driver
        target_url = "http://www.moviefone.com/showtimes/alhambra-ca/91801/theaters"
        #movie time tickets css path
        mtt = "#header > div.desktop.header > div > ul > li:nth-child(1) > a"
        #theater near you path
        tny = "#header > div.desktop.header > div > ul > li:nth-child(1) > ul > li:nth-child(1) > a"
        driver.get(target_url)
        mtt_ele = driver.find_element_by_css_selector(mtt)
        tny_ele = driver.find_element_by_css_selector(tny)

        #Action Chain
        ActionChains(driver).move_to_element(mtt_ele).click(tny_ele).perform()

        loc_search_inpt = driver.find_element_by_id('location')

        self.assertEquals(loc_search_inpt.is_enabled(), True)





    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()
