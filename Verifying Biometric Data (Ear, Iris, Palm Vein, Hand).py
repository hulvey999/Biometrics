import cv2
import numpy as np
import os

# Load stored data function
def load_data(filename):
    if os.path.exists(f'biometric_data/{filename}.txt'):
        return np.loadtxt(f'biometric_data/{filename}.txt')
    else:
        print(f"No stored {filename} data found.")
        return None

# Compare two images using MSE (Mean Squared Error)
def compare_images(imageA, imageB):
    if imageA.shape != imageB.shape:
        return False
    mse = np.mean((imageA - imageB) ** 2)
    return mse < 1000  # Tolerance for image differences

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame for the user to verify
    cv2.imshow('Verification Mode: Press e for Ear, i for Iris, p for Palm Vein, h for Hand', frame)

    key = cv2.waitKey(1) & 0xFF

    # Verify ear data
    if key == ord('e'):
        ear_data = load_data('ear')
        if ear_data is not None:
            live_ear_region = gray[:, :gray.shape[1] // 2]
            if compare_images(ear_data, live_ear_region):
                print("Ear verified!")
            else:
                print("Ear verification failed.")

    # Verify iris data
    elif key == ord('i'):
        iris_data = load_data('iris')
        if iris_data is not None:
            live_iris_region = gray[gray.shape[0] // 4:gray.shape[0] // 2, gray.shape[1] // 4:3 * gray.shape[1] // 4]
            if compare_images(iris_data, live_iris_region):
                print("Iris verified!")
            else:
                print("Iris verification failed.")

    # Verify palm vein data
    elif key == ord('p'):
        palm_vein_data = load_data('palm_vein')
        if palm_vein_data is not None:
            _, live_palm_vein = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
            if compare_images(palm_vein_data, live_palm_vein):
                print("Palm vein verified!")
            else:
                print("Palm vein verification failed.")

    # Verify hand data
    elif key == ord('h'):
        hand_data = load_data('hand')
        if hand_data is not None:
            _, live_hand_mask = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(live_hand_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                live_hand_contour = cv2.drawContours(np.zeros_like(frame), [largest_contour], -1, (255, 255, 255), 2)
                if compare_images(hand_data, live_hand_contour):
                    print("Hand verified!")
                else:
                    print("Hand verification failed.")

    # Break the loop on 'q' key press
    elif key == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
