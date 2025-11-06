from playwright.sync_api import expect
import allure
from locators.home import Loc, Modal



class Home:
    def __init__(self, driver):
        self.driver = driver
    def validate_signup(self, titleHeader, email):
        with allure.step("Sign up validation"):
            expect(self.driver.locator(Loc.titleHeader)).to_be_visible()
            expect(self.driver.locator(Loc.titleHeader)).to_have_text(titleHeader)
            expect(self.driver.locator(Loc.email)).to_contain_text(email)
    def validate_signin(self, titleHeader, email):
        with allure.step("Sign in validation"):
            expect(self.driver.locator(Loc.titleHeader)).to_be_visible()
            expect(self.driver.locator(Loc.titleHeader)).to_have_text(titleHeader)
            expect(self.driver.locator(Loc.email)).to_contain_text(email)

class AddProductModal:
    def __init__(self, driver):
        self.driver = driver
        
    def click_add_button(self):
        with allure.step("Click Add Product button"):
            self.driver.locator(Modal.addButton).click()
    def input_product_name(self, pdtName):
        with allure.step("Input product name"):
            self.driver.locator(Modal.productName).fill(pdtName)
    def input_product_price(self, pdtPrice):
        with allure.step("Input price"):
            self.driver.locator(Modal.productPrice).fill(pdtPrice)
    def input_product_stock(self, pdtStock):
        with allure.step("Input stock"):
            self.driver.locator(Modal.productStock).fill(pdtStock)
    def select_product_category(self, pdtCate):
        with allure.step("Select category"):
            self.driver.locator(Modal.productCategory).select_option(pdtCate)
    def input_product_desc(self, pdtDesc):
        with allure.step("Input description"):
            self.driver.locator(Modal.productDescription).fill(pdtDesc)
    def click_submit(self):  
        with allure.step("Submit new product"):
            self.driver.locator(Modal.submitButton).click()
    def validate_add(self, pdtName):
        with allure.step("New product validation"):
            locator_new_add = self.driver.locator(Modal.validationSubmit)
            expect(locator_new_add).to_have_text(pdtName)
     
class EditProductModal():       
    def __init__(self, driver):
        self.driver = driver
        
    def click_edit_button(self):
        with allure.step("Click Edit button"):
            self.driver.locator(Modal.editButton).click()
    def edit_product_name(self, pdtName):
        with allure.step("Edit product name"):
            self.driver.locator(Modal.productName).fill(pdtName)
    def edit_product_price(self, pdtPrice):
        with allure.step("Edit price"):
            self.driver.locator(Modal.productPrice).fill(pdtPrice)
    def edit_product_stock(self, pdtStock):
        with allure.step("Edit stock"):
            self.driver.locator(Modal.productStock).fill(pdtStock)
    def edit_product_category(self, pdtCate):
        with allure.step("Edit Category"):
            self.driver.locator(Modal.productCategory).select_option(pdtCate)
    def edit_product_desc(self, pdtDesc):
        with allure.step("Edit description"):
            self.driver.locator(Modal.productDescription).fill(pdtDesc)
    def click_submit(self):
        with allure.step("Submit edit data"):    
            self.driver.locator(Modal.submitButton).click()
    def validate_edit(self, pdtName):
        with allure.step("Validation edit data"):
            locator_new_add = self.driver.locator(Modal.validationSubmit)
            expect(locator_new_add).to_have_text(pdtName)

class DeleteProduct:
    def __init__(self, driver):
        self.driver = driver
          
    def click_delete(self):   
        with allure.step("Click Delete button"):
            self.driver.locator(Loc.delete).click()
    def click_confirm_delete(self):  
        with allure.step("Delete confirmation popup"):
            self.driver.locator(Loc.deleteConfirm).click()
    def validate_delete(self, pdtName):  
        with allure.step("Validation delete data"):
            locator_new_add = self.driver.locator(Loc.validateDelete)
            expect(locator_new_add).not_to_have_text(pdtName)

class Logout:
    def __init__(self, driver):
        self.driver = driver
        
    def click_logout(self):
        with allure.step("Log out"):
            self.driver.locator(Loc.logout).click()
    def validate_logout(self, validateLogout):
        with allure.step("Validate log out"):
            expect(self.driver.locator(Loc.validateLogout)).to_have_text(validateLogout)