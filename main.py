import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h  = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0))
            if id == 1:
                screen_x = 1 * screen_w / frame_w * x
                screen_y = 2 * screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (0, 255, 255))
        print(left_eye[0].y - left_eye[1].y)
        if left_eye[0].y - left_eye[1].y < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eyes protection', frame)
    cv2.waitKey(1)