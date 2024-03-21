import csv
import isodate
from googleapiclient.discovery import build
from time import sleep
from datetime import datetime

# Set up YouTube API credentials (replace with your own)
API_KEY = "AIzaSyBUVRrpd2jyubk8YQxJNZjiIg0DZwNWkVc"

# YouTube API service (ensure proper authentication)
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to parse duration from ISO format to Minutes:Seconds
# Function to parse duration from ISO format to Minutes:Seconds
def parse_duration(duration_iso):
    try:
        # Use isodate library for robust parsing
        from isodate import parse_duration as parse_iso_duration
        
        # Parse ISO duration string
        duration = parse_iso_duration(duration_iso)
        
        # Extract components
        hours = duration.total_seconds() // 3600
        minutes = (duration.total_seconds() % 3600) // 60
        seconds = duration.total_seconds() % 60
        
        # Format the result
        return f"{int(hours)*60 + int(minutes)}:{int(seconds):02d}"
    except Exception as e:
        print(f"Error parsing duration: {e}")
        return ''



# Function to fetch subscriber count for a channel
def fetch_subscriber_count(channel_id):
    try:
        channel_response = youtube.channels().list(
            id=channel_id,
            part='statistics'
        ).execute()

        if 'items' in channel_response:
            channel_stats = channel_response['items'][0]['statistics']
            subscriber_count = int(channel_stats.get('subscriberCount', 0))
            return subscriber_count
    except Exception as e:
        print(f"Failed to fetch subscriber count for channel {channel_id}: {e}")
    return 0  # Return 0 if subscriber count cannot be fetched

# Function to fetch YouTube data for a given category
def fetch_youtube_data(category):
    search_query = category
    max_results = 50  # Increased to fetch more videos
    next_page_token = None

    csv_file = f"{category}_youtube_data.csv"
    fieldnames = ["Video ID", "Title", "Channel", "Channel ID", "Published At",
                  "Description", "Views", "Likes", "Comments",
                  "Duration (Minutes:Seconds)", "Category", "Tags/Keywords",
                  "Subscriber Count", "Thumbnail URL", "Resolution/Quality", "Language"]

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        print(f"Fetching YouTube data for category: {category}")

        while True:
            try:
                search_response = youtube.search().list(
                    q=search_query,
                    type="video",
                    part="id,snippet",
                    maxResults=max_results,
                    pageToken=next_page_token
                ).execute()

                video_ids = [item['id']['videoId'] for item in search_response['items']]
                video_response = youtube.videos().list(
                    id=",".join(video_ids),
                    part='snippet,statistics,contentDetails'
                ).execute()

                for video_info in video_response['items']:
                    # Extract relevant information from video response
                    video_id = video_info['id']
                    snippet = video_info['snippet']
                    statistics = video_info.get('statistics', {})
                    content_details = video_info.get('contentDetails', {})

                    # Extract required fields
                    title = snippet.get('title', '')
                    channel = snippet.get('channelTitle', '')
                    channel_id = snippet.get('channelId', '')
                    published_at = snippet.get('publishedAt', '')
                    description = snippet.get('description', '')
                    views = statistics.get('viewCount', 0)
                    likes = statistics.get('likeCount', 0)
                    comments = statistics.get('commentCount', 0)
                    duration_iso = content_details.get('duration', '')
                    duration = parse_duration(duration_iso)

                    # Fetch subscriber count
                    subscriber_count = fetch_subscriber_count(channel_id)

                    # Write data to CSV file
                    writer.writerow({
                        "Video ID": video_id,
                        "Title": title,
                        "Channel": channel,
                        "Channel ID": channel_id,
                        "Published At": published_at,
                        "Description": description,
                        "Views": views,
                        "Likes": likes,
                        "Comments": comments,
                        "Duration (Minutes:Seconds)": duration,
                        "Category": category,
                        "Tags/Keywords": ', '.join(snippet.get('tags', [])),
                        "Subscriber Count": subscriber_count,
                        "Thumbnail URL": snippet['thumbnails']['default']['url'],
                        "Resolution/Quality": '',  # Resolution/Quality not directly provided by API
                        "Language": snippet.get('defaultLanguage', '')
                    })

                # Check if there are more pages of results
                next_page_token = search_response.get('nextPageToken')
                if not next_page_token:
                    print(f"Data fetched for category: {category}")
                    break

            except Exception as e:
                print(f"An error occurred: {e}")
                break

    print(f"YouTube data fetching for category {category} complete.")

# List of categories
categories = [ "Shopping", "Finance", "Films","Music","Health&Fitness","Technology","travel & adventure","Gaming","Finance","Cooking$Recepis"]

# Fetch data for each category
for category in categories:
    fetch_youtube_data(category)
