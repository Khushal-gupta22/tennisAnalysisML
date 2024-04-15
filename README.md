# Tennis Analysis System

## Introduction

This ML project focuses on comprehensive analysis and tracking of tennis players and the ball during matches. It leverages state-of-the-art object detection techniques like YOLO (You Only Look Once) to accurately identify and localize players and the tennis ball in video footage. Additionally, it employs deep learning algorithms, specifically Convolutional Neural Networks (CNNs), to precisely extract key points defining the boundaries and markings of the tennis court.

It aims to provide in-depth insights into various aspects of tennis gameplay. It calculates and visualizes player speed, ball shot speed, and the number of shots taken during the match. By leveraging advanced computer vision and machine learning techniques, this project offers a powerful tool for coaches, analysts, and enthusiasts to gain a deeper understanding of player performance, strategy, and game dynamics.

It also provides a practical application of ML, enabling users to build robust systems that can analyze and extract meaningful insights from complex video data.

![Output Video](output_videos/output_video.avi)

## Key Features

- **Player Detection**: Accurately detects and localizes tennis players in the video footage.
- **Ball Detection**: Precisely identifies and tracks the tennis ball during the match.
- **Court Boundary Extraction**: Extracts key points defining the boundaries and markings of the tennis court.
- **Player Speed Calculation**: Calculates the speed of players based on their movement during the match.
- **Ball Shot Speed Estimation**: Estimates the speed of the ball based on its trajectory and movement.
- **Shot Count Analysis**: Counts the number of shots taken by each player during the match.
- **Visualization**: Provides visualizations of player movement, ball trajectory, and court markings.
- **Performance Metrics**: Offers detailed performance metrics for players and the ball.
- **User-Friendly Interface**: Easy-to-use interface for input video selection and analysis.

## Models Used

- **YOLO (You Only Look Once)**: Object detection model for detecting players and the ball. -**Fine Tuned YOLO**: for tennis ball detection -**Court Key Point Extraction**: CNN model for extracting key points defining the tennis court boundaries.

* Trained YOLOV5 model: https://drive.google.com/file/d/1UZwiG1jkWgce9lNhxJ2L0NVjX1vGM05U/view?usp=sharing
* Trained tennis court key point model: https://drive.google.com/file/d/1QrTOF1ToQ4plsSZbkBs3zOLkVt3MBlta/view?usp=sharing

## Training

- Tennis ball detetcor with YOLO: training/tennis_ball_detector_training.ipynb
- Tennis court keypoint with Pytorch: training/tennis_court_keypoints_training.ipynb

## Technologies Used

- **Python**: Programming language used for developing the ML models and analysis system.
- **OpenCV**: Library for computer vision and video processing tasks.
- **PyTorch**: Deep learning framework used for training the tennis court keypoint model.
- **YOLOv5**: Object detection model used for player and ball detection.
- **CNN**: Convolutional Neural Networks used for extracting key points defining the tennis court boundaries.
- **Matplotlib**: Library for creating visualizations and plots.
- **NumPy**: Library for numerical computations and array operations.
- **Pandas**: Library for data manipulation and analysis.
