from time import sleep
from tqdm import tqdm

import os
os.listdir('./')

print(os.listdir('./'))


for i in tqdm(range(300)):
    sleep(0.01)
    print(i)
