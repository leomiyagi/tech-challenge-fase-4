import cv2
import os

def cut_video(input_path, output_path, duration=10):
    # Open the input video
    cap = cv2.VideoCapture(input_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the number of frames to capture
    frames_to_capture = min(duration * fps, total_frames)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Read and write the frames
    for _ in range(frames_to_capture):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video cut successfully. Saved to {output_path}")

# Path to the input video file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')  # Replace with your input video file name
output_video_path = os.path.join(script_dir, 'video_cut.mp4')  # Replace with your desired output video file name

# Cut the video and save the first 10 seconds
cut_video(input_video_path, output_video_path)