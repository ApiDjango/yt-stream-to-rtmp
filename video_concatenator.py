import os
import subprocess

# Путь к папке с видео файлами
path = "/path/to/videos/"

# Получаем список всех файлов в папке
files = os.listdir(path)

# Фильтруем только файлы с расширением .mp4
files = [f for f in files if f.endswith(".mp4")]

# Сортируем файлы в алфавитном порядке
files.sort()

# Создаем список с путями к файлам
paths = [os.path.join(path, f) for f in files]

# Используем ffmpeg для склеивания файлов
command = ["ffmpeg", "-i", "concat:" + "|".join(paths), "-c", "copy", "output.mp4"]
subprocess.call(command)
