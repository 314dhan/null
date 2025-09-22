# import pyautogui
# import time
#
# def type_text_and_press_enter():
#     # Arahkan kursor ke koordinat (-994, 977)
#     # Loop untuk mengetik "halo" dan tekan enter sebanyak 40 kali
#     while True:
#         pyautogui.moveTo(57, 647, duration=1)
#         pyautogui.click(57, 647)
#         time.sleep(306)
#
# # Panggil fungsi untuk menjalankan proses
# type_text_and_press_enter()

import os

for i in range(400):
    d = str(i) + ' days ago'
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system(f'git commit --date="{d}" -m "Commit from {d}"')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600"
#git fetch origin master
#git rebase origin/master

# def get_cursor_resolution():
#     while True:
#         # Mendapatkan resolusi layar
#         screen_width, screen_height = pyautogui.size()
#
#         # Mendapatkan posisi kursor saat ini
#         cursor_x, cursor_y = pyautogui.position()
#
#         # Menampilkan hasil
#         print("Resolusi layar:", screen_width, "x", screen_height)
#         print("Koordinat kursor saat ini:", cursor_x, ",", cursor_y)
#
#         # Tunggu sebentar sebelum mengambil posisi kursor berikutnya
#         time.sleep(0.1)
#
# # Panggil fungsi untuk memulai loop mendapatkan koordinat resolusi kursor
# get_cursor_resolution()
