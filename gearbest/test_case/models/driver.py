from selenium import webdriver


class Browser(object):

    @staticmethod
    def firefox():
        return webdriver.Firefox()

    @staticmethod
    def chrome():
        return webdriver.Chrome()


if __name__ == "__main__":
    dr = Browser.firefox()
    dr.get("https://www.gearbest.com")
