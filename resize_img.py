
# coding: utf-8

# In[1]:


import sys
import numpy
from PIL import Image


# In[56]:


photo_path = './CN_prof_pic.jpg'

background = Image.open("white.png")
foreground = Image.open(photo_path).convert("RGBA")
#background.save("white.jpg", quality=95, format="jpeg")
#bg = Image.new("RGB", background.size, (255,255,255))
#bg.save("white.jpg", quality=95)


# In[57]:


width = foreground.size[0]
height = foreground.size[1]

large_side = max(foreground.size)


# In[58]:


resized_background = background.resize((large_side, large_side))

x_pos = (large_side - width) // 2
y_pos = (large_side - height) // 2

resized_background.paste(foreground, (x_pos, y_pos), foreground)
final_image = resized_background.convert("RGB")
final_image.save("new_post.jpg", quality=90)

