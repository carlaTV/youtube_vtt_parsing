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

    def get_ids(self):
        video_names = []
        for dir, dirnames, filenames in os.walk('resources/youtube_downloads'):
            for name in dirnames:
                self.ids.append(name)
                video_names.append(name)
        return video_names

    def open_selected_files(self, id, lang):
        path = 'resources/youtube_downloads/{}'
        path = path.format(id)
        for dir, dirname, filenames in os.walk(path):
            for name in filenames:
                if re.search('_heading_removed', name) and re.search(lang, name):
                    id_parsed_vtt, words_times = self.parse_vtt_word_time(id, name)
        return id_parsed_vtt, words_times

    def parse_vtt_word_time(self, id, name):
        """ This function deals with subtitles that have a word-timestamp relationship"""
        word_timestamp = Dictlist()
        id_parsed_vtt = {}
        words = []
        times = []
        words_times = []
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
                                    elem = re.sub('^<\w*\.\w*>', '', elem)
                                word = re.search('[ ]?\w*', elem).group()
                                time = re.search('\d\d\:\d\d\:\d\d\.\d*', elem).group()
                                if num == 0:
                                    timestamp = [time_start, time]
                                    time_anterior = time
                                if num != 0 and num != len(word_time_list):
                                    timestamp = [time_anterior, time]
                                    time_anterior = time
                                if num == len(word_time_list):
                                    timestamp = [time_anterior, time_end]
                                word_timestamp[word] = timestamp
                                words_times.append([word, timestamp])
                            except:
                                word = re.split('<*', elem)[0]
                                time = time_end
                                if word in words and time in times:
                                    continue
                                else:
                                    word_timestamp[word] = timestamp
                                    words.append(word)
                                    times.append(time)
                                    words_times.append([word, timestamp])
                            # print('word: ', word, timestamp)
            if not word_timestamp:
                id_parsed_vtt, words_times = self.parse_vtt_sent_time(id, name)
            else:
                id_parsed_vtt.update({id: word_timestamp})
                # print(id_parsed_vtt)
            return id_parsed_vtt, words_times

    def parse_vtt_sent_time(self, id, name):
        """This function deals with subtitles that have timestamps for each sentence instead of for each word."""
        path = 'resources/youtube_downloads/{}/{}'
        path = path.format(id, name)
        # time_format = '%H:%M:%S.%f'
        words = []
        times = []
        words_times = []
        word_timestamp = Dictlist()
        id_parsed_vtt = {}
        with open(path, 'r') as f:
            text = f.readlines()
            for num, line in enumerate(text):
                if re.search('-->', line):
                    time_start = re.split('-->', line)[0]
                    time_start = re.sub(' ', '', time_start)
                    time_end = re.split('-->', line)[1]
                    time_end = re.sub(' ', '', time_end)
                    time_end = re.sub('\n$', '', time_end)
                    timestamp = [time_start, time_end]
                    # duration = datetime.strptime(time_end, time_format) - datetime.strptime(time_start, time_format)
                    # duration = duration.seconds + float(duration.microseconds) / 1e6
                elif re.search(r'\w* ', line):
                    words_in_this_line = line.split(' ')
                    for word in words_in_this_line:
                        # word += str(num)
                        if word in words and time_start in times:
                            continue
                        else:
                            words.append(word)
                            times.append(time_start)
                            word_timestamp[word] = timestamp
                            words_times.append([word, timestamp])
                        # word_timestamp.update({word: time_start})
                else:
                    continue
            id_parsed_vtt.update({id: word_timestamp})
            # print(id_parsed_vtt)
            return id_parsed_vtt, words_times

    def parse_vtt(self, ids, lang):
        data = []
        data_list = {}
        for id in ids:
            try:
                id_parsed_vtt, words_times = self.open_selected_files(id, lang)
                data.append(id_parsed_vtt)
                data_list.update({id: words_times})
            except Exception:
                print('could not process file %s' %id)
        return data, data_list
