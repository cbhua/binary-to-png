import os
import re
import binascii


def bin2png(file_path: str, save_path: str):
    ''' Bin to PNG Tool

    A tool for extracting PNGs from bin file. 

    Args: 
        file_path <str>: the file path of bin to be extracted, e.g. '/folder/file.bin'
        save_path <str>: the folder path of PNG to be saved, e.g. '/folder/'
    '''
    counter = 0
    png_pattern = re.compile(r'89504E47.*?49454E44AE426082', re.IGNORECASE)
    file_name = file_path.split('/')[-1][:-4]
    save_path = os.path.join(save_path, file_name)
    
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    with open(file_path, 'rb') as file:
        for match in png_pattern.findall(str(binascii.hexlify(file.read()))):
            with open('{}/{}.png'.format(save_path, counter), 'wb+') as image:
                image.write(binascii.unhexlify(match))
                counter += 1
    
    if counter != 0:
        print('Successfully extra {} PNGs from file {}'.format(counter, file_name))
    else:
        print('Failed to find PNGs in file {}'.format(file_name))