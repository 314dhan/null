import pyautogui
import keyboard
import time

def start_clicking():
    while not keyboard.is_pressed('s'):
        pyautogui.click()
        # time.sleep(0.1)  # Jeda antara klik, bisa diatur sesuai kebutuhan

# Membuka aplikasi menggunakan Windows + 8
keyboard.press_and_release('win+8')

# Mulai clicker ketika tombol 't' ditekan
keyboard.add_hotkey('t', start_clicking)

# Menunggu tombol 's' untuk menghentikan program
print("Tekan 't' untuk mulai, dan 's' untuk berhenti.")
keyboard.wait('s')
