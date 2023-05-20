#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: weChat.py
@时间: 2023/05/15 08:32:49
@说明: 
"""

import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
# 配置appium数据
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "vivo X50",
    "automationName": "UiAutomator2",
    "noReset": "true",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI"
}
# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 使用隐式等待或者显示等待，尽量减少time.sleep强制等待的使用提高脚本执行速度
driver.implicitly_wait(5)

try:
    driver.find_element(
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.tencent.mm:id/btg")'
    ).click()

    time.sleep(1)

    content = driver.find_element(MobileBy.ID, "com.tencent.mm:id/b3s")
    print(content.get_attribute("content-desc"))

except Exception as error:
    raise error
finally:
    driver.close_app()
