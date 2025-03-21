from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# 设置Appium的Desired Capabilities
DESIRED_CAPS = {
    'platformName': 'Mac',  # 平台名称
    'automationName': 'Mac2',  # 自动化引擎
    'appPackage': '/Applications/QQMusic.app',  # 替换为你的应用程序路径
    'newCommandTimeout': 6000,  # 新命令超时时间
    'unicodeKeyboard': True,  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
    'noReset': True,  # true:不重新安装APP，false:重新安装app
}

# 启动Appium会话
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', DESIRED_CAPS)
driver.implicitly_wait(20)

try:
    # 等待应用程序启动
    time.sleep(5)

    # 查找并点击某个UI元素
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'YourElementAccessibilityID')  # 替换为你的元素Accessibility ID
    element.click()

    # 输入文本
    text_field = driver.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')  # 替换为你的文本框类名
    text_field.send_keys('Hello, macOS!')

    # 截图保存
    driver.save_screenshot('screenshot.png')

    # 打印页面源码
    print(driver.page_source)

finally:
    # 关闭会话
    driver.quit()