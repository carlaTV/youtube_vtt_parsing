import os
from os import walk
import re
from shutil import copyfile

# class YoutubeSubtitle:
#     def __init__(self, id, lang):
#         self.id = id
#         self.lang = lang
#         self.extension = 'vtt'
#
# class YoutubeAudio:
#     def __init__(self, id):
#         self.id = id
#         self.extension = 'webm'

class DownloadsManager():
    def __init__(self):
        self.ids = []
        self.filename = None
        self.subtitle = None
        self.audio = None

    def get_file_ids(self):
        for dirpath, dirnames, self.filename in walk('resources/youtube_downloads'):
            for name in self.filename:
                try:
                    # subtitles
                    id, lang, extension = name.split('.')
                    # self.subtitle = YoutubeSubtitle(id, lang)
                    if id not in self.ids:
                        self.ids.append(id)
                    # print('SUBTITLES: ', id, '---', lang, '---', extension)
                except:
                    if re.search('.webm', name):
                        # audio:
                        id, extension = name.split('.')
                        # self.audio = YoutubeAudio(id)
                        # print('AUDIO: ', id, '---', extension)
                    else:
                        os.remove('resources/youtube_downloads/%s' % name)
                        # print(name)

    def make_dir_for_each_video(self):
        for element in self.ids:
            os.mkdir('resources/youtube_downloads/%s' % element)

    def move_videos_to_dir(self):
        origin_path = 'resources/youtube_downloads/{}'
        dest_path = 'resources/youtube_downloads/{}/{}'
        for d, dn, self.filename in walk('resources/youtube_downloads'):
            for name in self.filename:
                try:
                    id, lang, extension = name.split('.')
                except:
                    id, extension = name.split('.')
                copyfile(origin_path.format(name), dest_path.format(id, name))
