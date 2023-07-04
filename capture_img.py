import cv2


def capture_fruit():
    # Create a VideoCapture object to access the USB webcam
    # Use the appropriate camera index (0, 1, 2, etc.)
    camera = cv2.VideoCapture(1)

    # Check if the webcam is opened successfully
    if not camera.isOpened():
        print("Failed to open the webcam")
        exit()

    # Capture a frame from the webcam
    ret, frame = camera.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame from the webcam")
        camera.release()
        exit()

    # Save the captured frame to a file
    image_file = "fruit.jpg"
    cv2.imwrite(image_file, frame)

    # Release the webcam
    camera.release()


capture_fruit()
