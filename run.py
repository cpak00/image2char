# -*- coding: utf -*-
from image2char import tool
from PIL import Image
import logging

img_path1 = 'input1.jpg'
img_path2 = 'image2char/input2.png'

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)

    img1 = img1.resize((600, int(600 * img1.size[1] / img1.size[0])), Image.ANTIALIAS)
    matrix = tool.to_chars(img1, density=0.7, scale=2, reversed=True)
    logging.info('matrix: %d, %d' % (len(matrix), len(matrix[0])))
    for i in range(len(matrix)):
        print(''.join(matrix[i]))

    char_list = '''█　'''
    scanner = tool.get_scanner(density=0.6, scale=1)
    scanner.scan(img2, reversed=True, char_list=char_list)
    scanner.print_result()
