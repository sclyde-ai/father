import keyboard
import webbrowser

# open chatgbt
def open_chatgpt():
    chatgpt_url = "https://www.chatgpt.com/"
    webbrowser.open(chatgpt_url)
# Replace the desired key combination
keyboard.add_hotkey("ctrl+alt+c+g", open_chatgpt)

# open google_keep
def open_google_keep():
    google_keep_url = "https://www.google_keep.com/"
    webbrowser.open(google_keep_url)
# Replace the desired key combination
keyboard.add_hotkey("ctrl+alt+g+k", open_google_keep)

# Keep the script running
keyboard.wait("esc")
