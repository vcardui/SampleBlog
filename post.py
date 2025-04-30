# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: January 9th, 2025
# | Last update..: March 11th, 2025
# | WhatIs.......: Cardui Web Development Post - Class
# +----------------------------------------------------------------------------+

# ------------------------- Libraries -------------------------
import requests

# -------------------------- Class ----------------------------
class Post:
    def __init__(self, id):
        self.id = int(id) - 1

        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        blog_response = requests.get(blog_url)
        all_posts = blog_response.json()

        self.title = all_posts[self.id]["title"]
        self.subtitle = all_posts[self.id]["subtitle"]
        self.body = all_posts[self.id]["body"]
        self.image = "post-bg" + (str("-" + id) if id is not None else "") + ".jpg"

        # print(f"self.title = {self.title}")
        # print(f"self.subtitle = {self.subtitle}")
        # print(f"self.body = {self.body}")
