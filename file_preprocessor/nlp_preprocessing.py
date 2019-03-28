import re


class NLPPreprocessor:

    @staticmethod
    def get_spanish_stopwords():
        stop_words = []
        with open('file_preprocessor/spanish_stopwords.txt', 'r') as f:
            stopwords = f.readlines()
            for line in stopwords:
                line = re.sub('\n', '', line)
                stop_words.append(line)
        return stop_words

    def remove_stopwords(self, data, ids):
        stop_words = self.get_spanish_stopwords()
        new_data = {}
        for num, chunk in enumerate(data):
            id = ids[num]
            print(id)
            words = chunk[id].keys()
            for word in words:
                if word not in stop_words:
                    print(word, '--->', chunk[id][word])
                    # new_data.update({word: chunk[id][word]})
                    # no_stop_words.append(word)
        # print(new_data)
