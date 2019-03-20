# -*- coding: utf-8 -*-

import os
import re


class VTTManager:
    """ clean and parse subtitles associated to each video """

    def __init__(self):
        self.ids = []

    def get_ids(self):
        for dir, dirnames, filenames in os.walk('resources/youtube_downloads'):
            for name in dirnames:
                self.ids.append(name)

    def remove_heading(self, path_vtt, id, lang):
        new_file_path = 'resources/youtube_downloads/{}/{}_heading_removed.{}.vtt'
        new_file_path = new_file_path.format(id, id, lang)
        with open(path_vtt, 'r') as f:
            text = f.readlines()
            for num, line in enumerate(text):
                if line == '##\n':
                    heading_ends = num
                    break
                else:
                    heading_ends = 0
            new_text = text[heading_ends+2:len(text)]
        with open(new_file_path, 'w') as fn:
            fn.write('')
        with open(new_file_path, 'a') as fn:
            for num, line in enumerate(new_text):
                fn.write(line)

    def open_selected_files(self, id):
        path = 'resources/youtube_downloads/{}'
        path = path.format(id)
        for dir, dirname, filenames in os.walk(path):
            for name in filenames:
                if re.search('_heading_removed', name):
                    self.parse_subtitles(id, name)

    def parse_subtitles(self, id, name):
        word_timestamp = {}
        words = []
        times = []
        path = 'resources/youtube_downloads/{}/{}'
        path = path.format(id, name)
        with open(path, 'r') as f:
            text = f.readlines()
            for line in text:
                if re.search('-->', line):
                    time_start = re.split('-->', line)[0]
                    time_end = re.split('-->', line)[1]
                    time_end = re.split(' align', time_end)[0]
                elif re.search('<*>', line):
                    word_time_list = line.split('<c>')
                    if len(word_time_list) == 1:
                        continue
                    else:
                        for num, elem in enumerate(word_time_list):
                            try:
                                if re.search('^<\w*\.\w*>', elem):
                                    elem = re.sub('^<\w*\.\w*>','',elem)
                                word = re.search('[ ]?\w*', elem).group()
                                time = re.search('\d\d\:\d\d\:\d\d\.\d*', elem).group()
                                word_timestamp.update({word:time})
                                words.append(word)
                                times.append(time)
                                # print('word: '+word, '---', 'time: '+time)
                            except:
                                word = re.split('<*',elem)[0]
                                time = time_end
                                word_timestamp.update({word:time})
                                words.append(word)
                                times.append(time)
            print(id, word_timestamp)


    # def parse_subtitles(self, path):
    #     vtt = webvtt.read(path)
    #     for text in vtt:
    #         print(text.start, '--->', text.end)
    #         print(text.text)

    def get_lang_vtt(self, lang):
        path = 'resources/youtube_downloads/{}/{}.{}.vtt'
        for id in self.ids:
            specific_path = path.format(id, id, lang)
            # self.remove_heading(specific_path, id, lang)
            self.open_selected_files(id)
            # self.parse_subtitles(specific_path)


def main():
    manager = VTTManager()
    manager.get_ids()
    manager.get_lang_vtt('es')


if __name__ == '__main__':
    main()
