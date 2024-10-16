import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Write your signature on paper and show it to the camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):  # Press 'c' to capture
            cv2.imwrite('biometric_data/signature.png', frame)
            print("Signature captured and stored.")
            break

cap.release()
cv2.destroyAllWindows()
