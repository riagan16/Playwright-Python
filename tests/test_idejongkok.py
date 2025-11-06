from playwright.sync_api import expect
import allure
from pages.login import Login
from pages.home import Home, Add_Product

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
    add = Add_Product(setup)
    
    login.input_email('testemail1@example.com')
    login.input_password('testpassword')
    login.click_login()
    
    add.click_add_button()
    add.input_product_name()
    add.input_product_price()
    add.input_product_stock()
    add.select_product_category()
    add.input_product_desc()
    add.click_submit()
    add.validate_add()
    
        
        # #Add Product
        # with allure.step("Click Add Product button"):
        #     #setup.locator("button", has_text="Add Product").click()
        #     setup.locator("//span[text()='Add Product']/parent::button").click()
        # with allure.step("Input product name"):
        #     setup.locator('//input[@type="text"]').fill("Xiaomi 1234")
        # with allure.step("Input price"):
        #     setup.locator("(//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[1]").fill("99999")
        # with allure.step("Input stock"):
        #     #setup.locator("//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").fill("5")
        #     setup.locator("(//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[2]").fill("5")
        #     #setup.locator("input[type='number']").nth(1).fill("5")
        # with allure.step("Select category"):
        #     #setup.locator("//select[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").select_option("Electronics")
        #     setup.locator("(//select[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[1]").select_option("Electronics")
        #     #setup.locator("select").select_option("Electronics")
        # with allure.step("Input description"):
        #     setup.locator("//textarea[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").fill("ini contoh deskripsi")
        #     # setup.locator("textarea").fill("ini contoh deskripsi")
        # with allure.step("Submit new product"):
        #     setup.locator("//button[@type='submit']").click()
        # with allure.step("New product validation"):
        #     locator_new_add = setup.locator("(//tr[@class='hover:bg-gray-50 transition-colors'])[1]/descendant::div[2]")
        #     expect(locator_new_add).to_have_text('Xiaomi 1234')
 

# def test_edit_product(setup):
    
#         #Sign in
#         with allure.step("Input email"):
#             setup.locator("//input[@id='email']").fill('testemail1@example.com')
#         with allure.step("Input password"):
#             setup.locator("//input[@id='password']").fill('testpassword')
#         with allure.step("Click login button"):
#             setup.locator("//span[text()='Sign In']/parent::button").click()
            
#         #Edit
#         with allure.step("Click Edit button"):
#             setup.locator("(//button[@title='Edit'])[1]").click()
#         with allure.step("Edit product name"):
#             setup.locator("//input[@type='text' and @value='Xiaomi 1234']").fill("New Product Name")
#         with allure.step("Edit price"):
#             setup.locator("//input[@type='number' and @value='99999']").fill("1000")
#         with allure.step("Edit stock"):
#             setup.locator("//input[@type='number' and @value='5']").fill("100")
#         with allure.step("Edit Category"):
#             setup.locator("select").select_option("Audio")
#         with allure.step("Submit edit data"):    
#             setup.locator("//button[@type='submit']").click()
#         with allure.step("Validation edit data"):
#             locator_new_add = setup.locator("(//tr[@class='hover:bg-gray-50 transition-colors'])[1]/descendant::div[2]")
#             expect(locator_new_add).to_have_text('New Product Name')
    
# def test_delete_product(setup):
    
#         #Sign in
#         with allure.step("Input email"):
#             setup.locator("//input[@id='email']").fill('testemail1@example.com')
#         with allure.step("Input password"):
#             setup.locator("//input[@id='password']").fill('testpassword')
#         with allure.step("Click login button"):
#             setup.locator("//span[text()='Sign In']/parent::button").click()
        
#         #Delete    
#         with allure.step("Click Delete button"):
#             setup.locator("(//button[@title='Delete'])[1]").click()
#         with allure.step("Delete confirmation popup"):
#             setup.locator("//button[@class='flex-1 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors']").click()
#         with allure.step("Validation delete data"):
#             locator_new_add = setup.locator("(//tr[@class='hover:bg-gray-50 transition-colors'])[1]/descendant::div[2]")
#             expect(locator_new_add).not_to_have_text('New Product Name')

# def test_signout(setup):
    
#     #Sign in
#         with allure.step("Input email"):
#             setup.locator("//input[@id='email']").fill('testemail1@example.com')
#         with allure.step("Input password"):
#             setup.locator("//input[@id='password']").fill('testpassword')
#         with allure.step("Click login button"):
#             setup.locator("//span[text()='Sign In']/parent::button").click()
    
#     #signout
#         with allure.step("Sign out"):
#             setup.locator("//span[text()='Sign Out']/parent::button").click()
#         with allure.step("Validate sign out"):
#             expect(setup.locator("(//h2[@class='text-2xl font-bold text-white text-center'])")).to_have_text('Welcome Back!')
    
#     # input("Press Enter to close the browser...")
    
    
    
    
    
    
    
    
    
    