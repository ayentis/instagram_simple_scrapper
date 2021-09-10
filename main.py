from selenium import webdriver
from PIL import Image
import time
import sys


def press_button_with_text(driver, text):
    buttons = driver.find_elements_by_css_selector('Button')
    for button in buttons:
        if button.text == text:
            button.click()
            return True
    return False


def instagram_simple_scrapper(usr_login, usr_password):
    # using try to get exception if it happens
    try:
        # set timeout
        timeout = 5

        # connect firefox driver
        driver = webdriver.Firefox(executable_path='geckodriver')

        # load instagram page
        driver.get("https://www.instagram.com/")

        # waiting when page loads
        time.sleep(timeout)

        # searching username input field on the page
        username = driver.find_element_by_css_selector("input[name='username']")
        # searching password input field on the page
        password = driver.find_element_by_css_selector("input[name='password']")

        # cleaning fields
        username.clear()
        password.clear()

        # "input" username
        username.send_keys(usr_login)
        # "input" password
        password.send_keys(usr_password)

        # searching and pressing "submit" button
        login = driver.find_element_by_css_selector("button[type='submit']").click()

        # waiting when page check login and password and will load
        time.sleep(5)

        # if popup message "Save login info" appears press Not Now button
        if press_button_with_text(driver, 'Not Now'):
            # waiting when page will updated if Button was pressed
            time.sleep(5)

        # if popup message "send notification" appears press Not Now button
        if press_button_with_text(driver, 'Not Now'):
            # waiting when page will updated if Button was pressed
            time.sleep(5)

        # making screenshort
        driver.save_screenshot("screenshort.png")

        # open screenshot
        screenshot = Image.open('screenshort.png')
        screenshot.show()
    except Exception as e:
        # printing error
        print(e)
    finally:
        # closing driver
        driver.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough parameters. Expected <login> <password>")
    else:
        instagram_simple_scrapper(sys.argv[1], sys.argv[2])
