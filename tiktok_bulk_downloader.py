import json
import os
from tiktok_scraper import TikTokScraper

# Load configuration from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

username = config["username"]
download_folder = config["download_folder"]

# Ensure the download folder exists
os.makedirs(download_folder, exist_ok=True)

# Initialize the TikTokScraper
scraper = TikTokScraper()

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
        video_url = video['video']['playAddr']

        # Check if the video has already been downloaded
        if not is_downloaded(video_id):
            # Download the video without the watermark
            scraper.download_video(video_url, os.path.join(download_folder, f'{video_id}.mp4'), wm=False)
            print(f"Downloaded video {video_id}")
        else:
            print(f"Skipped video {video_id} (already downloaded)")

def main():
    # Get the user's videos
    user_videos = scraper.user_videos(username)

    # Download the videos
    download_videos(user_videos)

if __name__ == "__main__":
    main()
# Get the user's videos
user_videos = scraper.user_videos(username)
# Download the videos
download_videos(user_videos)