import os
import subprocess


img_new_width = '200'

converted_dir_name = 'Converted'
raw_dir_name = 'Source'

current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_converted_files_dir = os.path.join(current_dir, converted_dir_name)
path_to_raw_files_dir = os.path.join(current_dir, raw_dir_name)


def create_converted_files_dir():
    subprocess.run(['mkdir', '-p', converted_dir_name])


def get_filelist():
    filelist = []
    for file_name in os.listdir(path=path_to_raw_files_dir):
        if not file_name.startswith('.'):
            filelist.append(file_name)
    return filelist


def convert_img():
    process = subprocess.run(['sips', '--resampleWidth', img_new_width, '--out', path_to_converted_files_dir, img_name])
    if process.returncode == 0:
        print("converting —> done")
    else:
        print("can't convert")


create_converted_files_dir()

for file in get_filelist():
    img_name = os.path.join(path_to_raw_files_dir, file)
    convert_img()
