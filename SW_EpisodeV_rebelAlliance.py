import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import fileupload
import pandas as pd
import numpy as np
from PIL import Image
from pathlib import Path

def file_extract(file_name):
    data=open(file_name,encoding='utf-8')
    data=data.read().lower()
    file_contents = data.replace('\n', '')
    return file_contents

def dic_generation(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["not","get","on","the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no","in", "nor", "too", "very", "can", "will", "just"]
        

    string = ""
    string1=""
    wdcloud={}
    def get_key(value):
        for key, val in wdcloud.items():
            if val == value:
                return key
        print("Key not found")
    for ch in file_contents:
        if (ch not in punctuations):
            string+=ch
    string = string.lower()
    #print("This is STRING, ", string)
    list1 = string.split()
    for x in list1 :
        if x not in uninteresting_words:
            string1 = string1+" "+x
    #print("this is String1", string1)
    list2 = string1.split()
    for j in list2:
        if j not in wdcloud.keys():
            wdcloud[j] = 1
        else:
            wdcloud[j]+=1
    #print(wdcloud)
    #print(get_key(max(wdcloud.values())), " : ",max(wdcloud.values()))
    return wdcloud

def wordcloud_generate(image_name, wdcloud):
    cand_mask=np.array(Image.open(image_name))

    # this line will take all values greater than 3 and make them 255 (white)
    # if they are less than 3, they will be whatever value they are in the array
    cand_mask=np.where(cand_mask > 3, 255, cand_mask)


    cmap = mpl.cm.Oranges(np.linspace(0,1,20)) #['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd',
                                                #'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
    cmap = mpl.colors.ListedColormap(cmap[-10:,:-1]) 

    #create and generate our wordcloud object
    wordcloud = WordCloud(background_color='white',contour_color='black',max_words=500,mask=cand_mask,
                          colormap=cmap,contour_width=4).generate_from_frequencies(wdcloud)
    #plot
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return

file_contents = file_extract('SW_EpisodeV.txt')
wdcloud = dic_generation(file_contents)
wordcloud_generate('rebel alliance.png', wdcloud)

