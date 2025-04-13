import cv2
import os

def extract_frames_from_folder(video_folder, output_folder="frames", fps=5):
    os.makedirs(output_folder, exist_ok=True)
    
    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mov"):  # supports .mov, .mp4, etc.
            video_path = os.path.join(video_folder, video_file)
            video_name = os.path.splitext(video_file)[0]
            subfolder = os.path.join(output_folder, video_name)
            os.makedirs(subfolder, exist_ok=True)

            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                print(f"Error opening {video_file}")
                continue

            video_fps = cap.get(cv2.CAP_PROP_FPS)
            interval = max(1, int(video_fps // fps))  # avoid division by zero

            frame_count = 0
            saved_count = 0
            success, frame = cap.read()

            while success:
                if frame_count % interval == 0:
                    frame_name = f"frame_{saved_count:04d}.jpg"
                    frame_path = os.path.join(subfolder, frame_name)
                    cv2.imwrite(frame_path, frame)
                    saved_count += 1
                frame_count += 1
                success, frame = cap.read()
            
            cap.release()
            print(f"Extracted {saved_count} frames from {video_file}")

# Run the function
if __name__ == "__main__":
    extract_frames_from_folder("scenes")
