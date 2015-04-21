# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

class WebTestCase(unittest.TestCase):
    build = ""
    url = ""
    desired_cap = {}
    wait_seconds = 0

    def setUp(self):

    def tearDown(self):
        self.driver.save_screenshot('screenshot.png')
        self.driver.quit()

    def remoteDriver(self, url):
        WebTestCase.desired_cap["project"] = project
        WebTestCase.desired_cap["build"] = WebTestCase.build
        self.driver = webdriver.Remote(url, desired_capabilities = WebTestCase.desired_cap)
        self.wait = WebDriverWait(self.driver, WebTestCase.wait_seconds)

    def loadPage(self, title):
        self.wait.until(EC.title_is(title))

    def switchToWindow(self, title):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to_window(handles[len(handles) - 1])
            try:
                self.loadPage(title)
            except TimeoutException:
                self.driver.switch_to_window(handles[len(handles) - 2])

    def switchToLightbox(self, path):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, path)))

    def switchToFrame(self, name):
        self.wait.until(EC.visibility_of_element_located((By.ID, name)))
        self.driver.switch_to_frame(name)

    def clickElement(self, path):
        if WebTestCase.wait_seconds > 0:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()
        else:
            self.driver.find_element_by_xpath(path).click()

    def selectOption(self, path, index):
        if WebTestCase.wait_seconds > 30:
            self.clickElement(path)
            Select(self.driver.find_element_by_xpath(path)).select_by_index(index)
        elif WebTestCase.wait_seconds > 20:
            Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, path)))).select_by_index(index)
        else:
            Select(self.driver.find_element_by_xpath(path)).select_by_index(index)

    def inputText(self, path, text):
        if WebTestCase.wait_seconds > 0:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, path))).send_keys(text)
        else:
            self.driver.find_element_by_xpath(path).send_keys(text)

    def getText(self, path):
        if WebTestCase.wait_seconds > 0:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, path))).text
        else:
            return self.driver.find_element_by_xpath(path).text

    def testChrome(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = desired_cap = {'browser': 'Chrome', 'browser_version': '32.0', 'os': 'OS X', 'os_version': 'Lion', 'resolution': '1024x768'}
        self.start()

    def testFireFox(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = {'browser': 'Firefox', 'browser_version': '26.0', 'os': 'OS X', 'os_version': 'Lion', 'resolution': '1024x768'}
        self.start()

    def testIE8(self):
        WebTestCase.wait_seconds = 40
        WebTestCase.desired_cap = {'browser': 'IE', 'browser_version': '8.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
        self.start()

    def testIE10(self):
        WebTestCase.wait_seconds = 40
        WebTestCase.desired_cap = {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
        self.start()

    def testSafari(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = {'browser': 'Safari', 'browser_version': '7.0', 'os': 'OS X', 'os_version': 'Mavericks', 'resolution': '1024x768'}
        self.start()

    def testAndroid(self):
        WebTestCase.wait_seconds = 60
        WebTestCase.desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S III'}
        self.start()

    def testiPhone(self):
        WebTestCase.wait_seconds = 20
        WebTestCase.desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        self.start()
