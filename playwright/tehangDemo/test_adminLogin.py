import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright


def test_admin_login(page: Page):
    page.goto('https://dev-tehang-system-env-2.teyixing.com/login')
    page.get_by_placeholder('请输入手机号或邮箱').fill('8924')
    page.get_by_placeholder('请输入密码').fill('@12345678')
    page.locator('xpath=//button').click()
    locator = page.locator('xpath=//span[contains(text(),"朱秀君")]')
    expect(locator).to_contain_text('朱秀君')

