import googleapiclient.discovery
import googleapiclient.errors

def get_channel_videos(api_key, channel_id):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    # Get the playlist ID for the channel's uploaded videos
    channel_response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    if not channel_response.get("items"):
        print("No channel found for the provided ID.")
        return []

    playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Retrieve videos from the playlist
    video_ids = []
    next_page_token = None

    while True:
        playlist_response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,  # Max allowed per request
            pageToken=next_page_token
        ).execute()

        # Extract video IDs
        for item in playlist_response.get("items", []):
            video_ids.append(item["contentDetails"]["videoId"])

        # Check for next page
        next_page_token = playlist_response.get("nextPageToken")
        if not next_page_token:
            break

    return video_ids

def save_to_file(video_ids, filename="video_ids.txt"):
    try:
        with open(filename, "w") as f:
            for video_id in video_ids:
                f.write(video_id + "\n")
        print(f"Saved {len(video_ids)} video IDs to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    # Replace with your YouTube Data API key
    API_KEY = "AIzaSyD9HzaFhzW7EHnkGcjNquEbUeidSExr1Z8"

    # Prompt user for channel ID
    channel_id = input("Enter the YouTube channel ID (e.g., UCdJwPghVETTxYLXFxplLwPQ): ").strip()

    # Validate channel ID format (basic check)
    if not channel_id.startswith("UC") or len(channel_id) != 24:
        print("Invalid channel ID format. It should start with 'UC' and be 24 characters long.")
        return

    video_ids = get_channel_videos(API_KEY, channel_id)

    if video_ids:
        print(f"Found {len(video_ids)} videos.")
        save_to_file(video_ids)
    else:
        print("No videos found or an error occurred.")

if __name__ == "__main__":
    main()