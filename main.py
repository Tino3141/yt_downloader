import subprocess
import pandas as pd
import argparse
from concurrent.futures import ThreadPoolExecutor

def download_segment(track_info, directory="music"):
    ytid, start_s, end_s = track_info
    output_filename = f"{directory}/{ytid}_{start_s}_{end_s}.mp3"
    command = (
        f"yt-dlp -x --audio-format mp3 --postprocessor-args "
        f"\"-ss {start_s} -to {end_s}\" -o \"{output_filename}\" {ytid}"
    )
    subprocess.run(command, shell=True)

def download_music_from_segments(data_file, directory="music", max_workers=5, delimiter=","):
    data = pd.read_csv(data_file, delimiter=delimiter)
    search_terms = [(row["ytid"], row["start_s"], row["end_s"]) for index, row in data.iterrows()]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_segment, track_info, directory) for track_info in search_terms]
        for future in futures:
            future.result()  # Handle exceptions here if needed

def main():
    parser = argparse.ArgumentParser(description='Download specific segments of music tracks')
    parser.add_argument('--data', type=str, default='data.csv', help='Path to data file')
    parser.add_argument('--directory', type=str, default='music', help='Path to directory where audio files will be stored')
    parser.add_argument('--delimiter', type=str, default=",", help='CSV delimiter')
    parser.add_argument('--max-workers', type=int, default=5, help='Number of parallel downloads')
    
    args = parser.parse_args()
    
    download_music_from_segments(args.data, directory=args.directory, max_workers=args.max_workers, delimiter=args.delimiter)

if __name__ == "__main__":
    main()