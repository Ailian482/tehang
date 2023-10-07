from page.webpage import WebPage, sleep
from utils.logger import log
from common.readelement import Element
from common.readconfig import ini
from common.customerlogin import CustomerLogin
from common.adminlogin import AdminLogin

from selenium import webdriver

backflightinsurancesetting = Element('web', 'web_backflightinsurancesettings')
frontflightinsurancesetting = Element('web', 'web_frontflightinsurancesettings')

drivers = webdriver.Chrome()


class FlightInsuranceSettingPage(WebPage):
    """国内机票保险配置类"""

    def to_back_flight_setting(self):
        """进入后台机构国内机票配置页面"""
        log.info("进入后台机构国内机票配置页面")
        self.js_click(backflightinsurancesetting["运营管理"])
        self.js_click(backflightinsurancesetting["商旅事业部机构客户"])
        self.input_text(backflightinsurancesetting["客户名称"], "UI自动化测试")
        self.js_click(backflightinsurancesetting["查询"])
        self.is_click(backflightinsurancesetting["详情"])
        self.is_click(backflightinsurancesetting["国内机票"])

    def judge_back_self_give_insurance_setting(self):
        """判断是否开启了自主赠险模式"""
        log.info("判断是否开启了自主赠险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["自主预订赠险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_self_regular_insurance_setting(self):
        """判断是否开启了自主固定购险模式"""
        log.info("判断是否开启了自主固定购险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["自主预订固定购险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_admin_give_insurance_setting(self):
        """判断是否开启了代订赠险模式"""
        log.info("判断是否开启了代订赠险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["后台代订赠险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_admin_regular_insurance_setting(self):
        """判断是否开启了代订固定购险模式"""
        log.info("判断是否开启了代订固定购险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["后台代订固定购险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def cancel_back_insurance_setting(self):
        """取消勾选后台国内机票所有保险"""
        log.info("取消勾选后台国内机票所有保险")
        for i in range(1, 3):
            element_locator = backflightinsurancesetting["保险复选框"][1]
            for j in range(1, 3):
                new_element_locator = element_locator.replace("[n]", str([i]))
                new_element = new_element_locator.replace("[m]", str([j]))
                new_locator = ("xpath", new_element)
                attr_class = self.find_element(new_locator).get_attribute("class")
                if attr_class == "ant-checkbox":
                    continue
                else:
                    # 如果保险已勾选，则取消勾选
                    self.js_click(new_locator)

    def open_back_self_give_insurance_setting(self):
        """开启国内机票自主赠险模式"""
        log.info("开启国内机票自主赠险模式")
        if self.judge_back_self_give_insurance_setting():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["自主预订赠险"])

    def open_back_self_regular_insurance_setting(self):
        """开启国内机票自主固定购险模式"""
        log.info("开启国内机票自主固定购险模式")
        if self.judge_back_self_regular_insurance_setting():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["自主预订固定购险"])

    def open_flight_admin_give_insurance_setting(self):
        """开启国内机票代订赠险模式"""
        log.info("开启国内机票代订赠险模式")
        if self.judge_back_admin_give_insurance_setting():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["后台代订赠险"])

    def open_flight_admin_regular_insurance_setting(self):
        """开启国内机票代订固定购险模式"""
        log.info("开启国内机票代订固定购险模式")
        if self.judge_back_admin_regular_insurance_setting():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["后台代订固定购险"])

    def click_self_insurance(self):
        """点击自主预订选择保险"""
        log.info("点击自主预订选择保险")
        self.js_click(backflightinsurancesetting["选择自主预订保险"])

    def click_admin_insurance(self):
        """点击后台代订选择保险"""
        log.info("点击后台代订选择保险")
        self.js_click(backflightinsurancesetting["选择后台代订保险"])

    def select_back_flight_insurance(self):
        """选择后台具体保险"""
        log.info("选择后台具体保险")
        self.js_click(backflightinsurancesetting["选择具体保险"])
        self.js_click(backflightinsurancesetting["确定"])

    def save_flight_setting(self):
        """点击后台国内机票配置保存按钮"""
        log.info("点击后台国内机票配置保存按钮")
        self.js_click(backflightinsurancesetting["保存"])

    def to_front_flight_setting(self):
        """进入前台机构国内机票配置页面"""
        log.info("进入前台机构国内机票配置页面")
        self.js_click(frontflightinsurancesetting["商旅管理"])
        self.js_click(frontflightinsurancesetting["出差设置"])
        self.js_click(frontflightinsurancesetting["差旅政策"])
        self.js_click(frontflightinsurancesetting["预订设置"])
        self.js_click(frontflightinsurancesetting["国内机票"])

    def judge_front_insurance_setting(self):
        """判断自愿购险是否开启"""
        log.info("判断自愿购险是否开启")
        insurance_attr_class = WebPage(drivers).find_element(
            frontflightinsurancesetting["自愿购买保险开关"]).get_attribute("class")
        if insurance_attr_class == "ant-switch":
            return False
            # WebPage(drivers).js_click(frontflightinsurancesetting["自愿购买保险开关"])
        # else:
        #     return True
            # pass
        return True

    def open_front_insurance_setting(self):
        """打开自愿购险开关"""
        log.info("打开自愿购险开关")
        if self.judge_front_insurance_setting():
            # 如果已开启自愿购险，则无需操作
            pass
        else:
            # 如果未开启自愿购险，则打开自愿购险开关
            self.js_click(frontflightinsurancesetting["自愿购买保险开关"])

    def close_front_insurance_setting(self):
        """关闭自愿购险开关"""
        log.info("关闭自愿购险开关")
        if self.judge_front_insurance_setting():
            # 如果已开启自愿购险，则关闭自愿购险开关
            self.js_click(frontflightinsurancesetting["自愿购买保险开关"])
        else:
            # 如果未开启自愿购险，则无需操作
            pass

    def select_front_flight_insurance(self):
        """选择前台具体保险"""
        log.info("选择前台具体保险")
        self.js_click(frontflightinsurancesetting["保险类型"])
        self.js_click(frontflightinsurancesetting["具体保险"])
        self.js_click(frontflightinsurancesetting["确定"])

    def default_buy_insurance(self):
        """选择是默认购买保险"""
        log.info("选择是默认购买保险")
        self.js_click(frontflightinsurancesetting["默认购买"])
        self.js_click(frontflightinsurancesetting["是"])

    def default_not_buy_insurance(self):
        """选择否默认购买保险"""
        log.info("选择否默认购买保险")
        self.js_click(frontflightinsurancesetting["默认购买"])
        self.js_click(frontflightinsurancesetting["否"])



