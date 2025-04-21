import pyautogui
import time

print("Move your mouse to the desired location. Press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')  # '\r' to overwrite the line in terminal
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped tracking.")
