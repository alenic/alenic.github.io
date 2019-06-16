import cv2

webcam_id = 0
capture = cv2.VideoCapture(webcam_id)
# You can set custom resolution if your webcam can support it, otherwise the method capture.read() fails
# (comment the following 4 lines of code if you want to use the default webcam resolution)
webcam_res_width = 640
webcam_res_height = 480
capture.set(3, webcam_res_width)
capture.set(4, webcam_res_height)

while True:
  ret, frame = capture.read()
  if ret:
    # process the frame
    # ...
    # show the frame
    cv2.imshow('original frame', frame)
    # wait millis_delay milliseconds for a pressed key (if millis_delay <= 0 waits a key events indefinitely)
    millis_delay = 1
    key_pressed = cv2.waitKey(millis_delay)
    # break the while cycle if the key q is pressed
    if key_pressed == ord('q'):
      break

# Safetly close the video capture and imshow windows
capture.release()
cv2.destroyAllWindows()