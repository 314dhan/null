# import pyautogui
# import time
#
# # Contoh fungsi untuk menekan tombol Windows + 2
# def open_second_taskbar_app():
#     pyautogui.hotkey('win', '2')  # Tekan Windows + 2 untuk membuka aplikasi kedua di taskbar
#
# # Contoh fungsi untuk mengetik URL dan menekan Enter
# def type_youtube_url_and_enter():
#     url = "https://www.youtube.com/watch?v=R3qsEquoRn0&ab_channel=WindahBasudara"
#     pyautogui.typewrite(url)  # Ketik URL
#     pyautogui.press('enter')  # Tekan Enter
#     pyautogui.hotkey('ctrl', 't')
#     url = "https://www.youtube.com/watch?v=R3qsEquoRn0&ab_channel=WindahBasudara"
#     pyautogui.typewrite(url)  # Ketik URL
#     pyautogui.press('enter')  # Tekan Enter
#
# open_second_taskbar_app()
# a = range(10)
# for i in a:
#     type_youtube_url_and_enter()
#     if(a == 5):
#         break

import os
os.system('shutdown /s /t 1')