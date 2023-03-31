###TikTok Bulk Downloader

This script allows you to bulk download all videos from a specified TikTok user profile. The script is modular and uses a config.json file to set the username and download folder.

##Prerequisites

To run the script, you will need Python 3.6 or later and the tiktok-scraper package. You can install the package using the following command:

`pip install tiktok-scraper`

##Usage

    Clone this repository or copy the tiktok_bulk_downloader.py script to your local machine.

    Create a config.json file in the same directory as your script with the following structure:


`{
    "username": "your_tiktok_username",
    "download_folder": "tiktok_downloads"
}`

Replace "your_tiktok_username" with the desired TikTok username, and "tiktok_downloads" with your desired download folder.

    Run the script using the following command:

`python tiktok_bulk_downloader.py`

The script will then download all videos from the specified TikTok user's profile to the specified download folder. If a video has already been downloaded, the script will skip it.

##Configuration

To change the TikTok username or download folder, simply edit the config.json file and update the "username" and/or "download_folder" values as needed.

##License

This project is licensed under the GPL v3 License.