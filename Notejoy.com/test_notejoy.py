# Test of NoteJoy for login, make a new note and then delete it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging

logging.basicConfig(filename="test.log", filemode="w", level=logging.INFO)

# Initialize WebDriver for Chrome
driver = webdriver.Chrome()

USERNAME = ""
PASSWORD = ""
NOTE_TITLE = "This is test note"
NOTE_TEXT = "This is an automated test Note. #Selenium"

try:
    # Open the authentication page
    driver.get("https://notejoy.com/login")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "site")))
    wait = WebDriverWait(driver, 10)

    # Enter Username/email
    email_field = driver.find_element(By.ID, "login-email")
    email_field.send_keys(USERNAME)
    
    time.sleep(2)

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys(PASSWORD)
    
    time.sleep(2)

    driver.find_element(By.NAME, "action").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-actions-menu")))

    print("Logged into Notejoy successfully!")
    logging.info("Logged into Notejoy successfully!")
    
    time.sleep(2)

    new_note_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add Note')]")))
    new_note_button.click()

    note_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Untitled']")))
    note_title.send_keys(NOTE_TITLE)

    note_body = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    note_body.send_keys(NOTE_TEXT)

    note = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{NOTE_TITLE}')]")))
    note.click()

    print("Note was created successfully!")
    logging.info("Note was created successfully!")

    #Right click on Note
    actions = ActionChains(driver)
    actions.context_click(note).perform()

    delete_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Delete')]")))
    delete_option.click()

    time.sleep(2)

    print("Note was deleted successfully!")
    print("All tests are passed!")
    logging.info("Note was deleted successfully!")
    logging.info("All tests are passed!")
        
except Exception as e:
    print("Test failed:", e)
    
finally:
    # Close the browser
    driver.quit()