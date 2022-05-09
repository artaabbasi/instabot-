import json
import os
import random
import time
import pika
from instapy import InstaPy , smart_run


def interact_by_comments(body):
    data = json.loads(body)


    try:
        users = data['users']
    except:
        print("Should send users!")
        return None
    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)

    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 
        if main_setup is not None:
            session.interact_by_comments(
                users, 
                randomize= bool(main_setup.get('enabled')) if main_setup.get('enabled',None) is not None else True if main_setup is not None else None,
                reply=bool(main_setup.get('reply')) if main_setup.get('reply',None) is not None else False if main_setup is not None else None,
                interact= bool(main_setup.get('interact')) if main_setup.get('interact',None) is not None else False if main_setup is not None else None,
            )
        else:
            session.interact_by_comments(
                    users,
            )




def interact_user_followers(body):
    data = json.loads(body)

    try:
        users = data['users']
    except:
        print("Should send users!")
        return None
    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 
        if main_setup is not None:
            session.interact_user_followers(
                users, 
                randomize= bool(main_setup.get('enabled')) if main_setup.get('enabled',None) is not None else True if main_setup is not None else None,
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 10 if main_setup is not None else None,  
            )
        else:
            session.interact_user_followers(
                users,
            )



def interact_user_likers(body):
    data = json.loads(body)

    try:
        users = data['users']
    except:
        print("Should send users!")
        return None
    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 
        if main_setup is not None:
            session.interact_user_followers(
                users, 
                randomize= bool(main_setup.get('enabled')) if main_setup.get('enabled',None) is not None else True if main_setup is not None else None,
                posts_grab_amount= int(main_setup.get('posts_grab_amount')) if main_setup.get('posts_grab_amount',None) is not None else 3 if main_setup is not None else None,
                interact_likers_per_post= int(main_setup.get('interact_likers_per_post')) if main_setup.get('interact_likers_per_post',None) is not None else 3 if main_setup is not None else None,
            )
        else:
            session.interact_user_followers(
                users, 
            )


def interact_user_following(body):
    data = json.loads(body)

    try:
        users = data['users']
    except:
        print("Should send users!")
        return None
    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 
        if main_setup is not None:
                session.interact_user_following(
                users, 
                randomize= bool(main_setup.get('enabled')) if main_setup.get('enabled',None) is not None else True ,
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 10 ,   
            )
        else:
            session.interact_user_following(
                users,
            )


def interact_by_users(body):
    data = json.loads(body)

    try:
        users = data['users']
    except:
        print("Should send users!")
        return None
    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 
        if main_setup is not None:
                session.interact_by_users(
                users, 
                randomize= bool(main_setup.get('enabled')) if main_setup.get('enabled',None) is not None else True ,
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 10 ,   
            )
        else:
            session.interact_by_users(
                users,
            )

def like_by_tags(body):
    data = json.loads(body)


    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 

        main_setup.update({'use_random_tags':True}) if main_setup.get('tags',None) is None else None
        if main_setup is not None:
                session.like_by_tags(
                tags = main_setup.get('tags') if main_setup.get('tags',None) is not None else [], 
                use_random_tags= bool(main_setup.get('use_random_tags')) if main_setup.get('use_random_tags',None) is not None else False ,
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 20 ,   
                skip_top_posts = bool(main_setup.get('skip_top_posts')) if main_setup.get('skip_top_posts',None) is not None else True,
                use_smart_hashtags = bool(main_setup.get('use_smart_hashtags')) if main_setup.get('use_smart_hashtags',None) is not None else False,
                use_smart_location_hashtags = bool(main_setup.get('use_smart_location_hashtags')) if main_setup.get('use_smart_location_hashtags',None) is not None else False,
                interact = bool(main_setup.get('interact')) if main_setup.get('interact',None) is not None else False,
                randomize= bool(main_setup.get('randomize')) if main_setup.get('randomize',None) is not None else True ,
            )
        else:
            session.like_by_tags()


def like_by_locations(body):
    data = json.loads(body)


    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 

        if main_setup is not None:
                session.like_by_locations(
                locations = main_setup.get('locations') if main_setup.get('locations',None) is not None else [], 
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 20 ,   
                skip_top_posts = bool(main_setup.get('skip_top_posts')) if main_setup.get('skip_top_posts',None) is not None else True,
                randomize= bool(main_setup.get('randomize')) if main_setup.get('randomize',None) is not None else True ,
            )
        else:
            session.like_by_locations()


