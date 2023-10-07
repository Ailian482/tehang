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

    def judge_back_self_give_insurance(self):
        """判断是否开启了自主赠险模式"""
        log.info("判断是否开启了自主赠险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["自主预订赠险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_self_regular_insurance(self):
        """判断是否开启了自主固定购险模式"""
        log.info("判断是否开启了自主固定购险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["自主预订固定购险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_admin_give_insurance(self):
        """判断是否开启了代订赠险模式"""
        log.info("判断是否开启了代订赠险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["后台代订赠险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def judge_back_admin_regular_insurance(self):
        """判断是否开启了代订固定购险模式"""
        log.info("判断是否开启了代订固定购险模式")
        insurance_attr = self.find_element(backflightinsurancesetting["后台代订固定购险"]).get_attribute("class")
        if insurance_attr == "ant-checkbox":
            # 未开启，返回 False
            return False
        return True

    def cancel_back_insurance(self):
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

    def check_back_self_free_insurance(self):
        """勾选国内机票自主赠险模式"""
        log.info("勾选国内机票自主赠险模式")
        if self.judge_back_self_give_insurance():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["自主预订赠险"])

    def check_back_self_regular_insurance(self):
        """勾选国内机票自主固定购险模式"""
        log.info("勾选国内机票自主固定购险模式")
        if self.judge_back_self_regular_insurance():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["自主预订固定购险"])

    def check_back_admin_free_insurance(self):
        """勾选国内机票代订赠险模式"""
        log.info("勾选国内机票代订赠险模式")
        if self.judge_back_admin_give_insurance():
            # 如果已勾选，则无需做任何操作
            pass
        else:
            # 如果未勾选，则勾选复选框
            self.js_click(backflightinsurancesetting["后台代订赠险"])

    def check_back_admin_regular_insurance(self):
        """勾选国内机票代订固定购险模式"""
        log.info("勾选国内机票代订固定购险模式")
        if self.judge_back_admin_regular_insurance():
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

    def save_back_flight_setting(self):
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

    def judge_front_insurance(self):
        """判断自愿购险是否开启"""
        log.info("判断自愿购险是否开启")
        insurance_attr_class = self.find_element(frontflightinsurancesetting["自愿购买保险开关"]).get_attribute("class")
        if insurance_attr_class == "ant-switch":
            # 如果未开启，则返回 False
            return False
        return True

    def check_front_insurance(self):
        """打开自愿购险开关"""
        log.info("打开自愿购险开关")
        if self.judge_front_insurance():
            # 如果已开启自愿购险，则无需操作
            pass
        else:
            # 如果未开启自愿购险，则打开自愿购险开关
            self.js_click(frontflightinsurancesetting["自愿购买保险开关"])

    def cancel_front_insurance(self):
        """取消勾选自愿购险"""
        log.info("取消勾选自愿购险")
        if self.judge_front_insurance():
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

    def save_front_flight_setting(self):
        """点击前台国内机票配置保存按钮"""
        log.info("点击前台国内机票配置保存按钮")
        self.js_click(frontflightinsurancesetting["保存"])

    def close_back_flight_insurance(self):
        """关闭机构后台的国内机票保险配置"""
        log.info("关闭机构后台的国内机票保险配置")
        self.to_back_flight_setting()
        self.cancel_back_insurance()
        self.save_back_flight_setting()

    def open_back_self_free_insurance(self):
        """仅开启机构后台的国内机票自主赠险模式"""
        log.info("仅开启机构后台的国内机票自主赠险模式")
        self.to_back_flight_setting()
        self.check_back_self_free_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_self_regular_insurance(self):
        """仅开启机构后台的国内机票自主固定购险模式"""
        log.info("仅开启机构后台的国内机票自主固定购险模式")
        self.to_back_flight_setting()
        self.check_back_self_regular_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_admin_free_insurance(self):
        """仅开启机构后台的国内机票代订赠险模式"""
        log.info("仅开启机构后台的国内机票代订赠险模式")
        self.to_back_flight_setting()
        self.check_back_admin_free_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_admin_regular_insurance(self):
        """仅开启机构后台的国内机票代订固定购险模式"""
        log.info("仅开启机构后台的国内机票代订固定购险模式")
        self.to_back_flight_setting()
        self.check_back_admin_regular_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_self_admin_regular_insurance(self):
        """开启机构后台的国内机票自主和代订固定购险模式"""
        log.info("开启机构后台的国内机票自主和代订固定购险模式")
        self.to_back_flight_setting()
        self.check_back_self_free_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.check_back_admin_free_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_self_free_admin_regular_insurance(self):
        """开启机构后台的国内机票自主赠险和代订固定购险模式"""
        log.info("开启机构后台的国内机票自主赠险和代订固定购险模式")
        self.to_back_flight_setting()
        self.check_back_self_free_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.check_back_admin_regular_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_self_regular_admin_free_insurance(self):
        """开启机构后台的国内机票自主固定购险和代订赠险模式"""
        log.info("开启机构后台的国内机票自主和代订固定购险模式")
        self.to_back_flight_setting()
        self.check_back_self_regular_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.check_back_admin_free_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def open_back_self_admin_free_insurance(self):
        """开启机构后台的国内机票自主和代订赠险模式"""
        log.info("开启机构后台的国内机票自主和代订赠险模式")
        self.to_back_flight_setting()
        self.check_back_self_regular_insurance()
        self.click_self_insurance()
        self.select_back_flight_insurance()
        self.check_back_admin_regular_insurance()
        self.click_admin_insurance()
        self.select_back_flight_insurance()
        self.save_back_flight_setting()

    def close_front_flight_insurance(self):
        """关闭机构前台的国内机票保险配置"""
        log.info("关闭机构前台的国内机票保险配置")
        self.to_front_flight_setting()
        self.cancel_front_insurance()
        self.save_front_flight_setting()

    def open_front_flight_insurance_default_buy(self):
        """开启机构前台的国内机票保险配置-默认购买"""
        log.info("开启机构前台的国内机票保险配置-默认购买")
        self.to_front_flight_setting()
        self.check_front_insurance()
        self.select_front_flight_insurance()
        self.default_buy_insurance()
        self.save_front_flight_setting()

    def open_front_flight_insurance_default_not_buy(self):
        """开启机构前台的国内机票保险配置-默认不购买"""
        log.info("开启机构前台的国内机票保险配置-默认不购买")
        self.to_front_flight_setting()
        self.check_front_insurance()
        self.select_front_flight_insurance()
        self.default_not_buy_insurance()
        self.save_front_flight_setting()


if __name__ == "__main__":
    CustomerLogin(drivers).customer_login()
    FlightInsuranceSettingPage(drivers).close_front_flight_insurance()
    AdminLogin(drivers).admin_login()
    FlightInsuranceSettingPage(drivers).close_back_flight_insurance()
    FlightInsuranceSettingPage(drivers).open_back_self_free_admin_regular_insurance()
    drivers.quit()
