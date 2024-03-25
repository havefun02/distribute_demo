import pika

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'order_process'

def process_order(ch, method, properties, body):
    # Mock inventory update logic
    order_data = body.decode('utf-8')
    print("Received order for inventory update:", order_data)
    # Perform inventory update logic here
    # For demonstration, let's just print the order data
    print("Inventory updated for order:", order_data)

def consume_orders():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=process_order, auto_ack=True)
    print('Inventory service is waiting for orders...')
    channel.start_consuming()

if __name__ == '__main__':
    consume_orders()
