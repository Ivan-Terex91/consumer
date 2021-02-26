import random
import pika
import time
import os

name_queue = os.environ["name_queue"]

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(name_queue, durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(random.randint(3, 6))  # для очереди 1
    # time.sleep(random.randint(4, 8))  # для очереди 2
    # time.sleep(random.randint(1, 4))  # для очереди 3
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(on_message_callback=callback, queue=name_queue)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
