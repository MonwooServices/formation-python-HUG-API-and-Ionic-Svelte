# https://sixfeetup.com/blog/end-to-end-testing-python-playwright
import os
from playwright.sync_api import Playwright, sync_playwright, expect

# get URL through environment variable
URL = "http://127.0.0.1:8000"

def run(playwright: Playwright) -> None:
    #browser = playwright.chromium.launch(headless=True)
    #context = browser.new_context()
    # Open new page and go to our URL
    try:
      page = context.new_page().goto(URL)
      server_status="Server is up"
    except:
      server_status="Server is down"
    return server_status

    #expect(page).to_have_title("MediaCMS")

    # Find and click Register link
    #register_page = page.get_by_role("link", name="Register")
    #register_page.click()

    # Expects the URL to contain intro.
    #expect(page).to_have_url("https://demo.mediacms.io/accounts/signup/")


with sync_playwright() as playwright:
  result=run(playwright)

print(result)