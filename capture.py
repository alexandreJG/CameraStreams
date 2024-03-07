import cv2
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# Initialize GStreamer
Gst.init(None)

# Create GStreamer pipelines for each camera
pipeline1 = Gst.parse_launch("v4l2src device=/dev/video0 ! videoconvert ! appsink")
pipeline2 = Gst.parse_launch("v4l2src device=/dev/video1 ! videoconvert ! appsink")

# Create OpenCV VideoCapture objects with the GStreamer pipelines
cap1 = cv2.VideoCapture(pipeline1.get_property('name'), cv2.CAP_GSTREAMER)
cap2 = cv2.VideoCapture(pipeline2.get_property('name'), cv2.CAP_GSTREAMER)

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