import os
from os import walk
import re

class YoutubeDownloader():
    def __init__(self):
        self.videos_list = []
        self.download_command = "youtube-dl --output \"{}\" --all-subs --write-auto-sub " \
                   "--extract-audio --audio-format mp3 " \
                   "https://www.youtube.com/watch?v={}"

    def read_ids(self):
        with open('resources/ids_list', 'r') as f:
            videos = f.readlines()
            for id in videos:
                id = re.sub('\n','', id)
                id = re.sub('"', '', id)
                self.videos_list.append(id)
        return self.videos_list

    def download_videos(self):
        path_to_check = 'resources/youtube_downloads/{}'
        for id in self.videos_list:
            if not os.path.exists(path_to_check.format(id)):
                try:
                    path = '/home/carlatv/PycharmProjects/youtube_vtt_parsing/resources/youtube_downloads/{}/{}.%(ext)s.%(ext)s'
                    # path = 'resources/.%(ext)s.%(ext)s'
                    path = path.format(id, id)
                    # print(path, id)
                    command = self.download_command.format(path, id)
                    # print(command)
                    os.system(command)
                except:
                    continue
            else:
                continue