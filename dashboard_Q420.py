from selenium import webdriver
import pyautogui
import time

# variables
powerbi_url = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=871c010f-5e61-4fb1-83ac-98610a7e9110&response_type=code%20id_token&scope=openid%20profile%20offline_access&state=OpenIdConnect.AuthenticationProperties%3DIze4Jsv1scyLTYST3itPb_53njMXp15TIZbRyhKBzREENmV5_b8bOreNYA8OhTBYGb9mwAW71C8BCBVlQ4i7nGNtwIY3vhEY1xun-CnSkmOW7k33qtU7Txd-TwHM8nh0gIiV4fNpt-8QogZb9mdtdiCerfroQpqDCyAqwH5BrQQ5eUg-ATW7Sww7B-a27vwT&response_mode=form_post&nonce=637435327685683446.ZjlhYTlmMDktMTdjOC00OGY4LTk3MjMtOGIwY2FlYjI1NjFlMmZlYjk5YTAtMjI4Yy00MGQxLWExMDctZjUzM2U2M2E4Nzhj&site_id=500453&redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1%26pbi_source%3Dwebheadersignin&post_logout_redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1%26pbi_source%3Dwebheadersignin&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&nux=1&msafed=0&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0"
wh_username = '*********'
wh_password = '********'
hp_username = "*************"
hp_password = '*********'
sec = 0.05

# fail-safes
pyautogui.FAILSAFE = True

time.sleep(3)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(powerbi_url)
pyautogui.typewrite('marcos.trevino')
pyautogui.hotkey('altright','2')
pyautogui.typewrite('hp.com')
pyautogui.hotkey('enter')

time.sleep(5)
pyautogui.typewrite(wh_username, interval=sec)
pyautogui.hotkey('tab')
pyautogui.typewrite(wh_password, interval=sec)
pyautogui.hotkey('enter')

time.sleep(5)
pyautogui.hotkey('tab')
pyautogui.typewrite('marcos.trevino', interval=sec)
pyautogui.hotkey('altright','2')
pyautogui.typewrite('hp.com', interval=sec)
pyautogui.hotkey('tab')
pyautogui.typewrite(hp_password, interval=sec)
pyautogui.hotkey('enter')

time.sleep(5)
pyautogui.hotkey('enter')



time.sleep(5)
pyautogui.hotkey('ctrl','t')
pyautogui.typewrite('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
pyautogui.typewrite('marcostrevinordz', interval=sec)
pyautogui.hotkey('enter')
time.sleep(3)
pyautogui.typewrite('marcostrevinordz', interval=sec)
pyautogui.hotkey('altright','2')
pyautogui.typewrite('gmail.com', interval=sec)
pyautogui.hotkey('enter')

# Project end since Google Chrome doesn't allow an automation to access my account.'


