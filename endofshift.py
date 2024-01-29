from login import login_to_website, print_element_info
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver, wait = login_to_website()

try:
    # Wait for the status dropdown to be clickable
    status_dropdown = wait.until(
        EC.element_to_be_clickable((By.ID, "statusListCombo"))
    )
    print_element_info("Status dropdown", status_dropdown)

    # Wait for the overlay to disappear
    loading_overlay = wait.until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )

    # Click on the status dropdown after the overlay disappears
    status_dropdown.click()

    # Locate the "10. End of shift" option within the status dropdown
    end_of_shift_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='statusListCombo']/option[text()='10. End of shift']"))
    )
    print_element_info("End of Shift option", end_of_shift_option)

    # Click on the "10. End of shift" option
    end_of_shift_option.click()

    # Locate the "Submit" button
    submit_button = wait.until(
        EC.element_to_be_clickable((By.ID, "submitmanualStatusChange"))
    )
    print_element_info("Submit button", submit_button)

    # Click the "Submit" button
    submit_button.click()

    print("Successfully changed status to '10. End of shift'")

    # Wait for a few seconds to allow the page to update (you can adjust this time)
    driver.implicitly_wait(5)

except Exception as status_change_error:
    print(f"Error during status change: {status_change_error}")
    exit(1)

# Finally, close the browser
driver.quit()
