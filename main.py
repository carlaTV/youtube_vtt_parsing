from file_preprocessor import files_preprocessing as fp


class Pipeline:
    def process(self):
        downloader = fp.DownloadsManager()
        downloader.move_videos_to_dir()


def main():
    pipeline = Pipeline()
    pipeline.process()


if __name__ == '__main__':
    main()
