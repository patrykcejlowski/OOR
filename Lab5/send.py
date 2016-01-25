import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost')) #laczymy z lokalhostem lub ip
channel = connection.channel()

channel.queue_declare(queue='hello') #kolejka do ktorej wysylamy wiadomosc

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!")

connection.close()