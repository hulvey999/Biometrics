import face_recognition
import cv2
import os

# Load stored face encoding from file
if os.path.exists('biometric_data/face_encoding.txt'):
    with open('biometric_data/face_encoding.txt', 'r') as file:
        stored_face_encoding = list(map(float, file.read().split(',')))

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(frame)
    
    # Draw rectangles around detected faces
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # If faces are found, compare with stored encoding
    if face_locations:
        # Get the face encoding of the first face in the frame
        live_face_encoding = face_recognition.face_encodings(frame)[0]
        
        # Compare with stored face encoding
        match_result = face_recognition.compare_faces([stored_face_encoding], live_face_encoding)
        
        if match_result[0]:
            cv2.putText(frame, "Verified", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print("Face verified!")
        else:
            cv2.putText(frame, "Verification Failed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print("Verification failed.")

    # Display the resulting frame
    cv2.imshow('Verification - Press "q" to Quit', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
