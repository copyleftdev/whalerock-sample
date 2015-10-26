import unittest
from selenium import webdriver
import requests





class SmokeTestWhaleRockCorpSite(unittest.TestCase):
    _multiprocess_can_split_ = True

    def setUp(self):
        self.driver =webdriver.Firefox()

    def test_no_cache_true(self):
        base_url = "http://www.whalerockindustries.com/"
        r = requests.get(base_url)
        cache_check = r.headers.get('Cache-Control')
        self.assertEquals(cache_check, "no-cache")


    def test_javascript_cdn_payload(self):
        base_cdn_url = "http://cdnjs.cloudflare.com"
        js_assets = ['/ajax/libs/modernizr/2.7.1/modernizr.min.js','/ajax/libs/jquery/1.11.2/jquery.min.js']
        for each_asset in js_assets:
            asset_req = requests.get("{}{}".format(base_cdn_url, each_asset))
        self.assertEquals(asset_req.status_code, 200)

    def test_css_cdn_payload(self):
        base_cdn_url = "http://cdnjs.cloudflare.com"
        css_assets = ['/ajax/libs/normalize/3.0.0/normalize.min.css']
        for each_asset in css_assets:
            asset_req = requests.get("{}{}".format(base_cdn_url, each_asset))
            self.assertEquals(asset_req.status_code, 200)

    def test_applestore_assets(self):
        apple_base_url = "http://appstore.com/"

        store_assets = ['KimKardashianWest','KendallJenner']
        for each_asset in store_assets:
            asset_req = requests.get("{}{}".format(apple_base_url, each_asset))
        url_shortner_asset = requests.get("https://appsto.re/us/4N_g9.I")
        self.assertEquals(asset_req.status_code, 200)
        self.assertEquals(url_shortner_asset.status_code, 200)

    def test_googleplay_store_assets(self):
        google_play_base_url = "https://play.google.com/store/apps/"
        store_assets = ['details?id=com.whalerock.kendall','details?id=com.whalerock.kylie']
        for each_asset in store_assets:
            asset_req = requests.get("{}{}".format(google_play_base_url, each_asset))
            self.assertEquals(asset_req.status_code, 200)

    def test_landing_page_title(self):
        driver  = self.driver
        driver.get("http://www.whalerockindustries.com/")
        self.assertEquals(driver.title, "Whalerock Industries")

    def test_about_page_title(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/about")
        self.assertEqual(driver.title, "About Whalerock Industries")

    def test_news_page_title(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/news")
        self.assertEquals(driver.title, "Whalerock Industries - News")

    def test_apply_page_title(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/apply/")
        self.assertEquals(driver.title, "Careers at Whalerock Industries")

    def test_landing_pagination_presents(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/")
        pagelements = driver.find_element_by_class_name("onepage-pagination")
        self.assertEqual(pagelements.tag_name, u"ul")

    def test_pagination_navigation_down(self):
        driver = self.driver
        driver.get("http://www.whalerockindustries.com/")
        for i in range(1,19):
            driver.find_element_by_xpath('/html/body/ul/li[{}]/a'.format(i)).click()
        self.assertEquals(driver.current_url, "http://www.whalerockindustries.com/#18")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
