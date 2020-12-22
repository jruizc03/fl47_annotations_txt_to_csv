# -*- coding: utf-8 -*-
"""
Script that converts all the multiple annotation files of the flickrlogos47 dataset
to a single .txt file with the format: "imgfilename classname subset x1 y1 x2 y2" that
is the format that the method DeepLogo uses.

@author: Julio César Ruiz Calle
"""

import glob

testset_images = []
testset_annots = []
imagex1 = []
imagey1 = []
imagex2 = []
imagey2 = []
imageclassnames = []
imagefilenames = []

def get_image_class(ide:int):
    names = ['HP', 'adidas_symbol', 'adidas_text', 'aldi', 'apple', 'becks_symbol', 'becks_text', 'bmw', 'carlsberg_symbol', 'carlsberg_text', 'chimay_symbol', 'chimay_text', 'cocacola', 'corona_symbol', 'corona_text', 'dhl', 'erdinger_symbol', 'erdinger_text', 'esso_symbol', 'esso_text', 'fedex', 'ferrari', 'ford', 'fosters_symbol', 'fosters_text', 'google', 'guinness_symbol', 'guinness_text', 'heineken', 'milka', 'nvidia_symbol', 'nvidia_text', 'paulaner_symbol', 'paulaner_text', 'pepsi_symbol', 'pepsi_text', 'rittersport', 'shell', 'singha_symbol', 'singha_text', 'starbucks', 'stellaartois_symbol', 'stellaartois_text', 'texaco', 'tsingtao_symbol', 'tsingtao_text', 'ups']
    return names[ide]

with open('/home/julio/wdir/datasets/flickrlogos47/FlickrLogos_47/test/filelist.txt', 'r') as infile:
    for line in infile:
        clean_line = line.replace('\n', '')
        clean_line = clean_line.lstrip('.')
        testset_images.append('/home/julio/wdir/datasets/flickrlogos47/FlickrLogos_47/test/'+clean_line)

#Store the location of the image files
for imagefile in testset_images:
    temp = imagefile.replace('png', 'gt_data.txt')
    testset_annots.append(temp)

print('Test number of image files = ' + str(len(testset_images)))
print('Test number of annotation files = ' + str(len(testset_annots)))
#Retrieve the x1 y1 x2 y2 for each of the annotation files
for i in range(len(testset_annots)):
    with open(testset_annots[i], 'r') as infile:
        for line in infile:
            numbers = line.split(' ')
            x1, y1, x2, y2 = numbers[:4]
            imagex1.append(str(x1))
            imagey1.append(str(y1))
            imagex2.append(str(x2))
            imagey2.append(str(y2))
            classname = get_image_class(int(numbers[4]))
            imageclassnames.append(classname)
            subdirectories = testset_annots[i].split('/')
            #imageclassnames.append(subdirectories[-2].capitalize())
            imagefilename = subdirectories[-1].rstrip('.gt_data.txt')
            imagefilename = imagefilename + '.png'
            imagefilenames.append(imagefilename)

print('Test number of annotations = ' + str(len(imagefilenames)))
#Write the lines in the text file
for i in range(len(imagefilenames)):
    with open('flickr_logos_47_dataset_test_set_annotation.txt', 'a') as infile:
        infile.write(imagefilenames[i]+' '+imageclassnames[i]+' '+'1'+' '+imagex1[i]+' '+imagey1[i]+' '+imagex2[i]+' '+imagey2[i]+'\n')
