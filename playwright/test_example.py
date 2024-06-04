# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2024/6/3 23:09

import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.baidu.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("百度一下，你就知道"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
