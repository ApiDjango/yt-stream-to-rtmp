import subprocess

url = ""
rtmp_url = "rtmp://vsu.mycdn.me/input"
key = ""

# получаем поток из youtube
proc = subprocess.Popen(['yt-dlp','-f','bestvideo+bestaudio','-o','output.mp4',url], stdout=subprocess.PIPE)

# Дожидаемся завершения процесса yt-dlp
proc.wait()

# запускаем стрим
ffmpeg_command = f'ffmpeg -re -i output.mp4 -c:v libx264 -c:a aac -f flv "{rtmp_url}/{key}"'
subprocess.call(ffmpeg_command, shell=True)
