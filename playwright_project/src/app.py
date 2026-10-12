from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, channel = 'chrome')

    page = browser.new_page()

    #page.goto('https://varzesh3.com')

    #page.goto('https://divar.ir')
    page.goto('https://aphacademy.ir/')
    
    # page.get_by_role("link", name="اهواز").click()
    # page.get_by_role("button", name=" دیوار من").click()
    # page.get_by_role("button", name=" ورود به حساب کاربری").click()
    # page.get_by_placeholder("۰۹۱۲ ۱۲۳ ۴۵۶۷").fill('09398226275')
    # page.get_by_role("textbox", name="۰۹۳۹ ۸۲۲ ۶۲۷۵").fill('09398226275')
    # page.get_by_role("button", name="بعدی").click()

    page.pause()