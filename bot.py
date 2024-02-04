import pyautogui
import time

def get_cursor_resolution():
    while True:
        # Mendapatkan resolusi layar
        screen_width, screen_height = pyautogui.size()

        # Mendapatkan posisi kursor saat ini
        cursor_x, cursor_y = pyautogui.position()

        # Menampilkan hasil
        print("Resolusi layar:", screen_width, "x", screen_height)
        print("Koordinat kursor saat ini:", cursor_x, ",", cursor_y)

        # Tunggu sebentar sebelum mengambil posisi kursor berikutnya
        time.sleep(0.1)

# Panggil fungsi untuk memulai loop mendapatkan koordinat resolusi kursor
get_cursor_resolution()
