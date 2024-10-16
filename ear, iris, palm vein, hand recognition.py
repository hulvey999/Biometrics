import cv2
import numpy as np
import os

# Ensure biometric data directory exists
if not os.path.exists('biometric_data'):
    os.makedirs('biometric_data')

def save_data(filename, data):
    np.savetxt(f'biometric_data/{filename}.txt', data, fmt='%f')
    print(f"{filename.capitalize()} biometric data saved.")

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame for the user to choose what to capture
    cv2.imshow('Capture Mode: Press e for Ear, i for Iris, p for Palm Vein, h for Hand', frame)

    key = cv2.waitKey(1) & 0xFF

    # Capture and store ear data
    if key == ord('e'):
        # Here we would normally apply an ear detection algorithm
        # For simplicity, we just crop the left half of the image as ear region
        ear_region = gray[:, :gray.shape[1] // 2]  # Assuming ear is on the left side
        save_data('ear', ear_region)
        print("Ear data captured.")

    # Capture and store iris data
    elif key == ord('i'):
        # Normally you'd apply eye/iris detection, here we mock it by cropping eye region
        eye_region = gray[gray.shape[0] // 4:gray.shape[0] // 2, gray.shape[1] // 4:3 * gray.shape[1] // 4]
        save_data('iris', eye_region)
        print("Iris data captured.")

    # Capture and store palm vein data
    elif key == ord('p'):
        # Apply basic thresholding to enhance palm veins
        _, palm_vein = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
        save_data('palm_vein', palm_vein)
        print("Palm vein data captured.")

    # Capture and store hand data
    elif key == ord('h'):
        # Detect hand contour (simplistic approach using threshold)
        _, hand_mask = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(hand_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            hand_contour = cv2.drawContours(np.zeros_like(frame), [largest_contour], -1, (255, 255, 255), 2)
            save_data('hand', hand_contour)
            print("Hand data captured.")

    # Break the loop on 'q' key press
    elif key == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
