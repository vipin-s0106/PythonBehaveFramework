from src.framework.WebDriverFactory import WebDriverFactory


driver = WebDriverFactory.get_driver()

driver.get("http://blazedemo.com/")

driver.quit()


