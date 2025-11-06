from playwright.sync_api import expect
import allure
from locators.login import Loc

class Signup:
    def __init__(self, driver):
        self.driver = driver
        
    def click_signup_link(self):   
        with allure.step("Click signup link"):
            self.driver.locator(Loc.signupLink).click()   
    def input_email(self, email):
        with allure.step("Input email"):
            self.driver.locator(Loc.inputEmail).fill(email)
    def input_password(self, password):    
        with allure.step("Input password"):
            self.driver.locator(Loc.inputPassword).fill(password)
    def click_signup(self):   
        with allure.step("Click signup button"):
            self.driver.locator(Loc.signupButton).click()   
        
class Login:
    def __init__(self, driver):
        self.driver = driver
    def input_email(self, email):
        with allure.step("Input email"):
            self.driver.locator(Loc.inputEmail).fill(email)
    def input_password(self, password):    
        with allure.step("Input password"):
            self.driver.locator(Loc.inputPassword).fill(password)
    def click_login(self):   
        with allure.step("Click login button"):
            self.driver.locator(Loc.loginButton).click()
        