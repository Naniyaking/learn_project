from selenium import webdriver


from selenium.webdriver import ActionChains


def open_url_by_chrome():
   #去掉chrome 自动化控制提示和打印错误日志

   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])#
   set_driver = webdriver.Chrome(options=chrome_options,service_log_path=os.devnull)
   return set_driver
