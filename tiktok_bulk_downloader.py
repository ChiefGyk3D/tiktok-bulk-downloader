import json
import os
import subprocess

# Load configuration from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

username = config["username"]
download_folder = config["download_folder"]

# Ensure the download folder exists
os.makedirs(download_folder, exist_ok=True)

def is_downloaded(video_id):
    """Check if a video has been downloaded already."""
    for filename in os.listdir(download_folder):
        if video_id in filename:
            return True
    return False

def download_videos(videos):
    """Download TikTok videos without a watermark."""
    for video in videos:
        video_id = video['id']

        # Check if the video has already been downloaded
        if not is_downloaded(video_id):
            # Download the video without the watermark
            command = f"tiktok-scraper video {video['video']['playAddr']} -o {download_folder} -w"
            subprocess.run(command, shell=True, check=True)
            print(f"Downloaded video {video_id}")
        else:
            print(f"Skipped video {video_id} (already downloaded)")

def main():
    # Get the user's videos
    command = f"tiktok-scraper user {username} -t json -n 0"
    user_videos_raw = subprocess.check_output(command, shell=True)
user_videos = json.loads(user_videos_raw)["collector"]

# Download the videos
download_videos(user_videos)
if name == "main":
    main()