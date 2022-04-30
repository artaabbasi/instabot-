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
    "media":9

}
channel.basic_publish(exchange='', routing_key='insta', body=json.dumps(body), properties=pika.BasicProperties(headers={"message":"sendstory"}))

connection.close()