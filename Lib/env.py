from playwright.sync_api import sync_playwright

# Lib/env 크롬 브라우저 런처

def lunch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # headless 여부
        return browser

def close_browser(browser): # browser 객체가 위에 외부로 있기 떄문에 close 내부 객체를 전달
    browser.close() # 전달된 브라우저 객체를 닫음