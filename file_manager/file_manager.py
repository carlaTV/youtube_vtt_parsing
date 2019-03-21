import re


class FileManager:
    def __init__(self):
        self.path = 'resources/word_timestamps/{}.json'

    def write_results_opening(self, id):
        path = self.path.format(id)
        opening_line = '{{ \n "{}": {{\n'
        with open(path, 'w') as f:
            f.write(opening_line.format(id))

    def write_results_content(self, id, data):
        word_timestamp = '\t "{}" : "{}",\n'
        to_write = data[id]
        with open(self.path.format(id), 'a') as f:
            for num, elem in enumerate(to_write):
                word_timestamp = word_timestamp.format(elem[0], elem[1])
                if num != len(to_write)-1:
                    f.write(word_timestamp)
                else:
                    f.write(re.sub(',', '', word_timestamp))
                word_timestamp = '\t "{}" : "{}",\n'

    def write_results_content_data(self, id, data):
        word = '\t"{}" : [\n'
        timestamps = '\t\t"{}",\n'
        to_write = data[id]
        with open(self.path.format(id), 'a') as f:
            for num, elem in enumerate(to_write):
                word = word.format(elem)
                f.write(word)
                for iter, time in enumerate(to_write[elem]):
                    if iter != len(to_write[elem])-1:
                        f.write(timestamps.format(time))
                    else:
                        f.write(re.sub(',', '', timestamps.format(time)))
                    timestamps = '\t\t"{}",\n'
                word = '\t"{}" : [\n'
                if num != len(to_write)-1:
                    f.write('\t\t],\n')
                else:
                    f.write('\t\t]\n')

    def write_end_file(self, id):
        with open(self.path.format(id), 'a') as f:
            f.write('}}\n')
