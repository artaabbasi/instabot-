import json
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='insta')

body = {
    "auth":{
        "username":"novatest822",
        "password":"avangp23",

    },
    "users":['cristiano'],
    "like":{
        "enabled": True,
        "percentage":100
    },
    "intract":{
        "amount":10,
        "percentage":100,
        "randomize": True
    },
    "follow":{
        "enabled": True,
        "percentage":100
    },
}
channel.basic_publish(exchange='', routing_key='insta', body=json.dumps(body), properties=pika.BasicProperties(headers={"message":"interact_user_following"}))

connection.close()