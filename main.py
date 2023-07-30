from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

try:

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')

    # Wait for the user to scan the QR code and load the WhatsApp web page
    input('Please scan the QR code and press Enter to continue...')

    # Read the phone numbers from the Excel sheet
    try:
        contacts_df = pd.read_excel('contacts.xlsx', usecols=['PhoneNumber'])
        contacts = list(contacts_df['PhoneNumber'])
    except Exception as e:
        print("An error occurred while reading the phone numbers from the Excel sheet:", e)
        driver.quit()
        exit()

    message = "Test message"

    # Loop through the contacts and send the message
    for contact in contacts:
        url = "https://web.whatsapp.com/send?phone=" + str(contact) + "&text="  # + message + "&app_absent=1"

        # Load Whatsapp Web page
        driver.get(url)
        # Wait for the page be loaded
        time.sleep(10)
        enter_action = ActionChains(driver)
        time.sleep(2)
        enter_action.send_keys(Keys.ENTER)
        time.sleep(2)
        enter_action.perform()
        message_box = driver.find_element(By.XPATH, "(//div[@contenteditable='true'])[2]")
        try:
            message_lines = message.split("\n")
            for line in message_lines:
                message_box.send_keys(line)
                ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                    Keys.ENTER).perform()
            message_box.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"An error occurred while sending the message to {contact}:", e)
        time.sleep(2)
        # message_box.send_keys(Keys.ENTER)
        # time.sleep(2)

    # Close the browser window
    driver.quit()
except Exception as e:
    print(f"Error occurred while running the script: {e}")
