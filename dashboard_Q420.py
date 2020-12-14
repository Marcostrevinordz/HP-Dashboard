from selenium import webdriver
import pyautogui

start_url = "https://app.powerbi.com/groups/me/reports/77c5ab02-86c5-436a-bd21-c3b4e6f3bc04/ReportSection0e3419147caa07737936"
wh_username = 'mtrevino'
wh_password = 'Webhelp2021'
hp_username = 'marcos.trevino@hp.com'
hp_password = 'Octubre2020'

driver = webdriver.Chrome()
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()