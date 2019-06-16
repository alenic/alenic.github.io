---
layout: post
title:  "Capture webcam with opencv"
subtitle: ""
date:   2019-06-16 00:00:00 -0600
categories: snippets
imgpath: ""
keywords: "opencv, webcam, capture, python"
code_folder: /assets/code/capture-webcam
---

OpenCV is a simple and nice library for image processing and computer vision.


This simple code is a start point for experiments with your webcam, infact it captures the webcam's frames and simply show it continuously on a window. If you press the 'q' key it will exit from the main while cycle.

{% highlight python %}
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

{% endhighlight %}

You can download the code from: [capture-webcam.py]({{page.code_folder}}/capture-webcam.py)