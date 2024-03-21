YouTube Data Fetcher

This Python script is designed to fetch data from YouTube for specified categories and store it in CSV format. The script utilizes the YouTube Data API for retrieving information about videos and channels. Below is a detailed breakdown of the script:

Dependencies
csv: Python library for CSV file operations.
isodate: Python library for parsing ISO format durations.
googleapiclient: Python library for interacting with the YouTube API.
datetime: Python library for working with date and time.
Setup
Before running the script, ensure the following:

YouTube API Key (API_KEY): Replace "YOUR_API_KEY" with your own API key. You can obtain an API key by creating a project in the Google Developers Console and enabling the YouTube Data API.

Python Environment: Ensure you have Python installed on your system along with the required dependencies listed above.

Usage
Update API Key: Replace "YOUR_API_KEY" with your YouTube API key.
Run the Script: Execute the script in a Python environment.
View Results: Fetched data will be stored in CSV files named <category>_youtube_data.csv in the same directory as the script.
Objectives
Fetch YouTube Data: The script fetches data such as video title, channel, views, likes, comments, etc., for specified categories from YouTube using the YouTube Data API.

Parse Duration: It parses the duration of videos from ISO format to Minutes:Seconds format using the isodate library.

Fetch Subscriber Count: The script retrieves the subscriber count for each channel by making additional API requests.

Store Data: Fetched data is stored in CSV files for further analysis. The script writes the following columns to the CSV files:

Video ID
Title
Channel
Channel ID
Published At
Description
Views
Likes
Comments
Duration (Minutes:Seconds)
Category
Tags/Keywords
Subscriber Count
Thumbnail URL
Resolution/Quality (Not directly provided by API)
Language
How to Run
Define Categories: Define the categories for which you want to fetch YouTube data in the categories list.

Run the Script: The script iterates through each category, fetches data, and stores it in respective CSV files.

Example Categories
Shopping
Finance
Films
Music
Health & Fitness
Technology
Travel & Adventure
Gaming
Cooking & Recipes
Error Handling
The script handles errors gracefully and logs them for reference. It continues fetching data for other categories even if an error occurs for a particular category.
Note
Ensure proper authentication is set up for the YouTube API to avoid any authorization errors.
This script is provided as is and may require further customization based on your specific needs and YouTube API usage limits.