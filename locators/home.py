class Loc:
    titleHeader = "//h1[@class='text-xl font-semibold text-gray-900']"
    email = "//span[@class='text-sm text-gray-600']"
    
class Modal:
    addButton = "//span[text()='Add Product']/parent::button"
    productName = "//input[@type='text']"
    productPrice = "(//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[1]"
    productStock = "(//input[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[2]"
    productCategory = "(//select[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500'])[1]"
    productDescription = "//textarea[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']"
    submitButton = "//button[@type='submit']"
    validationSubmit = "(//tr[@class='hover:bg-gray-50 transition-colors'])[1]/descendant::div[2]"
    