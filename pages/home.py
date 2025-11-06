from playwright.sync_api import expect
import allure
from locators.home import Loc, Modal


class Home:
    def __init__(self, driver):
        self.driver = driver
    def validate_signin(self):
        with allure.step("Sign in validation"):
            expect(self.driver.locator(Loc.titleHeader)).to_be_visible()
            expect(self.driver.locator(Loc.titleHeader)).to_have_text("Ide Jongkok's Scraping Lab")
            expect(self.driver.locator(Loc.email)).to_contain_text('testemail1@example.com')

class Add_Product:
    def __init__(self, driver):
        self.driver = driver
        
    def click_add_button(self):
        with allure.step("Click Add Product button"):
            self.driver.locator(Modal.addButton).click()
    def input_product_name(self):
        with allure.step("Input product name"):
            self.driver.locator(Modal.productName).fill("Xiaomi 1234")
    def input_product_price(self):
        with allure.step("Input price"):
            self.driver.locator(Modal.productPrice).fill("99999")
    def input_product_stock(self):
        with allure.step("Input stock"):
            #setup.locator("//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").fill("5")
            self.driver.locator(Modal.productStock).fill("5")
            #setup.locator("input[type='number']").nth(1).fill("5")
    def select_product_category(self):
        with allure.step("Select category"):
            #setup.locator("//select[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").select_option("Electronics")
            self.driver.locator(Modal.productCategory).select_option("Electronics")
            #setup.locator("select").select_option("Electronics")
    def input_product_desc(self):
        with allure.step("Input description"):
            self.driver.locator(Modal.productDescription).fill("ini contoh deskripsi")
            # setup.locator("textarea").fill("ini contoh deskripsi")
    def click_submit(self):  
        with allure.step("Submit new product"):
            self.driver.locator(Modal.submitButton).click()
    def validate_add(self):
        with allure.step("New product validation"):
            locator_new_add = self.driver.locator(Modal.validationSubmit)
            expect(locator_new_add).to_have_text('Xiaomi 1234')