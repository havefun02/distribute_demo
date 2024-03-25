from flask import Flask, request, jsonify
import pika

app = Flask(__name__)
# RabbitMQ connection parameters
RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'order_process'

def forward_request_to_message_broker(request_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=request_data)
    print("Request sent to message broker")
    connection.close()

# Endpoint to receive orders
@app.route('/order', methods=['POST'])
def receive_order():
    order_data = request.data
    # Process the received order data
    # For demonstration, let's just print the order data
    print("Received order:", order_data)
    #forward the order to inventory
    forward_request_to_message_broker(order_data)
    return jsonify({"message": "Order received successfully"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # Run the Flask app
