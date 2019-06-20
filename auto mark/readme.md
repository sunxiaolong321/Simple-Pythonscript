# auto mark|德州学院教务系统自动教师评价脚本

## Requests

* Chromedriver  
* pyquery
* selenium
* python3

脚本自动评分,分数设置为90到100之间，没有设置评语，最后需要自己提交，方便检查，万一出错就凉凉了。

## 说明
脚本写的非常粗糙，不过能跑，偶尔遇到不能跑的情况，重新运行就行了。
根据selenium官方网站的说法，用sleep()等待页面加载是非常stupid的行为。但是呢，自动评价嘛，跑完就行了。细节完善的话也没写。

### 显式等待  
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"myDynamicElement"))

### 隐式等待：
driver.implicitly_wait(10) # seconds


下载地址:  
* [ChromeDriver](http://chromedriver.storage.googleapis.com/index.html)  
* [Firefox](https://github.com/mozilla/geckodriver/releases/)   
* [IE](http://selenium-release.storage.googleapis.com/index.html)  
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
