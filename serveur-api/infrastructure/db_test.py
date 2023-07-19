# https://sixfeetup.com/blog/end-to-end-testing-python-playwright
import os
from playwright.sync_api import Playwright, sync_playwright, expect

# get URL through environment variable
URL = os.environ.get("URL")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page and go to our URL
    page = context.new_page()
    page.goto(URL)
    expect(page).to_have_title("MediaCMS")

    # Find and click Register link
    register_page = page.get_by_role("link", name="Register")
    register_page.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url("https://demo.mediacms.io/accounts/signup/")


with sync_playwright() as playwright:
  run(playwright)