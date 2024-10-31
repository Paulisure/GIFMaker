# Gif Maker

import cv2
import numpy as np
from PIL import Image
import os

def create_gif(video_path, gif_path, target_size=(800, 600), fps=10):
    """
    Convert video to optimized GIF for GitHub
    """
    # Verify video path exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    # Read video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video file")
    
    frames = []
    frame_count = 0
    
    print(f"Converting video to GIF...")
    print(f"Target size: {target_size}")
    print(f"Target FPS: {fps}")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process every nth frame to reduce GIF size
        if frame_count % (30//fps) == 0:
            # Resize frame
            frame = cv2.resize(frame, target_size)
            
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Add frame to list
            frames.append(Image.fromarray(frame_rgb))
        
        frame_count += 1
    
    cap.release()
    
    if not frames:
        raise ValueError("No frames were extracted from the video")
    
    print(f"Extracted {len(frames)} frames")
    print(f"Saving GIF to: {gif_path}")
    
    # Save as GIF
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=1000//fps,  # Duration between frames in milliseconds
        loop=0,
        optimize=True
    )
    
    gif_size = os.path.getsize(gif_path) / (1024 * 1024)  # Size in MB
    print(f"GIF created successfully! Size: {gif_size:.2f}MB")

if __name__ == "__main__":
    # Use raw strings for Windows paths
    video_path = r"C:\Github_Projects\AutonomousDrone-EmbeddedAI\object_detection\optimizedobj.mp4"
    gif_path = r"C:\Github_Projects\AutonomousDrone-EmbeddedAI\object_detection\object_detection_demo.gif"
    
    try:
        create_gif(video_path, gif_path)
    except Exception as e:
        print(f"Error creating GIF: {str(e)}")