from page.webpage import WebPage, sleep
from utils.logger import log
from common.readelement import Element
from common.readconfig import ini
from common.customerlogin import CustomerLogin

from selenium import webdriver

frontflightinsurancesetting = Element('web', 'web_frontflightinsurancesettings')

drivers = webdriver.Chrome()
CustomerLogin(drivers).customer_login()
WebPage(drivers).js_click(frontflightinsurancesetting["商旅管理"])
WebPage(drivers).js_click(frontflightinsurancesetting["出差设置"])
WebPage(drivers).js_click(frontflightinsurancesetting["差旅政策"])
WebPage(drivers).js_click(frontflightinsurancesetting["预订设置"])
WebPage(drivers).js_click(frontflightinsurancesetting["国内机票"])
log.info("判断保险是否开启了")
insurance_attr_class = WebPage(drivers).find_element(frontflightinsurancesetting["自愿购买保险开关"]).get_attribute("class")
if insurance_attr_class == "ant-switch":
    # return False
    WebPage(drivers).js_click(frontflightinsurancesetting["自愿购买保险开关"])
    WebPage(drivers).js_click(frontflightinsurancesetting["保险类型"])
    WebPage(drivers).js_click(frontflightinsurancesetting["具体保险"])
    WebPage(drivers).js_click(frontflightinsurancesetting["确定"])
    WebPage(drivers).js_click(frontflightinsurancesetting["默认购买"])
    WebPage(drivers).js_click(frontflightinsurancesetting["是"])

else:
    # return True
    WebPage(drivers).js_click(frontflightinsurancesetting["保险类型"])
    WebPage(drivers).js_click(frontflightinsurancesetting["具体保险"])
    WebPage(drivers).js_click(frontflightinsurancesetting["确定"])
    WebPage(drivers).js_click(frontflightinsurancesetting["默认购买"])
    WebPage(drivers).js_click(frontflightinsurancesetting["是"])


WebPage(drivers).js_click(frontflightinsurancesetting["保存"])
drivers.quit()
