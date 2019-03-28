# Parsing Youtube subtitles 

This project returns a list of a Youtube video's transcription along with each word's timestamps. It uses the Youtube video id as input.

```
In 
https://www.youtube.com/watch?v=-hyQDlgSMUs
the id of the video is -hyQDlgSMUs.
```

### System
The project only runs on Linux. To adapt it to other operating systems, modify the download_command in
[download_youtube.py](file_preprocessor/download_youtube.py).

### Requirements
To download the videos, install ffmpeg in your computer. You can find further informations on how to do it [here](https://www.ffmpeg.org/download.html).

For the processing, you need to install os and regex.
```
pip install os
pip install regex
```

### How to use it

You only need to clone the project and run the main file.

Inputs: place the youtube identifiers of the videos you want to process in the file resources/ids_list.
For example:
```
"Yn5Hypn5Zxs"
"4KzGdW3OwZM"
"mt5E0eFRz6c"
"ZJ0OblSyAFA"
```

By running the main file, the code will download the videos in the list that have not been downloaded yet and process their subtitles.

Output: a list of each word in the transcription along with its timestamp. This list is stored in a dictionary where the keys are the videos ids. Each video's output is stored in resources/word_timestamps.

This is an example of an output:

```
{ 
 "4KzGdW3OwZM": {
	 "el" : "['00:00:07.220 ', '00:00:07.819']",
	 " mediterráneo" : "['00:00:07.819', '00:00:08.599']",
	 " un" : "['00:00:08.599', '00:00:09.139']",
	 " sistema" : "['00:00:09.139', '00:00:09.740']",
	 " vulnerable" : "['00:00:09.139', '00:00:09.740']",
	 "en" : "['00:00:13.530 ', '00:00:14.099']",
   ...
    "la" : "['00:05:43.550 ', '00:05:43.670']",
	 " innovación" : "['00:05:43.550 ' '00:05:43.670']"
}}
```

## Authors

* **Carla Ten Ventura** - *Initial work* - [carlaTV](https://github.com/carlaTV)