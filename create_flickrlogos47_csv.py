# -*- coding: utf-8 -*-
"""
Python script to create a csv file with the annotations of the flickrlogos47 dataset
to train and test it with the OS2D model.

@author: Julio César Ruiz Calle
"""
import glob
import os
import csv

train_1 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\train\000000\*.txt')

train_2 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\train\000001\*.txt')

train_3 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\train\000002\*.txt')

test_1 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\test\000000\*.txt')

test_2 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\test\000001\*.txt')

test_3 = glob.glob(r'C:\Users\crcj2\Desktop\Uni\GVIS\Datasets\Flickrlogos47\test\000002\*.txt')

files = train_1 + train_2 + train_3 + test_1 + test_2 + test_3
#print(files)

raw_info = []
for file in files:
    subdirectories = file.split('\\')
    file_name = os.path.basename(file)
    dot_index = file_name.index('.')
    file_id = file_name[0:dot_index]
    
    with open(file, 'r') as infile:
        for line in infile:
            raw_info.append(file_id + " " + subdirectories[-3] + " " + line)
    
    infile.close()    

info = []
for i in raw_info:
        removed_line_break = i.replace('\n', '')
        info.append(removed_line_break)
        

counter = 0
with open('flickrlogos47.csv', mode='w', newline="") as flickrlogos47_file:
    flickrlogos47_writer = csv.writer(flickrlogos47_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    flickrlogos47_writer.writerow(['gtbboxid', 'classid', 'image_id', 'lx', 'rx', 'ty', 'by', 'difficult', 'split'])
    for i in info:
        gtbboxid = counter
        classid = i.split(' ')[6]    
        image_id = i.split(' ')[0]
        lx = "{0:.4f}".format(int(i.split(' ')[2]) / 1000)
        rx = "{0:.4f}".format(int(i.split(' ')[3]) / 1000)
        ty = "{0:.4f}".format(int(i.split(' ')[4]) / 1000)
        by = "{0:.4f}".format(int(i.split(' ')[5]) / 1000)
        difficult = i.split(' ')[9]
        splitted = i.split(' ')[1]
        counter+=1
        flickrlogos47_writer.writerow([gtbboxid, classid, image_id, lx, rx, ty, by, difficult, splitted])
  