# -*- coding: utf-8 -*-

import os
import re
from datetime import datetime


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

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

    def open_selected_files(self, id):
        path = 'resources/youtube_downloads/{}'
        path = path.format(id)
        for dir, dirname, filenames in os.walk(path):
            for name in filenames:
                if re.search('_heading_removed', name):
                    self.parse_vtt_word_time(id, name)

    def parse_vtt_word_time(self, id, name):
        """ This function deals with subtitles that have a word-timestamp relationship"""
        word_timestamp = Dictlist()
        id_parsed_vtt = {}
        words = []
        times = []
        path = 'resources/youtube_downloads/{}/{}'
        path = path.format(id, name)
        with open(path, 'r') as f:
            text = f.readlines()
            for num, line in enumerate(text):
                if re.search('-->', line):
                    # time_start = re.split('-->', line)[0]
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
                                    elem = re.sub('^<\w*\.\w*>', '', elem)
                                word = re.search('[ ]?\w*', elem).group()
                                time = re.search('\d\d\:\d\d\:\d\d\.\d*', elem).group()
                                word_timestamp[word] = time
                            except:
                                word = re.split('<*', elem)[0]
                                time = time_end
                                if word in words and time in times:
                                    continue
                                else:
                                    word_timestamp[word] = time
                                    words.append(word)
                                    times.append(time)
            if not word_timestamp:
                self.parse_vtt_sent_time(id, name)
            else:
                id_parsed_vtt.update({id: word_timestamp})
                print(id_parsed_vtt)

    def parse_vtt_sent_time(self, id, name):
        """This function deals with subtitles that have timestamps for each sentence instead of for each word."""
        path = 'resources/youtube_downloads/{}/{}'
        path = path.format(id, name)
        # time_format = '%H:%M:%S.%f'
        words = []
        times = []
        word_timestamp = Dictlist()
        id_parsed_vtt = {}
        with open(path, 'r') as f:
            text = f.readlines()
            for num, line in enumerate(text):
                if re.search('-->', line):
                    time_start = re.split('-->', line)[0]
                    time_start = re.sub(' ', '', time_start)
                    # time_end = re.split('-->', line)[1]
                    # time_end = re.sub(' ', '', time_end)
                    # time_end = re.sub('\n$', '', time_end)
                    # duration = datetime.strptime(time_end, time_format) - datetime.strptime(time_start, time_format)
                    # duration = duration.seconds + float(duration.microseconds) / 1e6
                elif re.search(r'\w* ', line):
                    words = line.split(' ')
                    for word in words:
                        # word += str(num)
                        if word in words and time_start in times:
                            continue
                        else:
                            words.append(word)
                            times.append(time_start)
                            word_timestamp[word] = time_start
                        # word_timestamp.update({word: time_start})
                else:
                    continue
            id_parsed_vtt.update({id: word_timestamp})
            print(id_parsed_vtt)

    def parse_vtt(self):
        for id in self.ids:
            self.open_selected_files(id)


def main():
    manager = VTTManager()
    manager.get_ids()
    manager.parse_vtt()


if __name__ == '__main__':
    main()
