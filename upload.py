
from InstagramAPI import InstagramAPI
from secrets import user, pwd


api = InstagramAPI(user, pwd)
api.login()  # login

# upload picture
photo_path = './new_post.jpg'
caption = "text message"
api.uploadPhoto(photo=photo_path, caption=caption)
