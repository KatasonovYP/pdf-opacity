from pdf2image import convert_from_path
from PIL import Image
import math
import os


def create_file(opacity, filename):
    result_filename = f'output/{filename[:-4]}/{filename[:-4]}-opacity-{opacity}.pdf'
    images = convert_from_path('input/' + filename, 300)
    pages = []
    page_image_filename = f'{result_filename[:-4]}.png'
    for image in images:
        image.save(page_image_filename)
        page = opacity_page(page_image_filename, opacity)
        pages.append(page)
    os.remove(page_image_filename)
    pages[0].save(
        result_filename, 
        'PDF', 
        resolution=100.0, 
        save_all=True, 
        append_images=pages[1:]
    )


def opacity_page(page_image_filename, opacity):
    with Image.open(page_image_filename) as rgba2:
        rgba2.putalpha(get_opacity_value(opacity))  # Half alpha; alpha argument must be an int
        rgb2 = Image.new('RGB', rgba2.size, (255, 255, 255))  # white background
        rgb2.paste(rgba2, mask=rgba2.split()[3])
        return rgb2


def get_opacity_value(percents):
    if (percents < 0 or percents > 100):
        raise ValueError('wrong opacity. Set value from 0 to 100')
    return math.ceil(255 / 100 * percents)


def create_folder(filename):
    if not os.path.isdir('output/' + filename[:-4]):
        os.mkdir('output/' + filename[:-4])