from file_preprocessor import files_preprocessing as fp
from file_preprocessor import download_youtube as dy
from vtt_manager import vtt_manager as vttm
from file_manager import file_manager as fm
import shutil
import os


class Pipeline:
    def __init__(self, lang):
        self.lang = lang
        self.data = None
        self.data_list = None
        self.ids = []
        self.manager = vttm.VTTManager()

    def download_videos(self):
        downloader = dy.YoutubeDownloader()
        self.ids = downloader.read_ids()
        downloader.download_videos()

    def pre_process(self):
        downloads_manager = fp.DownloadsManager()
        for id in self.ids:
            downloads_manager.remove_heading(id, self.lang)

    def process(self):
        self.data, self.data_list = self.manager.parse_vtt(self.ids, self.lang)
        # for id in self.ids:
        #     try:
        #         data = self.data_list[id]
        #         for d in data:
        #             print(d)
        #     except KeyError:
        #         continue

    def save_results(self):
        file_manager = fm.FileManager()

        for id in self.ids:
            file_manager.write_results_opening(id)
            file_manager.write_results_content(id, self.data_list)
            file_manager.write_end_file(id)
            self.delete_files(id)

        # for num, chunk in enumerate(self.data):
        #     file_manager.write_results_opening(self.ids[num])
        #     file_manager.write_results_content_data(self.ids[num], chunk)
        #     file_manager.write_end_file(self.ids[num])

    @staticmethod
    def delete_files(id):
        upper_path = 'resources/youtube_downloads'
        path = 'resources/youtube_downloads/{}'
        path = path.format(id)
        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.listdir(upper_path):
            shutil.rmtree(upper_path)


def main():
    pipeline = Pipeline('es')
    pipeline.download_videos()
    pipeline.pre_process()
    pipeline.process()
    pipeline.save_results()


if __name__ == '__main__':
    main()
