import os
import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def save_video(output_vio_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_vio_frames[0].shape[1], output_vio_frames[0].shape[0]))
    for frame in output_vio_frames:
        out.write(frame)
    out.release()

def save_video2(frames, output_path):
    # Ensure the output directory exists
    dir_name = os.path.dirname(output_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    for frame in frames:
        out.write(frame)

    out.release()