import cv2
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# Open the camera with OpenCV
cap1 = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap1.isOpened():
    print("Could not open camera")
    exit()

# Initialize GStreamer
Gst.init(None)

# Create GStreamer pipeline for the camera
pipeline1 = Gst.parse_launch("ksvideosrc device-index=0 ! videoconvert ! appsink")

# Create OpenCV VideoCapture object with the GStreamer pipeline
# This line is commented out as we are using the cap1 object created earlier
# cap1 = cv2.VideoCapture(pipeline1.get_property('name'), cv2.CAP_GSTREAMER)

while True:
    # Capture frame-by-frame from the camera
    ret1, frame1 = cap1.read()

    if ret1:
        # Display the resulting frame from the camera
        cv2.imshow('Camera 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the VideoCapture object
cap1.release()

# Close all the windows
cv2.destroyAllWindows()