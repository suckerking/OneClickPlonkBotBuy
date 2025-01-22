import pyperclip
import keyboard
import time

def send_clipboard_to_telegram_chat():
    #Pastes clipboard content into the active Telegram chat and presses Enter.
    clipboard_content = pyperclip.paste()
  
    # Ensure clipboard content is not empty
    if clipboard_content:  
        print(f"Pasting clipboard content: {clipboard_content}")
        keyboard.write(clipboard_content)  # Type clipboard content into the chat
        time.sleep(0.5)  # Small delay to ensure content is pasted
        keyboard.press_and_release('enter')  # Simulate pressing Enter key
        print("Message sent!")
    else:
        print("Clipboard is empty. Nothing sent.")

# Bind the function to the "1" key press
keyboard.add_hotkey('1', send_clipboard_to_telegram_chat)

# Keep the script running (press 'esc' to stop it)
print("Press '1' to paste clipboard content into Telegram chat and send it. Press 'esc' to exit.")
keyboard.wait('esc')
