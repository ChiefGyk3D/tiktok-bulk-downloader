import os
import json
from tiktok_scraper import TikTokScraper

def download_tiktoks(username, download_folder):
    scraper = TikTokScraper()

    # Scrape TikTok user profile and video metadata
    user_data = scraper.get_user(username)
    user_videos = scraper.get_user_videos(username, count=user_data['stats']['videoCount'])

    # Create download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Download TikTok videos
    for video in user_videos:
        video_id = video['id']
        video_url = video['video']['playAddr']
        local_video_path = os.path.join(download_folder, f"{video_id}.mp4")

        if not os.path.exists(local_video_path):
            print(f"Downloading {video_id}...")
            scraper.download_video(video_url, local_video_path)
            print(f"Downloaded {video_id} to {local_video_path}")
        else:
            print(f"Already downloaded {video_id}")

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    config_path = "config.json"
    config = load_config(config_path)
    my_username = config["username"]
    my_download_folder = config["download_folder"]

    download_tiktoks(my_username, my_download_folder)

