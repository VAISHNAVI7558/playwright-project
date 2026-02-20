import re
from playwright.sync_api import expect


def test_google_search(page):
    page.wait_for_timeout(5000) # wait for 5 seconds to ensure the page is fully loaded
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout = 5000)
    except:
        print("No Popup to accept")
        page.get_by_role("combobox", name="Search").fill("Playwright Python")
        page.keyboard.press("Enter")
        expect(page.get_by_text("Playwright")).to_be_visible()



