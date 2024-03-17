# Music Segment Downloader

This script, `main.py`, automates the process of downloading specific segments from YouTube videos as MP3 files, using `yt-dlp`. It reads a CSV file containing YouTube video IDs and the corresponding start and end times for each segment you wish to download. This is particularly useful for creating samples, clips, or extracting specific parts of audio from longer videos.

## Features

- Download specific segments of YouTube videos as MP3.
- Parallel downloads to improve efficiency.
- Customizable download directory and parallel download count.

## Prerequisites

Before you run this script, you need to have the following installed on your system:
- Python 3.9.10 or higher
- `yt-dlp` Python package
- `pandas` Python package

You can install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
Prepare Your CSV File: Ensure you have a CSV file with the columns ytid, start_s, and end_s, representing the YouTube video ID, the start time of the segment in seconds, and the end time of the segment in seconds, respectively.

Run the Script: Navigate to the directory containing main.py and run the following command:

```bash
python download_music_segments.py --data path/to/yourfile.csv --directory path/to/download/directory --delimiter "," --max-workers N
```

Replace path/to/yourfile.csv with the path to your CSV file, path/to/download/directory with the path where you want the MP3 files to be saved, "," with the delimiter used in your CSV file (if different from a comma), and N with the number of parallel downloads you wish to run.

## Arguments
* data: Path to the CSV file containing the download information. Default is data.csv.
* directory: Path to the directory where the MP3 files will be saved. Default is music.
* delimiter: Delimiter used in the CSV file. Default is ,.
* max-workers: Number of parallel downloads. Default is 5.

## Example CSV Format
Your CSV file should follow this format:

```
ytid,start_s,end_s
dQw4w9WgXcQ,10,20
```
This example would download the audio from 10 to 20 seconds of the video with ID dQw4w9WgXcQ.

## Disclaimer
This script is provided for educational purposes only. Be mindful of YouTube's Terms of Service before downloading content.