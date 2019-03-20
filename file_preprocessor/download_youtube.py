import os

videos_list = ("Yn5Hypn5Zxs", "4KzGdW3OwZM", "mt5E0eFRz6c", "ZJ0OblSyAFA", "tcaFRlyuq9s",
               "Gi4hBVELogA", "ZnEyo1krAjQ", "6bAob21suZc", "sZZx9WUG7l8", "-zB5mPADaFY")

download_command = "youtube-dl --output \"{path}\" --all-subs --write-auto-sub " \
                   "--extract-audio --audio-format mp3" \
                   "https://www.youtube.com/watch?v=${id}"

for id in videos_list:
    command = download_command.format(path='resources/${id}.%(ext)s')
    os.system(command)
