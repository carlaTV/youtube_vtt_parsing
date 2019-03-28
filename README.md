# Parsing Youtube subtitles 

This project returns a list of a Youtube video's transcription along with each word's timestamps. It uses the Youtube video id as input.

```
In 
https://www.youtube.com/watch?v=-hyQDlgSMUs
the id of the video is -hyQDlgSMUs.
```

## How it works

Inputs: place the youtube identifiers of the videos you want to process in the file resources/ids_list.

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
