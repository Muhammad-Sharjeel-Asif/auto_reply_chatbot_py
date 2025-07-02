import pyautogui
import pyperclip
import time
from client import agent
from client import is_last_message_from_friend
from functions import get_last_line

pyautogui.click(647, 754)
time.sleep(1)

# Step 1: Wait before starting
print("You have 3 seconds to focus the window with text...")
time.sleep(3)

while True:
    chat_history = ""

    coordinate_pairs = [
    ((510, 200), (520, 640)),
    ((505, 195), (525, 645)),
    ((519, 187), (527, 631)),
    ((512, 163), (527, 631)),
]

    for start, end in coordinate_pairs:
        # STEP 2: Triple click at start point to select first message ===
        pyautogui.moveTo(start[0], start[1], duration=0.2)
        pyautogui.click(clicks=3, interval=0.25)    

        # STEP 3: Drag to end point
        pyautogui.mouseDown()
        pyautogui.moveTo(end[0], end[1], duration=1)
        pyautogui.mouseUp()

        # Step 3: Copy using Ctrl + C
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')

        # Step 4: Read copied text
        time.sleep(0.5)
        chat_history = pyperclip.paste()
        print("Copied text:\n", chat_history)

        if chat_history != "":
            break



    if is_last_message_from_friend(chat_history, "MUHAMMAD SHARJEEL ASIF"):
        # Agent responds
        response = agent(chat_history)
        print(response)

        # Copying agent's response
        pyperclip.copy(response)
        time.sleep(0.5)

        # Step 5: Focus WhatsApp input box and paste reply
        print("Pasting agent's reply to WhatsApp...")
        pyautogui.click(772, 687)  # Adjust this to WhatsApp input box coordinates
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        # Step 6: Press escape
        pyautogui.press('esc')

        # Step 7: Press Enter to send
        pyautogui.press('enter')

    last_line = get_last_line(chat_history)

    if "bye" in last_line.lower() and "MUHAMMAD SHARJEEL ASIF" not in last_line:
        print("Friend said bye. Ending conversation.")
        break


# Optional Step 5: Wait and then paste elsewhere
# print("Pasting in 2 seconds. Place your cursor where you want the text.")
# time.sleep(2)


# pyautogui.moveTo(619, 691, duration=0.5)
# pyautogui.hotkey('ctrl', 'v')