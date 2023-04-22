import logging
import os
import sys
import argparse

from PIL import Image
from datetime import datetime
from sys import platform

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)

EXIF_DATETIME = 306

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


def adjust_creation_datetime_from_pictures_in_dir(directory):
    included_extensions = ['.jpg', '.jpeg']
    pictures = [file for file in os.listdir(directory)
                if any(file.endswith(ext) for ext in included_extensions)]

    for picture in pictures:
        image = Image.open(os.path.join(directory, picture))
        image_information = image.getexif()
        pic_datetime_str = image_information[EXIF_DATETIME]
        pic_datetime_obj = datetime.strptime(pic_datetime_str, '%Y:%m:%d %H:%M:%S')

        if platform == "darwin":  # macos
            formated_datetime = pic_datetime_obj.strftime('%m/%d/%Y %I:%M:%S %p')
            exitcode = os.system(
                f'SetFile -d "{formated_datetime}" -m "{formated_datetime}" "{os.path.join(directory, picture)}"')
            logger.info(f"adjusted: {os.path.join(directory, picture)}")

            if exitcode != 0:
                raise 'there was a problem executing updating the file time'


if __name__ == '__main__':
    args = parser.parse_args()
    selected_dir = os.getcwd() if not args.dir else args.dir
    logger.info(f"dir: {selected_dir}")

    adjust_creation_datetime_from_pictures_in_dir(selected_dir)
