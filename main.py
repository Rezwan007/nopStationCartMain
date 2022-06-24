import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

desired_cap= {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:app": "D:\\BS-23\\nopstationCart_4.40.apk"

}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

#Scenario: 01 Customer add products in his shopping cart
print(" Start of scenario 1")

# first I have click on the close page
driver.implicitly_wait(20)
read = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnAccept')
read.click()

# Click on the menu
driver.implicitly_wait(5)
menu = driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='NopStation Cart']")
menu.click()

# click on the electronic + (sub menu)
driver.implicitly_wait(5)
electronics = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='Placeholder'])[5]")
electronics.click()

# Scroll to nokia lumia 1020
time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=687, y=2009).move_to(x=712, y=663).perform().release()

time.sleep(10)
driver.implicitly_wait(15)
touch1 = TouchAction(driver)
touch1.press(x=704, y=2148).move_to(x=716, y=757).perform().release()

time.sleep(10)
driver.implicitly_wait(15)
touch2 = TouchAction(driver)
touch2.press(x=708, y=2140).move_to(x=728, y=1096).perform().release()

time.sleep(10)
driver.implicitly_wait(15)
touch2 = TouchAction(driver)
touch2.press(x=708, y=2140).move_to(x=728, y=1296).perform().release()
time.sleep(5)

# multiAction = MultiAction(driver)
# multiAction.add(touch, touch1, touch2)
# multiAction.perform()

# for i in range(4):
#     time.sleep(5)
#     driver.implicitly_wait(15)
#     touch = TouchAction(driver)
#     touch.press(x=703, y=2005).move_to(x=703, y=52).perform().release()

# print all the avilable product under cellphone
driver.implicitly_wait(5)
nokiaLumia1020 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='Placeholder'])[3]")
nokiaLumia1020.click()

# scrolldown to quantity
time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=733, y=1777).move_to(x=707, y=527).release().perform()

# click plus button to add 2 quantity in the cart
driver.implicitly_wait(5)
plusButton = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnPlus')
plusButton.click()

# print the quantity to ensure
driver.implicitly_wait(5)
qty = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/tvQuantity')
print(qty.text)

# find click to add in the cart
driver.implicitly_wait(5)
addToCart = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart')
addToCart.click()

# # Toast message
# toast = driver.find_element_by_id("//div[@id='toast-container']//*")
# print(toast.text)

# find of Scenario: 01 Customer add products in his shopping cart

print("Nokia Lumia 1020 successfully added to cart..... ")
driver.implicitly_wait(1)
print("---------------------------------------------------")
driver.implicitly_wait(1)
print("End of scenario 1")
print("---------------------------------------------------")
driver.implicitly_wait(1)
print("Start of scenario 2")

# Scenario: 02 Customer successfully place order as a guest user

# Click on the top cart button
driver.implicitly_wait(5)
cart = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/menu_cart')
cart.click()

# Click on the checkout button
driver.implicitly_wait(5)
checkOut = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut')
checkOut.click()

# Continue as a guest button
driver.implicitly_wait(5)
guestBtn = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout')
guestBtn.click()

# Customer detail
# First Name
driver.implicitly_wait(5)
firstName = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etFirstName')
firstName.click()
firstName.send_keys("HASAN-E-")
driver.back()

# Last name
driver.implicitly_wait(5)
lastName = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etLastName')
lastName.click()
lastName.send_keys("REZWAN")
driver.back()

# Email
driver.implicitly_wait(5)
emailAddress = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etEmail')
emailAddress.click()
emailAddress.send_keys("utsha124@gmail.com")
driver.back()

# Country drop-down
driver.implicitly_wait(5)
country = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/countrySpinner')
country.click()
countrySelect = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
countrySelect.click()
driver.back()

# company
driver.implicitly_wait(5)
company = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etCompanyName')
company.click()
company.send_keys("BS-23")
driver.back()

# scrolldown to city
time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=691, y=2127).move_to(x=745, y=495).release().perform()
time.sleep(10)

# City
driver.implicitly_wait(5)
city = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etCity')
city.click()
city.send_keys("DHK")

# Street address
driver.implicitly_wait(5)
streetAddress = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress')
streetAddress.click()
streetAddress.send_keys("21/A main road")
driver.back()

# Zip code
driver.implicitly_wait(5)
zipCode = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/etZipCode')
zipCode.click()
zipCode.send_keys("5400")
driver.back()

# Continue button
driver.implicitly_wait(5)
continueBtn = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/btnContinue')
continueBtn.click()

# Next Day Air
driver.implicitly_wait(5)
nextDayAir = driver.find_element_by_class_name("android.widget.RelativeLayout[4]")
nextDayAir.click()

# scrolldown to continueBtn2
time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=728, y=2009).move_to(x=769, y=679).release().perform()
time.sleep(10)

# continueBtn after shipping
driver.implicitly_wait(5)
continueBtn2 = driver.find_element_by_class_name("android.widget.Button")
continueBtn2.click()

# scrolldown to continueBtn3
time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=704, y=2176).move_to(x=814, y=311).release().perform()
time.sleep(10)

time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=765, y=2148).move_to(x=777, y=295).release().perform()
time.sleep(10)

time.sleep(10)
driver.implicitly_wait(15)
touch = TouchAction(driver)
touch.press(x=740, y=2135).move_to(x=802, y=503).release().perform()
time.sleep(10)

# check / money order
driver.implicitly_wait(5)
checkOrMoneyOrder = driver.find_element_by_class_name("android.widget.RelativeLayout[2]")
checkOrMoneyOrder.click()

# continueBtn
driver.implicitly_wait(5)
continueBtn3 = driver.find_element_by_class_name("android.widget.Button")
continueBtn3.click()

# Next Button
driver.implicitly_wait(5)
nextBtn = driver.find_element_by_class_name("android.widget.Button")
nextBtn.click()

# confirm button
driver.implicitly_wait(5)
confirmBtn = driver.find_element_by_class_name("android.widget.Button")
confirmBtn.click()

# confirmation of order
driver.implicitly_wait(5)
confirmOrder = driver.find_element_by_id('com.nopstation.nopcommerce.nopstationcart:id/md_text_message')
print(confirmOrder.text)

# End of scenario 2
print("End of scenario 2")
print("-----------------------------")

