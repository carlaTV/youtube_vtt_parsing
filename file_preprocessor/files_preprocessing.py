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

    @staticmethod
    def remove_heading(id, lang):
        source_path = 'resources/youtube_downloads/{}/{}.webm.{}.vtt'
        source_path = source_path.format(id, id, lang)
        new_file_path = 'resources/youtube_downloads/{}/{}_heading_removed.{}.vtt'
        new_file_path = new_file_path.format(id, id, lang)
        try:
            with open(source_path, 'r') as f:
                text = f.readlines()
                for num, line in enumerate(text):
                    # if line == '##\n':
                    if line.startswith('00:'):
                        heading_ends = num
                        break
                    else:
                        heading_ends = 0
                new_text = text[heading_ends - 1:len(text)]
            with open(new_file_path, 'w') as fn:
                fn.write('')
            with open(new_file_path, 'a') as fn:
                for num, line in enumerate(new_text):
                    fn.write(line)
        except:
            pass
    # def make_dir_for_each_video(self):
    #     for element in self.ids:
    #         os.mkdir('resources/youtube_downloads/%s' % element)
    #
    # def move_videos_to_dir(self):
    #     origin_path = 'resources/youtube_downloads/{}'
    #     dest_path = 'resources/youtube_downloads/{}/{}'
    #     for d, dn, self.filename in walk('resources/youtube_downloads'):
    #         for name in self.filename:
    #             try:
    #                 id, lang, extension = name.split('.')
    #             except:
    #                 id, extension = name.split('.')
    #             copyfile(origin_path.format(name), dest_path.format(id, name))