# # 检查后台保险配置
AdminLogin(drivers).admin_login()
WebPage(drivers).js_click(backflightinsurancesetting["运营管理"])
WebPage(drivers).js_click(backflightinsurancesetting["商旅事业部机构客户"])
WebPage(drivers).input_text(backflightinsurancesetting["客户名称"], "UI自动化测试")
WebPage(drivers).js_click(backflightinsurancesetting["查询"])
WebPage(drivers).is_click(backflightinsurancesetting["详情"])
WebPage(drivers).is_click(backflightinsurancesetting["国内机票"])

"""设置国内机票自主固定购险模式"""
element_locator = backflightinsurancesetting["保险复选框"][1]
new_element_locator = element_locator.replace("[n]", "[1]")
new_element = new_element_locator.replace("[m]", "[2]")
new_locator = ("xpath", new_element)
attr_class = WebPage(drivers).find_element(new_locator).get_attribute("class")
if attr_class == "ant-checkbox":
    # 如果保险未勾选，则勾选保险
    WebPage(drivers).js_click(new_locator)
else:
    pass
# for i in range(1, 3):
#     insurance_element_locator = backflightinsurancesetting["保险复选框"][1]
#     for j in range(1, 3):
#         new_insurance_element_locator = insurance_element_locator.replace("[n]", str([i]))
#         new_insurance_locator = new_insurance_element_locator.replace("[m]", str([j]))
#         new_insurance_element = ("xpath", new_insurance_locator)
#         insurance_attr_class = WebPage(drivers).find_element(new_insurance_element).get_attribute("class")
#         if insurance_attr_class == "ant-checkbox":
#             continue
#         else:
#             WebPage(drivers).js_click(new_insurance_element)
WebPage(drivers).js_click(backflightinsurancesetting["选择自主预订保险"])
WebPage(drivers).js_click(backflightinsurancesetting["选择具体保险"])
WebPage(drivers).js_click(backflightinsurancesetting["确定"])
WebPage(drivers).js_click(backflightinsurancesetting["保存"])

# CustomerLogin(drivers).customer_login()
# WebPage(drivers).js_click(frontflightinsurancesetting["商旅管理"])
# WebPage(drivers).js_click(frontflightinsurancesetting["出差设置"])
# WebPage(drivers).js_click(frontflightinsurancesetting["差旅政策"])
# WebPage(drivers).js_click(frontflightinsurancesetting["预订设置"])
# WebPage(drivers).js_click(frontflightinsurancesetting["国内机票"])
# # log.info("判断保险是否开启了")
# insurance_attr_class = WebPage(drivers).find_element(frontflightinsurancesetting["自愿购买保险开关"]).get_attribute("class")
# if insurance_attr_class == "ant-switch":
#     # return False
#     WebPage(drivers).js_click(frontflightinsurancesetting["自愿购买保险开关"])
#
# else:
#     pass
#     # return True
#
# WebPage(drivers).js_click(frontflightinsurancesetting["保险类型"])
# WebPage(drivers).js_click(frontflightinsurancesetting["具体保险"])
# WebPage(drivers).js_click(frontflightinsurancesetting["确定"])
# WebPage(drivers).js_click(frontflightinsurancesetting["默认购买"])
# WebPage(drivers).js_click(frontflightinsurancesetting["是"])
# WebPage(drivers).js_click(frontflightinsurancesetting["保存"])
drivers.quit()
