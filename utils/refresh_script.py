import keyboard
import time

init_sleep = 5
print(f"Script started. Sleeping 5 seconds before sending first ctrl-r")
print("\tPress Ctrl+C to stop the script.")

time.sleep(init_sleep)

try:
    while True:
        keyboard.send("ctrl+r")  # Sends the Ctrl+R hotkey (press and release)
        print(f"Sent Ctrl+R at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        time.sleep(14400)  # Wait 4 hours (4 * 60 * 60 = 14400 seconds)
except KeyboardInterrupt:
    print("\nScript stopped by user.")
