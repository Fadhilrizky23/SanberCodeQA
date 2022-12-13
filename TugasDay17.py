import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tugas_Day_17(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # LOGIN TEST CASE
    def testLogin_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(3)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("testsalah")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("testsalah")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    def testLogin_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(3)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    def test_add_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(3)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)

    def test_remove_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(2)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)

    def test_logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(2)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()


if __name__ == '__main__':
    unittest.main()
