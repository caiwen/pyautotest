from selenium import webdriver
import os
# 截图函数


def insert_img(driver, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('test_case')[0]
        file_path = base + "report/image/" + file_name
        driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.get("http://192.168.10.6/login")
        insert_img(driver, 'login.jpg')
        driver.quit()
