from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False ) 
   context = browser.new_context()
   page = context.new_page()
   
   page.goto("https://practicetestautomation.com/practice-test-login/")
   page.get_by_label("Username").fill("student")
   page.get_by_label("Password").fill("Password123")
   page.get_by_role("button", name="Submit").click()
   page.get_by_role("heading", name="Logged In Successfully").wait_for()
   
   text_element = page.get_by_label("Username").input_value()
   print(text_element)
   time.sleep(5)
   browser.close()