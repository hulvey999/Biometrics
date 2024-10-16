import cv2

# Load stored signature
stored_signature = cv2.imread('biometric_data/signature.png', cv2.IMREAD_GRAYSCALE)

# Capture live signature
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Show your signature to verify', frame)

        if cv2.waitKey(1) & 0xFF == ord('v'):  # Press 'v' to verify
            live_signature = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if stored_signature.shape == live_signature.shape:
                difference = cv2.absdiff(stored_signature, live_signature)
                if cv2.countNonZero(difference) < 1000:
                    print("Signature verified successfully.")
                else:
                    print("Signature verification failed.")
            break

cap.release()
cv2.destroyAllWindows()
