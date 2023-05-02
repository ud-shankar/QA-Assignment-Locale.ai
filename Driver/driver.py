from selenium import webdriver


browser = 'chrome'
if browser == 'chrome':
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()

elif browser == 'edge':
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    driver.maximize_window()

elif browser == "firefox":
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    