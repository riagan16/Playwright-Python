from playwright.sync_api import expect
import allure
from pages.login import Login
from pages.home import Home, AddProductModal, EditProductModal, DeleteProduct, Logout

@allure.title("Login")
@allure.description("Login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(setup):
    login = Login(setup)
    home = Home(setup)
    
    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login()
    home.validate_signin()
 
@allure.title("Add Product")
@allure.description("Add with valid data")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_product(setup):
    
    login = Login(setup)
    add = AddProductModal(setup)
    
    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login()
    
    add.click_add_button()
    add.input_product_name('Xiaomi 1234')
    add.input_product_price('99999')
    add.input_product_stock('10')
    add.select_product_category('Electronics')
    add.input_product_desc('ini contoh deskripsi"')
    add.click_submit()
    add.validate_add('Xiaomi 1234')
    
 
@allure.title("Edit Product")
@allure.description("Edit with valid data")
@allure.severity(allure.severity_level.BLOCKER)
def test_edit_product(setup):
    
    login = Login(setup)
    edit = EditProductModal(setup)
    
    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login()
    
    edit.click_edit_button()
    edit.edit_product_name('Test Edit Name')
    edit.edit_product_price('1000.99')
    edit.edit_product_stock('5')
    edit.edit_product_category('Computers')
    edit.edit_product_desc('Test Edit Desc')
    edit.click_submit()
    edit.validate_edit('Test Edit Name')
    
@allure.title("Delete Product")
@allure.description("Delete with valid data")
@allure.severity(allure.severity_level.BLOCKER)
def test_delete_product(setup):
    
    login = Login(setup)
    delete = DeleteProduct(setup)
    
    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login()    

    delete.click_delete()
    delete.click_confirm_delete()
    delete.validate_delete('Test Edit Name')

@allure.title("Logout")
@allure.description("Successful logout")
@allure.severity(allure.severity_level.BLOCKER)
def test_logout(setup):
    
    login = Login(setup)
    logout = Logout(setup)  

    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login() 
    
    logout.click_logout()
    logout.validate_logout('Welcome Back!')
  
 # input("Press Enter to close the browser...")
    
    
    
    
    
    
    
    