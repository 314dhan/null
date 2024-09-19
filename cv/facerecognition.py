import cv2
import numpy as np

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

while True:
    # Baca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame secara horizontal
    frame = cv2.flip(frame, 1)

    # Ambil region of interest (ROI) untuk tangan
    roi = frame[100:300, 100:300]

    # Konversi ke citra grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Gaussian blur untuk mengurangi noise
    gray_blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Thresholding untuk menemukan kontur tangan
    _, thresh = cv2.threshold(gray_blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Temukan kontur tangan
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Cari kontur terbesar (tangan)
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)

        # Tentukan convex hull
        hull = cv2.convexHull(contour)

        # Gambar kontur tangan dan convex hull
        cv2.drawContours(roi, [contour], -1, (255, 0, 0), 2)
        cv2.drawContours(roi, [hull], -1, (0, 255, 0), 2)

        # Temukan titik ekstrem atas, bawah, kiri, dan kanan
        ext_top = tuple(hull[hull[:, :, 1].argmin()][0])
        ext_bottom = tuple(hull[hull[:, :, 1].argmax()][0])
        ext_left = tuple(hull[hull[:, :, 0].argmin()][0])
        ext_right = tuple(hull[hull[:, :, 0].argmax()][0])

        # Tampilkan arah gerakan tangan
        cv2.circle(roi, ext_top, 5, (0, 0, 255), -1)
        cv2.circle(roi, ext_bottom, 5, (0, 0, 255), -1)
        cv2.circle(roi, ext_left, 5, (0, 0, 255), -1)
        cv2.circle(roi, ext_right, 5, (0, 0, 255), -1)

        # Tentukan arah gerakan berdasarkan posisi titik ekstrem
        if ext_top[1] < ext_bottom[1]:
            cv2.putText(frame, 'UP', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif ext_top[1] > ext_bottom[1]:
            cv2.putText(frame, 'DOWN', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if ext_left[0] < ext_right[0]:
            cv2.putText(frame, 'LEFT', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif ext_left[0] > ext_right[0]:
            cv2.putText(frame, 'RIGHT', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Hand Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
