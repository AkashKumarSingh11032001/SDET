from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\akash\\OneDrive\\Desktop\\Code\\SDET\\chromeDriver\\chromedriver.exe")

driver.get("https://www.youtube.com")

driver.maximize_window()

print(driver.title)