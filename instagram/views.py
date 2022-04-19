from code import interact
import json
from venv import main
from . import serialaizers, models
from rest_framework import response, generics, status, decorators, permissions as perms
import pika

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
            "media": medias
        }
        value  = json.dumps(value)
        hdr ={"task":"sendstory"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})

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


@decorators.api_view(['POST'])
def like_by_locations(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'intract':data.get('interact_setup', None)}
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


@decorators.api_view(['POST'])
def like_by_tags(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'intract':data.get('interact_setup', None)}
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



@decorators.api_view(['POST'])
def like_by_locations(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'intract':data.get('interact_setup', None)}
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
    interact_setup = {'intract':data.get('interact_setup', None)}
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
        hdr ={"task":"interact_user_following"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



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
    interact_setup = {'intract':data.get('interact_setup', None)}
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
        hdr ={"task":"interact_user_likers"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



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
    interact_setup = {'intract':data.get('interact_setup', None)}
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
        hdr ={"task":"interact_user_followers"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})



@decorators.api_view(['POST'])
def interact_by_comments(request):
    data = request.data
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='insta')
    accounts = models.InstagramAccounts.objects.filter(pk__in=data.get('accounts'))
    if data.get('follow_setup', None) is None or data.get('like_setup', None) is None:
        return response.Response({"messages":"you should send one of like or follow"})
    main_setup = {'main':data.get('main_setup', None)}
    interact_setup = {'intract':data.get('interact_setup', None)}
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
        hdr ={"task":"interact_by_comments"}
        channel.basic_publish(exchange='', routing_key='insta', body=value, properties=pika.BasicProperties(headers=hdr))
    connection.close()
    return response.Response({"messages":"done.."})
