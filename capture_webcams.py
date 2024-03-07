import cv2

# Create VideoCapture objects for each camera
cap1 = cv2.VideoCapture(0)  # Default camera
cap2 = cv2.VideoCapture(1)  # Additional camera

while True:
    # Capture frame-by-frame from each camera
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if ret1:
        # Display the resulting frame from camera 1
        cv2.imshow('Camera 1', frame1)

    if ret2:
        # Display the resulting frame from camera 2
        cv2.imshow('Camera 2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the VideoCapture objects
cap1.release()
cap2.release()

# Close all the windows
cv2.destroyAllWindows()