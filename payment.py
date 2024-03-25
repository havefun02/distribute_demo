from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE_SHIPPING = 'shipping'
# Endpoint to process payments
def push_order_to_shipping(order_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE_SHIPPING)
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE_SHIPPING, body=order_data)
    print("Order pushed to shipping queue:", order_data)
    connection.close()

@app.route('/payment', methods=['POST'])
def process_payment():
    payment_data = request.data
    # Process the received payment data
    # For demonstration, let's just print the payment data
    print("Received payment:", payment_data)
    push_order_to_shipping(payment_data)
    return jsonify({"message": "Payment processed successfully"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)  # Run the Flask app
