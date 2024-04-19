from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://google.com")
    print(page.title())
    page.screenshot(path="exampluuue.png")
    browser.close()

