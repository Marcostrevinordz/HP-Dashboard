import pyautogui
import time

# fail-safes
pyautogui.FAILSAFE = True

pyautogui.moveTo(99, 747, 1, pyautogui.easeInQuad)
pyautogui.click()

# OK
time.sleep(20)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.typewrite('Octubre2020')
pyautogui.hotkey('tab')
pyautogui.typewrite('Octubre2020')
pyautogui.hotkey('enter')





# time.sleep(5)
# print(pyautogui.position())