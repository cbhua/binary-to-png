import os
from src.bin2png import bin2png


for root, dirs, files in os.walk('./bin'):
    for file in files:
        if not file.endswith('.bin'):
            continue
        bin2png(os.path.join(root, file), './png')
    
    print('DONE')