from selenium import webdriver
from random import randint
from pyquery import PyQuery
import time


def parse_html(html):
    data = PyQuery(html)  # 解析界面资源，获取源码
    items = data('tbody tr').items()  # 通过pyquery的筛选查找规则获取自己想要爬取的标签
    # data_list = []  # 用来存储目标数据的列表
    for item in items:  # 遍历标签，提取想要的内容
        yield item.attr('data-kch_id')
    # print(data_list)


def pingfen():
    elements1 = driver.find_elements_by_xpath("//input[@type='text']")
    for grade in elements1:
        grade.clear()
        grade.send_keys(randint(89, 100))
    # element8 = driver.find_element_by_xpath('')
    driver.find_element_by_xpath("//input[@data-dyf='0']").click()
    # element7.click()
    driver.find_element_by_id('btn_xspj_bc').click()
    time.sleep(2)
    allhandles = driver.window_handles
    driver.switch_to.window(allhandles[1])
    time.sleep(2)
    driver.find_element_by_id("btn_ok").click()
    time.sleep(2)
    # print(alert.text)
    # alert.accept()


driver = webdriver.Chrome()
driver.get(
    'http://211.64.32.195/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t=1560961556524')
driver.find_element_by_id('yhm').send_keys('学号')
driver.find_element_by_id('mm').send_keys('密码')
driver.find_element_by_id('dl').click()
driver.find_element_by_link_text('教学评价').click()
# driver.switch_to_frame('_blank')
driver.find_element_by_link_text('学生评价').click()
handle = driver.window_handles
driver.switch_to.window(handle[1])
time.sleep(6)
driver.find_element_by_id('btn_yd').click()
time.sleep(5)
# print(driver.current_url)
pingfen()
parse_html(driver.page_source)
for page in parse_html(driver.page_source):
    if page != None:
        print(page)
        driver.find_element_by_xpath("//tr[@data-kch_id='%s']"%page).click()
        time.sleep(5)
        pingfen()
time.sleep(60)
