# import pyautogui
# import random
# import time

# # Disable PyAutoGUI Fail-Safe (NOT RECOMMENDED - see note below)
# pyautogui.FAILSAFE = False

# # Define movement distance (adjust as needed)
# movement_distance = 10

# # Set time intervals (in seconds)
# move_interval = 10            
# right_click_interval = 20

# # Define hotkeys for switching apps (modify as needed)
# switch_app_1_hotkey = 'alt', 'tab'  # Alt + Tab
# switch_app_2_hotkey = 'alt', 'shift', 'tab'  # Alt + Shift + Tab

# def move_mouse():
#   # Get screen dimensions
#   width, height = pyautogui.size()

#   # Define a margin from the edges (adjust as needed)
#   margin = 50

#   # Generate random coordinates within the adjusted boundaries
#   x = random.randint(margin, width - margin)
#   y = random.randint(margin, height - margin)

#   # Move the mouse with a slight delay
#   pyautogui.moveTo(x, y, duration=0.25)

# def right_click():
#   # Simulate right click
#   pyautogui.click(button='right')  # Specify button='right' for right click

# def switch_app(hotkey):
#   # Press the hotkey to switch applications
#   pyautogui.hotkey(*hotkey)  # Use unpacking for hotkey sequence

# last_move_time = time.time()  # Track time for movement
# last_right_click_time = time.time()  # Track time for right click
# last_app_switch_time = time.time()  # Track time for app switching (optional)

# while True:
#   current_time = time.time()

#   # Check for movement interval
#   if current_time - last_move_time >= move_interval:
#     move_mouse()
#     last_move_time = current_time

#   # Check for right click interval (ensure it happens at least every 20 seconds)
#   if current_time - last_right_click_time >= right_click_interval:
#     right_click()
#     last_right_click_time = current_time

#   # Switch app occasionally (adjust interval and hotkeys as needed)
#   if current_time - last_app_switch_time >= 30:  # Switch app every 30 seconds (optional)
#     # Alternate between hotkeys for different apps
#     if current_time % 60 < 30:  # Switch to app 1 in the first 30 seconds of each minute
#       switch_app(switch_app_1_hotkey)
#     else:
#       switch_app(switch_app_2_hotkey)
#     last_app_switch_time = current_time

#   # Short sleep to avoid busy waiting (adjust as needed)
#   time.sleep(0.1)

# # Press Ctrl-C to stop the program


import pyautogui
import random
import time

# Disable PyAutoGUI Fail-Safe (NOT RECOMMENDED - see note below)
pyautogui.FAILSAFE = False

# Define movement distance (adjust as needed)
movement_distance = 10

# Set time intervals (in seconds)
move_interval = 10
right_click_interval = 20
escape_click_interval = 21  # Click escape every 21 seconds

# Define hotkeys for switching apps (modify as needed)
switch_app_1_hotkey = 'ctrl', '1'  # Ctrl + 1

switch_app_2_hotkey = 'alt', 'shift', 'tab'  # Alt + Shift + Tab

def move_mouse():
  # Get screen dimensions
  width, height = pyautogui.size()

  # Define a margin from the edges (adjust as needed)
  margin = 50

  # Generate random coordinates within the adjusted boundaries
  x = random.randint(margin, width - margin)
  y = random.randint(margin, height - margin)

  # Move the mouse with a slight delay
  pyautogui.moveTo(x, y, duration=0.25)

def right_click():
  # Simulate right click
  pyautogui.click(button='right')  # Specify button='right' for right click

def switch_app(hotkey):
  # Press the hotkey to switch applications
  pyautogui.hotkey(*hotkey)  # Use unpacking for hotkey sequence

def click_escape():
  # Simulate escape key press
  pyautogui.press('esc')

last_move_time = time.time()  # Track time for movement
last_right_click_time = time.time()  # Track time for right click
last_app_switch_time = time.time()  # Track time for app switching (optional)
last_escape_click_time = time.time()  # Track time for escape click

while True:
  current_time = time.time()

  # Check for movement interval
  if current_time - last_move_time >= move_interval:
    move_mouse()
    last_move_time = current_time

  # Check for right click interval (ensure it happens at least every 20 seconds)
  if current_time - last_right_click_time >= right_click_interval:
    right_click()
    last_right_click_time = current_time

  # Check for escape click interval
  if current_time - last_escape_click_time >= escape_click_interval:
    click_escape()
    last_escape_click_time = current_time

  # Switch app occasionally (adjust interval and hotkeys as needed)
  if current_time - last_app_switch_time >= 30:  # Switch app every 30 seconds (optional)
    # Alternate between hotkeys for different apps
    if current_time % 60 < 30:  # Switch to app 1 in the first 30 seconds of each minute
      switch_app(switch_app_1_hotkey)
    else:
      switch_app(switch_app_2_hotkey)
    last_app_switch_time = current_time
 
  # Short sleep to avoid busy waiting (adjust as needed) nhmhng
  time.sleep(0.1)

# Press Ctrl-C to stop the program
1