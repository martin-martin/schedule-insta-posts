
# coding: utf-8

# In[6]:


import os
import sys
import numpy
from PIL import Image


# ## Create white squared background
# 
# Converts a JPG image of variable size into a square image that can be uploaded to instagram.
# It achieves that by adapting the size to the longest size of the input image and adding a white square as background.
# 
# Currently takes JPG images from `/pic` and saves the edited version to `/queued`.

# In[7]:


get_ipython().system(' pwd')


# In[8]:


def convert_square(photo_path, name):
    # use a white square image as background canvas
    background = Image.open("./pics/white.png")
    foreground = Image.open(photo_path).convert("RGBA")
    # set the size equal to the larger side of the input image
    # to receive the largest possible image
    width = foreground.size[0]
    height = foreground.size[1]
    large_side = max(foreground.size)
    resized_background = background.resize((large_side, large_side))
    # center the foreground image on the white background
    x_pos = (large_side - width) // 2
    y_pos = (large_side - height) // 2    
    resized_background.paste(foreground, (x_pos, y_pos), foreground)
    # convert because cannot save RGBA of the white square as JPG
    final_image = resized_background.convert("RGB")
    final_image.save(f"./queued/new_{name}", quality=90)


# In[10]:


for root, dirs, files in os.walk('./pics'):
    for name in files:
        if name.endswith('.jpg'):  # avoid .DS_store and the background white.png
            convert_square(os.path.join(root, name), name)

