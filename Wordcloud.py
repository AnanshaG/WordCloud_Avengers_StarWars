import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import pandas as pd
import numpy as np

from pathlib import Path
data=open('SW_EpisodeIV.txt',encoding='utf-8')
data=data.read().lower()
file_contents = data.replace('\n', '')
#print(data)

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
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(wdcloud)

myimage = cloud.to_array()
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


