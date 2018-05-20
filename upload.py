
# coding: utf-8

# In[1]:


import os
import re
from InstagramAPI import InstagramAPI
from secrets import user, pwd  # add your own login information!


# In[33]:


# move the first image from /queued to /upload
file_list = os.listdir('./queued')
for f in file_list:
    if f.endswith('.jpg'):  # avoid the pesky .DS_store file
        os.rename(f"./queued/{f}", f"./upload/{f}")
        break  # only the first JPG file shall be moved!


# In[9]:


# '@name' tags work '\n' don't do anything


# In[19]:


comments = {
    './upload/new_IMG_20170906_170908.jpg': "",
    './upload/new_IMG_20170906_170743.jpg': "",
    './upload/new_IMG_20171012_153515.jpg': "",
    './upload/new_IMG_20171014_104310.jpg': "",
    './upload/new_IMG_20171014_134211.jpg': "",
    './upload/new_IMG_20171017_183657.jpg': "",
    './upload/new_IMG_20171017_183803.jpg': "",
    './upload/new_IMG_20171017_184016.jpg': "",
    './upload/new_IMG_20171017_184134.jpg': "",
    './upload/new_IMG_20171017_184607.jpg': "",
    './upload/new_IMG_20171017_184927.jpg': "",
    './upload/new_IMG_20171017_185234.jpg': "",
    './upload/new_IMG_20171025_173436.jpg': "",
    './upload/new_IMG_20171025_181645.jpg': "",
    './upload/new_IMG_20171108_095434.jpg': "",
}


# In[10]:


tag_string = " . . . . . . . . . . . . . . . . . . . #learntocode #codecamp #bootcamp #codingnomads #softwareengineer #softwareengineering #softwaredevelopment #softwaredeveloper #learntocodeabroad #studyabroad #python #pythoncode #digitalnomad #worldtravel #travel #career #careertraining #computerprogramming #focus #webdeveloper #backenddeveloper"


# In[3]:


api = InstagramAPI(user, pwd)
api.login()  # login


# In[20]:


# get a list of current images queued for upload
img_list = list()

for root, dirs, files in os.walk('./upload'):
    for name in files:
        if name.endswith('.jpg'):  # avoid .DS_store etc
            img_list.append(os.path.join(root, name))
img_list


# In[21]:


# creating a regex pattern to grab the filename from the photo_path
p = re.compile(r'(\/new)\S+')  # match the image name from the last part of the file path


# In[26]:


for photo_path in img_list:
    if photo_path in comments:
        caption = comments[photo_path]
        print(photo_path, caption)
        api.uploadPhoto(photo=photo_path, caption=caption)
        filename = re.search(p, s)[0]  # search all over the string and return the matched string part
        os.rename(photo_path, f"./done{filename}")  # move the file from /upload to /done

