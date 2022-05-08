import json
from venv import main

from django.shortcuts import get_object_or_404
from . import serialaizers, models
from rest_framework import response, generics, status, decorators, permissions as perms
import pika
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import action
import random

@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.SendStorySerializer)
@decorators.api_view(['POST'])
def sendstory(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    medias = data.get('medias')
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
    return response.Response({"messages":"done.."})

@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.SendPostSerializer)
@decorators.api_view(['POST'])
def sendpost(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    media = data.get('media')
    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "auth": auth,
            "media": media,
            "caption":data.get('caption')
        }
        value  = json.dumps(value)
        hdr ={"task":"sendpost"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})

@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.LikeByLocations)
@decorators.api_view(['POST',])
def like_by_locations(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"like_by_locations"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})


@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.LikeByTags)
@decorators.api_view(['POST'])
def like_by_tags(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"like_by_tags"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})




@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.InteractByFollowing)
@decorators.api_view(['POST'])
def interact_user_following(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None or data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "users":users,

            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"interact_user_following"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.InteractByLikers)
@decorators.api_view(['POST'])
def interact_user_likers(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None or data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "users":users,

            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"interact_user_likers"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.InteractByFollowers)
@decorators.api_view(['POST'])
def interact_user_followers(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None or data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "users":users,
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"interact_user_followers"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.InteractByComments)
@decorators.api_view(['POST'])
def interact_by_comments(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None and data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "users":users,
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"interact_by_comments"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})

@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.InteractByUsers)
@decorators.api_view(['POST'])
def interact_by_users(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None and data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            "users":users,
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"interact_by_users"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})

@swagger_auto_schema(methods = ['post',],tags=['instagram'], request_body=serialaizers.LikeByFeed)
@decorators.api_view(['POST'])
def like_by_feed(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None and data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'interact':data.get('interact_setup', None)}
    comment_setup = {'comment':data.get('comment_setup', None)}
    comment_replies_setup = {'comment_replies':data.get('comment_replies_setup', None)}
    follow_setup = {'follow':data.get('follow_setup', None)}
    like_setup = {'like':data.get('like_setup', None)}
    # users = data.get('users', None)

    for account in accounts:
        auth = {
            "username": account.username,
            "password": account.password,
        }
        value = {
            # "users":users,
            "auth": auth,
        }
        value.update(interact_setup)
        value.update(comment_setup)
        value.update(comment_replies_setup)
        value.update(follow_setup)
        value.update(like_setup)
        value.update(main_setup)
        value  = json.dumps(value)
        hdr ={"task":"like_by_feed"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



@swagger_auto_schema(methods = ['get',],tags=['instagram'])
@decorators.api_view(['GET'])
def auto_intract(request):
    data = request
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = list(models.InstagramAccounts.objects.all())
    account = request.GET.get('account',  random.choice(accounts).id)
    users_table = models.ForIntractUsers.objects.all()
    users = data.GET.get('users', [random.choice(users_table).username])
    interact_setup = {'interact':json.loads(data.GET.get('interact_setup', '{"amount": 2,"randomize": true,"percentage": 50}'))}
    comments_table = models.Comments.objects.all()
    comments = [comm for comm in comments_table]
    comment_setup = {'comment': json.loads(data.GET.get('comment_setup', '{'+f'"enabled": true,"percentage": 20,"list": {comments}'+'}'))}
    comment_replies_setup = {'comment_replies':json.loads(data.GET.get('comment_replies_setup', "{"+f'"enabled": true,"percentage": 20,"list": {comments}'+"}"))}
    follow_setup = {'follow':json.loads(data.GET.get('follow_setup', '{"enabled": true,"percentage": 30}'))}
    like_setup = {'like':json.loads(data.GET.get('like_setup', '{"enabled": true,"percentage": 50}'))}

    # main_setup = {'main':data.get('main_setup', None)}

    auth = {
        "username": get_object_or_404(models.InstagramAccounts, pk=account).username,
        "password": get_object_or_404(models.InstagramAccounts, pk=account).password,
    }
    value = {
        "users":users,
        "auth": auth,
    }
    value.update(interact_setup)
    value.update(comment_setup)
    value.update(comment_replies_setup)
    value.update(follow_setup)
    value.update(like_setup)
    # value.update(main_setup)
    tasks  = ['interact_by_comments', "interact_user_following", "interact_user_likers", "interact_user_followers"]
    rand_task = random.randint(0, len(tasks)-1)
    if rand_task == 0:
        main_setup = {
            "randomize": True,
            "reply": True,
            "interact": True
        }
        value.update({'main':main_setup})
    elif rand_task == 1:
        main_setup = {
            "randomize": True,
            "amount": 10
        }
        value.update({'main':main_setup})
    elif rand_task == 2:
        main_setup = {
            "randomize": True,
            "posts_grab_amount": 5,
            "interact_likers_per_post": 10
        }
        value.update({'main':main_setup})
    elif rand_task == 3:
        main_setup = {
            "randomize": True,
            "amount": 10
        }
        value.update({'main':main_setup})
    value  = json.dumps(value)
    hdr ={"task":tasks[rand_task]}
    channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})