def like_by_feed(body):
    data = json.loads(body)


    main_setup = data.get('main', None)
    interact_setup = data.get('interact', None)
    comment_setup = data.get('comment', None)
    comment_replies_setup = data.get('comment_replies', None)
    follow_setup = data.get('follow', None)
    like_setup = data.get('like', None)
    
    try:
        session = InstaPy(username=data['auth']['username'], password=data['auth']['password'])
        session.login()
    except:
        print("Should send auth!")
        return None
    with  smart_run(session):
        session.set_user_interact(
            amount= int(interact_setup.get('amount')) if interact_setup.get('amount',None) is not None else 10,
            randomize= bool(interact_setup.get('randomize')) if interact_setup.get('randomize',None) is not None else True, 
            percentage= int(interact_setup.get('percentage')) if interact_setup.get('percentage',None) is not None else 100,
            ) if interact_setup is not None else None

        session.set_do_follow(
            enabled= bool(follow_setup.get('enabled')) if follow_setup.get('enabled',None) is not None else False,
            percentage= int(follow_setup.get('percentage')) if follow_setup.get('percentage',None) is not None else 100,
            ) if follow_setup is not None else None

        (
            session.set_comments(comment_setup.get('list')) if comment_setup.get('list', None) is not None else None,
            session.set_do_comment(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 50,
            )
        ) if comment_setup is not None else None

        session.set_do_like(
            enabled= bool(like_setup.get('enabled')) if like_setup.get('enabled',None) is not None else False,
            percentage= int(like_setup.get('percentage')) if like_setup.get('percentage',None) is not None else 100,
        ) if like_setup is not None else None

        (
            session.set_comment_replies(comment_replies_setup.get('list')) if comment_replies_setup.get('list', None) is not None else None,
            session.set_do_reply_to_comments(
                enabled= bool(comment_setup.get('enabled')) if comment_setup.get('enabled',None) is not None else False,
                percentage= int(comment_setup.get('percentage')) if comment_setup.get('percentage',None) is not None else 20,
            )
        )  if comment_replies_setup is not None else None 

        if main_setup is not None:
                session.like_by_feed(
                amount= int(main_setup.get('amount')) if main_setup.get('amount',None) is not None else 20 ,   
                unfollow = bool(main_setup.get('unfollow')) if main_setup.get('unfollow',None) is not None else False,
                randomize= bool(main_setup.get('randomize')) if main_setup.get('randomize',None) is not None else True ,
                interact= bool(main_setup.get('interact')) if main_setup.get('interact',None) is not None else False ,
            )
        else:
            pass


def sendstory(body):
    data = json.loads(body)

    path = f"story"

    try:
        username=data['auth']['username']
        password=data['auth']['password']
    except:
        print("Should send auth!")
        return None
    try:
        for media in data["medias"]:
            name = str(media)
            jpg_to_ = path + "/" + name + ".jpg"
            print(jpg_to_)
            try:
                with open(jpg_to_, "r") as f:
                    print("founded!")
                    os.system(f'java -jar instagram.jar {username} {password} {jpg_to_}')
                    time.sleep(random.randint(5,20))
            except:
                print("not found!")
    except:
        print("Should send media!")
    return None


def sendpost(body):
    data = json.loads(body)

    path = f"post"

    try:
        username=data['auth']['username']
        password=data['auth']['password']
    except:
        print("Should send auth!")
        return None
    try:
        name = str(data["media"])
        jpg_to_ = path + "/" + name + ".jpg"
        print(jpg_to_)
        try:
            with open(jpg_to_, "r") as f:
                print("founded!")
                os.system(f'java -jar instagram.jar {username} {password} {jpg_to_} "{data.get("caption", "Hi")}"')
        except:
            print("not found!")
    except:
        print("Should send media!")
    return None




























connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='insta')

def callback(ch, method, properties, body):
    task = properties.headers.get("task")
    exec(f"{task}(body)")

channel.basic_consume(queue='insta', on_message_callback=callback, auto_ack=True)

channel.start_consuming()