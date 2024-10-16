import face_recognition
import cv2
import os

# Create directory for storing biometric data if it doesn't exist
if not os.path.exists('biometric_data'):
    os.makedirs('biometric_data')

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(frame)

    # Draw rectangles around faces
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Capturing Biometric Data - Press "c" to Capture', frame)

    # If 'c' is pressed, capture and store the face encoding
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Only save when at least one face is detected
        if face_locations:
            # Extract face encoding
            face_encoding = face_recognition.face_encodings(frame)[0]
            
            # Save encoding to a file
            with open(f'biometric_data/face_encoding.txt', 'w') as file:
                file.write(','.join([str(val) for val in face_encoding]))
            
            print("Biometric data captured and stored.")
        else:
            print("No face detected.")

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
