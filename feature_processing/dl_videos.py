import pandas as pd
import numpy as np
import os
from yt_dlp import YoutubeDL

def youtube_dl(video_id):
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    video_name = f'{video_id}.mp4'

    ydl_opts = {
        'outtmpl': 'videos/' + video_name,
        'format': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


df = pd.read_csv('./files/train_subset_10.csv')

faulty_videos = 0
total_videos = df.shape[0]
video_paths_file = './video_paths.txt'
batch_size = 20

extractor_command = f'''
    python main.py feature_type=r21d file_with_video_paths="{video_paths_file}" on_extraction=save_pickle
'''
clear_videos = f'''
    rm -rf videos/*
'''

with open(video_paths_file, 'w') as paths_file:
    for i in range(0, total_videos, batch_size):
        #os.system(clear_videos)
        for j in range(0, batch_size):
            video_id = df.loc[i + j]['youtube_id']
            try:
                if not os.path.exists(f'videos/{video_id}.mp4'):
                    youtube_dl(video_id)
                    paths_file.write(f'videos/{video_id}.mp4')
            except Exception as e:
                faulty_videos += 1
                print(f'Error downloading video {video_id}')
                print(e)
        #os.system(extractor_command)
        print(f'Batch {i + 1} - {i + batch_size} downloaded')

print(f'{total_videos - faulty_videos} out of {total_videos} videos downloaded successfully')
    