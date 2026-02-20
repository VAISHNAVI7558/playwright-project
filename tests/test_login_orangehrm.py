import re
from playwright.sync_api import Page
from pages.orangehrm_login_page import loginPage
from pages.orangehram_home_page import HomePage

def test_example(page: Page) -> None:
    login_page = loginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()


    page.wait_for_url("**/dashboard**", timeout=50000)
    home_page.click_performance()   
    home_page.click_dashboard()
