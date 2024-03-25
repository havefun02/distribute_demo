import pika
import json
import time

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE_SHIPPING = 'shipping'

def process_order(ch, method, properties, body):
    order_data = json.loads(body.decode('utf-8'))
    print("Received order for shipping:", order_data)
    # Simulate shipping process
    simulate_shipping(order_data)
    print("Shipping completed for order:", order_data)

def simulate_shipping(order_data):
    # Simulate shipping process
    print("Simulating shipping process for order:", order_data)
    # Sleep to simulate shipping time
    time.sleep(3)  # Simulating shipping taking 3 seconds

def consume_shipping_orders():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE_SHIPPING)
    channel.basic_consume(queue=RABBITMQ_QUEUE_SHIPPING, on_message_callback=process_order, auto_ack=True)
    print('Shipping service is waiting for orders...')
    channel.start_consuming()

if __name__ == '__main__':
    consume_shipping_orders()
