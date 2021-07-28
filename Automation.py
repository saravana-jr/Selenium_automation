from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys


class Atgwebsite(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Ganesh/Desktop/chromedriver/chromedriver.exe")
        driver=self.driver
        driver.get("https://www.atg.party/")
        driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()
        time.sleep(2)
        driver.find_element_by_name("email").send_keys("wiz_saurabh@rediffmail.com")
        driver.find_element_by_name("password").send_keys("Pass@123")
        driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(5)

    def test_a_profile(self):
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/p/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[2]/div[2]/div[2]/div/a[1]/div[2]/span[1]").click()
        driver.find_element_by_id("edt-prof").click()

    def test_b_postarticle(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[1]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[1]/div/div/a[1]").click()
        driver.find_element_by_id("title").send_keys("testing")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div").send_keys("This is for testing")
        driver.find_element_by_id("hpost_btn").click()
        time.sleep(5)

    def test_firstname(self):
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/p/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[2]/div[2]/div[2]/div/a[1]/div[2]/span[1]").click()
        driver.find_element_by_id("edt-prof").click()
        time.sleep(5)
        fn=driver.find_element_by_id("first_name").send_keys("Spider")
        self.assertEqual("Spider",fn,"First name is not Taken")
        ln=driver.find_element_by_id("last_name").send_keys("man")
        self.assertEqual("Spider",ln, "First name is not Taken")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Atgwebsite)
    unittest.TextTestRunner(verbosity=2).run(suite)