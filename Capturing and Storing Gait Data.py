import cv2

# Initialize camera
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('biometric_data/gait_data.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('Capturing Gait Data', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop when 'q' is pressed
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
