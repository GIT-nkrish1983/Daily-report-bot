import pyautogui
import time
from datetime import datetime
import pyscreeze
##from openpyxl import Workbook, load_workbook

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

print ("W1 D3 Assignment 1 - Python AutoGUI")
print ("Prepare Daily status report for the day")


# Open Chrome
pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Open NIFTY 50
pyautogui.hotkey("ctrl", "l")
pyautogui.write(
    "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE"
)
pyautogui.press("enter")

time.sleep(5)

# Move the mouse to the NIFTY 50 price
# YOU NEED TO ADJUST THESE COORDINATES
pyautogui.moveTo(382, 258)

# Double-click the price
pyautogui.doubleClick()

time.sleep(1)

# Copy selected price
pyautogui.hotkey("ctrl", "c")

print("Price copied!")

# Get current date and time
now = datetime.now()

date_value = now.strftime("%d-%m-%Y")
time_value = now.strftime("%H:%M:%S")

# ---------------------------------------
# Open Excel
# ---------------------------------------

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("excel")
pyautogui.press("enter")

time.sleep(5)

# ---------------------------------------
# Create a new workbook
# ---------------------------------------

pyautogui.hotkey("ctrl", "n")
time.sleep(2)

# ---------------------------------------
# Enter column headings
# ---------------------------------------

pyautogui.write("Date")
pyautogui.press("tab")

pyautogui.write("Time")
pyautogui.press("tab")

pyautogui.write("Stock Name")
pyautogui.press("tab")

pyautogui.write("Stock Price")

# Move to next row
pyautogui.press("home")
pyautogui.press("down")

# ---------------------------------------
# Enter Date
# ---------------------------------------

pyautogui.write(date_value)
pyautogui.press("tab")

# ---------------------------------------
# Enter Time
# ---------------------------------------

pyautogui.write(time_value)
pyautogui.press("tab")

# ---------------------------------------
# Enter Stock Name
# ---------------------------------------

pyautogui.write("NIFTY 50")
pyautogui.press("tab")

# ---------------------------------------
# Paste copied stock price
# ---------------------------------------

pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

time.sleep(2)

print("NIFTY 50 data entered into Excel!")
timestamp = now.strftime("%Y%m%d_%H%M%S")

# --------------------------------------- # Take screenshot of Excel # --------------------------------------- 
time.sleep(2) 
# Take screenshot of the entire screen 
excel_screenshot = pyautogui.screenshot() 
# Save screenshot in the same folder as this Python program 
screenshot_name = f"Excel_SS_{timestamp}.png" 
excel_screenshot.save(screenshot_name) 
print("Excel screenshot saved as:") 
print(screenshot_name)

# ---------------------------------------
# Save Excel file with timestamp
# ---------------------------------------
time.sleep(2) 
filename = f"Daily report for stock tracking_{timestamp}.xlsx"

pyautogui.hotkey("ctrl", "s")

time.sleep(3)

pyautogui.write(filename)


# --------------------------------------- # Take screenshot of Excel saved # --------------------------------------- 
time.sleep(2) 
# Take screenshot of the entire screen 
excel_screenshot = pyautogui.screenshot() 
# Save screenshot in the same folder as this Python program 
screenshot_name = f"Daily_report_{timestamp}.png" 
excel_screenshot.save(screenshot_name) 
print("Excel screenshot saved as:") 
print(screenshot_name)
#-----------------------------
pyautogui.press("enter")

time.sleep(4)

print("Excel file saved as:")
print(filename)
