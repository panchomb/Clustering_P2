import os
import subprocess
import shutil
from pathlib import Path

def get_video_size(file_path):
    """Returns the size of the video file in MB."""
    return os.path.getsize(file_path) / (1024 * 1024)

def split_video(video_path, output_folder, target_size_mb=2):
    """Splits a video into multiple parts, ensuring each part is at most target_size_mb."""
    video_id = Path(video_path).stem  # Extracts the YouTube video ID
    output_template = os.path.join(output_folder, f"{video_id}_part%d.mp4")
    
    # Estimate the duration needed per segment (assumption: size is roughly linear to duration)
    total_size = get_video_size(video_path)
    if total_size <= target_size_mb:
        shutil.copy(video_path, os.path.join(output_folder, f"{video_id}_part1.mp4"))
        return
    
    # Get video duration
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    duration = float(result.stdout.strip())
    
    num_parts = int(total_size // target_size_mb) + 1
    segment_duration = duration / num_parts
    
    for i in range(num_parts):
        start_time = i * segment_duration
        output_file = output_template % (i + 1)
        
        subprocess.run([
            "ffmpeg", "-i", video_path, "-ss", str(start_time), "-t", str(segment_duration),
            "-c", "copy", output_file, "-y"
        ])

def process_videos(input_folder, output_folder):
    """Processes all videos in the input folder, ensuring they are at most 2MB in size."""
    os.makedirs(output_folder, exist_ok=True)
    
    for video_file in os.listdir(input_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(input_folder, video_file)
            split_video(video_path, output_folder)
    
if __name__ == "__main__":
    input_folder = "videos/"
    output_folder = "processed_videos/"
    process_videos(input_folder, output_folder)
    print("Processing complete. Check the 'processed_videos/' folder.")
