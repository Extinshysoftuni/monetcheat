import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_website():
    company = os.environ.get("COMPANY")
    username = os.environ.get("USERNAMEMONET")
    password = os.environ.get("PASSWORD")

    if company is None or username is None or password is None:
        print("Please set the COMPANY, USERNAMEMONET, and PASSWORD environment variables.")
        exit(1)

    driver = webdriver.Firefox()
    driver.get("https://www.monetwfo-eu.com/Monet5/login/login.aspx")
    wait = WebDriverWait(driver, 20)

    try:
        company_field = wait.until(EC.element_to_be_clickable((By.ID, "txtTenantId")))
        print_element_info("Company field", company_field)

        username_field = wait.until(EC.element_to_be_clickable((By.ID, "txtUserName")))
        print_element_info("Username field", username_field)

        password_field = wait.until(EC.element_to_be_clickable((By.ID, "txtPassword")))
        print_element_info("Password field", password_field)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit")))
        print_element_info("Login button", login_button)

    except Exception as e:
        print(f"Error during element location: {e}")
        exit(1)

    try:
        company_field.send_keys(company)
        username_field.send_keys(username)
        login_button.click()
        driver.implicitly_wait(5)

    except NameError as ne:
        print(f"Error: {ne}, please check the element location")
        exit(1)

    try:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "i0116")))
        print_element_info("Email field", email_field)

        email_field.send_keys(username)

        next_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        print_element_info("Next button", next_button)

        next_button.click()
        driver.implicitly_wait(5)

    except Exception as e:
        print(f"Error during Microsoft login: {e}")
        exit(1)

    try:
        password_field_ms = wait.until(EC.element_to_be_clickable((By.ID, "i0118")))
        print_element_info("Password field (Microsoft)", password_field_ms)

        password_field_ms.send_keys(password)

        sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        print_element_info("Sign in button", sign_in_button)

        sign_in_button.click()
        driver.implicitly_wait(5)

    except Exception as e:
        print(f"Error during Microsoft password entry and sign-in: {e}")
        exit(1)

    try:
        yes_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        print_element_info("Yes button", yes_button)

        yes_button.click()
        driver.implicitly_wait(5)

    except Exception as e:
        print(f"Error during confirmation page: {e}")
        exit(1)

    return driver, wait

def print_element_info(element_name, element):
    print(f"{element_name} found - tag name: {element.tag_name}, id: {element.get_attribute('id')}")

# Add more functions if needed

if __name__ == "__main__":
    login_to_website()
