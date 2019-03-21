from file_preprocessor import files_preprocessing as fp
from file_preprocessor import remove_stopwords as stpw
from vtt_manager import vtt_manager as vttm
from file_manager import file_manager as fm


class Pipeline:
    def __init__(self):
        self.data = None
        self.data_list = None
        self.ids = None

    def pre_process(self):
        downloader = fp.DownloadsManager()
        downloader.move_videos_to_dir()

    def process(self):
        manager = vttm.VTTManager()
        self.ids = manager.get_ids()
        self.data, self.data_list = manager.parse_vtt()

    def save_results(self):
        file_manager = fm.FileManager()

        # for id in self.ids:
        #     file_manager.write_results_opening(id)
        #     file_manager.write_results_content(id, self.data_list)
        #     file_manager.write_end_file(id)

        for num, chunk in enumerate(self.data):
            file_manager.write_results_opening(self.ids[num])
            file_manager.write_results_content_data(self.ids[num], chunk)
            file_manager.write_end_file(self.ids[num])


def main():
    pipeline = Pipeline()

    preprocessing = input('Do you want to preprocess the files? [Y/n]\n')
    if preprocessing.upper() == 'y':
        pipeline.pre_process()
    else:
        pipeline.process()
        pipeline.save_results()


if __name__ == '__main__':
    main()
