from playwright.sync_api import sync_playwright, expect
from time import sleep
import pytest


@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto('https://testapp.idejongkok.com/')
        
        yield page
        
        page.close()