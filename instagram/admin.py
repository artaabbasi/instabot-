import json
from django.contrib import admin
from .models import *
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import X6_IGNORED, get_display
import pika




@admin.action(description='Mark selected stories as published')
def publish_story(modeladmin, request, queryset):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    media = queryset.all()
    medias = []
    for m in media:
        medias.append(m.id)
        template = m.template.path
        photo1 = m.photoup.path
        photo2= m.photobut.path
        x = m.text1
        type = m.type

        x = x.strip()
        y = ""
        i=0
        n = 30
        while True:
            if i+n > len(x):
                y = y + x[i:i+n]
                break
            if x[i+n] == " ":
                y = y + x[i:i+n] + "\n"
                i = i+n+1
            else:
                for j in range(n):
                    if x[i+n-j]==" ":
                        y = y + x[i:i+n-j] + "\n"
                        i = i+n-j+1
                        break

        my_image = Image.open(f"{template}")
        pastedi=Image.open(f"{photo1}")
        logo=Image.open(f"{photo2}")

        if type == 1 :

            top_pos = (720, 50)
            but_pos = (50, 1650)
            text_pos = (200,550)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 60

        if type == 2 :

            top_pos = (720, 50)
            but_pos = (50, 1650)
            text_pos = (200,600)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 50

        if type == 3 :

            top_pos = (720, 50)
            but_pos = (50, 50)
            text_pos = (300,1000)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 50

        if type == 4 :
        
            top_pos = (385, 150)
            but_pos = (460, 1600)
            text_pos = (200,700)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 55

        if type == 5 :

            top_pos = (385, 100)
            but_pos = (10600, -3)
            text_pos = (250,350)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 45

        if type == 6 :

            top_pos = (50, 50)
            but_pos = (850, 1600)
            text_pos = (200,250)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 55

        if type == 7 :

            top_pos = (384, 1465)
            but_pos = (850, 16000)
            text_pos = (240,250)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 50

        if type == 8 :

            top_pos = (40, 1232)
            but_pos = (850, 16000)
            text_pos = (240,460)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 50

        if type == 9 :

            top_pos = (385, 100)
            but_pos = (800, 1650)
            text_pos = (240,350)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 50

        if type == 10 :

            top_pos = (385, 1400)
            but_pos = (800, 16000)
            text_pos = (200,200)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 40

        if type == 11 :

            top_pos = (50, 1750)
            but_pos = (800, 16000)
            text_pos = (250,200)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 55

        if type == 12 :

            top_pos = (50, 1750)
            but_pos = (800, 16000)
            text_pos = (250,80)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 55

        if type == 13 :

            top_pos = (385, 760)
            but_pos = (455, 300)
            text_pos = (300,955)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 45

        if type == 14 :

            top_pos = (755, 10)
            but_pos = (30, 1650)
            text_pos = (450,400)
            resized_im =  pastedi.resize((312, 136))
            resize_lg = logo.resize((164, 238))
            font_size = 45
        
        title_font = ImageFont.truetype('dana/Dana-FaNum-Medium.ttf', font_size)

        title_text = f"{y}"
        reshaped_text = arabic_reshaper.reshape(title_text) 
        bidi_text = get_display(reshaped_text)  

        image_editable = ImageDraw.Draw(my_image)

        image_editable.text(text_pos, title_text ,(0,0,0), font=title_font ,align='right', spacing=50 )

        # draw = ImageDraw.Draw(my_image)
        # draw.text((250,70), (0,0,0), font=title_font)

        copyi=my_image.copy()
        pastii=pastedi.copy()
        logoi= logo.copy()

        copyi.paste(resized_im ,top_pos)
        copyi.paste(resize_lg , but_pos) 
        copyi.save(f"story/{m.id}.jpg")
        accounts = InstagramAccounts.objects.all()
        for account in accounts:
            auth = {
                "username": account.username,
                "password": account.password,
            }
            value = {
                "auth": auth,
                "medias": medias
            }
            value  = json.dumps(value)
            hdr ={"task":"sendstory"}
            channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()

@admin.action(description='Mark selected posts as published')
def publish_post(modeladmin, request, queryset):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    media = queryset.all()
    for m in media:
        template = m.template.path
        photo1 = m.photoup.path
        photo2= m.photobut.path
        x = m.text1
        type = m.type

        x = x.strip()
        y = ""
        i=0
        n = 30
        while True:
            if i+n > len(x):
                y = y + x[i:i+n]
                break
            if x[i+n] == " ":
                y = y + x[i:i+n] + "\n"
                i = i+n+1
            else:
                for j in range(n):
                    if x[i+n-j]==" ":
                        y = y + x[i:i+n-j] + "\n"
                        i = i+n-j+1
                        break

        my_image = Image.open(f"{template}")
        pastedi=Image.open(f"{photo1}")
        logo=Image.open(f"{photo2}")

        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        title_font = ImageFont.truetype('dana/Dana-FaNum-Medium.ttf', 40)

        title_text = f"{y}"
        reshaped_text = arabic_reshaper.reshape(title_text) 
        bidi_text = get_display(reshaped_text)  

        image_editable = ImageDraw.Draw(my_image)

        image_editable.text((350,400), title_text ,(0,0,0), font=title_font ,align='right', spacing=50 )

        # draw = ImageDraw.Draw(my_image)
        # draw.text((250,70), (0,0,0), font=title_font)

        copyi=my_image.copy()
        pastii=pastedi.copy()
        logoi= logo.copy()

        copyi.paste(resized_im ,(600, 200))
        copyi.paste(resize_lg ,(165, 1480)) 
        copyi.save(f"post/{m.id}.jpg")
    
        accounts = InstagramAccounts.objects.all()
        for account in accounts:
            auth = {
                "username": account.username,
                "password": account.password,
            }
            value = {
                "auth": auth,
                "media": m.id,
                "caption":m.caption,
            }
            value  = json.dumps(value)
            hdr ={"task":"sendpost"}
            channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()


class PostAdmin(admin.ModelAdmin):
    actions = [publish_post]

class StoryAdmin(admin.ModelAdmin):
    actions = [publish_story]

admin.site.register(InstagramAccounts)
admin.site.register(ForIntractUsers)
admin.site.register(Comments)

admin.site.register(createstory, StoryAdmin)
admin.site.register(createpost, PostAdmin)

