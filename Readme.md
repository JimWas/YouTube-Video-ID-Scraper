# YouTube Video ID Scraper

This Python script retrieves all video IDs from a specified YouTube channel's uploads playlist using the YouTube Data API v3 and saves them to a text file (`video_ids.txt`). The script prompts the user to input a YouTube channel ID, making it flexible for use with any channel.

## Features
- Prompts the user to input a YouTube channel ID (e.g., `UCdJwPghVETTxYLXFxplLwPQ`).
- Fetches all video IDs from the channel's uploads playlist.
- Saves video IDs to `video_ids.txt`, with each ID on a new line.
- Includes basic validation for channel ID format.
- Handles API errors and file-writing exceptions gracefully.

## Prerequisites
- Python 3.x
- Google API Client Library for Python
- A Google Cloud project with the YouTube Data API v3 enabled
- An API key from the Google Cloud Console

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-video-id-scraper.git
   cd youtube-video-id-scraper

Install Dependencies:
Install the required Python library using pip:bash

pip install google-api-python-client

Set Up Google Cloud Project:Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable the YouTube Data API v3 for your project.
Navigate to the "Credentials" section and create an API key.
Copy the API key for use in the script.

Configure the Script:Open get_youtube_videos.py in a text editor.
Replace "YOUR_API_KEY" with your actual API key from the Google Cloud Console.

UsageRun the Script:bash

python get_youtube_videos.py

Enter Channel ID:When prompted, enter a valid YouTube channel ID (e.g., UCdJwPghVETTxYLXFxplLwPQ).
A valid channel ID typically starts with UC and is 24 characters long.

Output:The script will fetch all video IDs from the channel's uploads playlist.
Video IDs are saved to video_ids.txt in the same directory.
The console will display the number of videos found and confirm the file save.

Example Output

Enter the YouTube channel ID (e.g., UCdJwPghVETTxYLXFxplLwPQ): UCdJwPghVETTxYLXFxplLwPQ
Found 150 videos.
Saved 150 video IDs to video_ids.txt

The video_ids.txt file will contain:

dQw4w9WgXcQ
abc123xyz456
...

NotesAPI Quota: The YouTube Data API has a default quota of 10,000 units per day for free accounts. Fetching many videos may consume significant quota. Monitor usage in the Google Cloud Console.
Error Handling: The script validates channel IDs and handles API and file errors. If you encounter a Quota Exceeded error, check your API quota or wait for the next quota reset.
File Overwrite: The script overwrites video_ids.txt if it exists. To append instead, modify the save_to_file function in the script to use "a" mode instead of "w".
Channel ID: Find a channel's ID by visiting its YouTube page and checking the URL (e.g., https://www.youtube.com/channel/UCdJwPghVETTxYLXFxplLwPQ) or inspecting the page source for the channelId meta tag.

TroubleshootingInvalid API Key: Ensure your API key is correct and the YouTube Data API is enabled.
Invalid Channel ID: Verify the channel ID format (starts with UC, 24 characters long).
Quota Exceeded: Check your API quota in the Google Cloud Console or reduce the maxResults value in the script (default is 50, the maximum per request).
No Videos Found: The channel may have no public videos, or the ID may be incorrect.

ContributingContributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.LicenseThis project is licensed under the MIT License. See the LICENSE file for details.DisclaimerThis script is for educational and personal use. Ensure compliance with YouTube's Terms of Service and the Google API Terms of Service when using this script.


---

### Instructions for GitHub Setup
1. **Create a Repository**:
   - Go to GitHub and create a new repository (e.g., `youtube-video-id-scraper`).
   - Copy the description above into the repository description field.
   - Initialize the repository with a README (you can overwrite it with the one above).

2. **Add the Script**:
   - Save the Python script from the previous response as `get_youtube_videos.py`.
   - Create a `README.md` file with the content above.
   - Optionally, add a `LICENSE` file (e.g., MIT License) if you want to specify licensing.

3. **Push to GitHub**:
   ```bash
   git init
   git add get_youtube_videos.py README.md LICENSE
   git commit -m "Initial commit with YouTube video ID scraper script and README"
   git remote add origin https://github.com/your-username/youtube-video-id-scraper.git
   git push -u origin main