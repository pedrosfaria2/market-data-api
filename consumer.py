import pika  # Import the Pika library for RabbitMQ
import os  # Import the os library for environment variable handling

# Get RabbitMQ connection details from environment variables, with default values
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
rabbitmq_user = os.getenv("RABBITMQ_DEFAULT_USER", "user")
rabbitmq_pass = os.getenv("RABBITMQ_DEFAULT_PASS", "password")

def callback(ch, method, properties, body):
    """
    Callback function to process received messages.
    
    Args:
        ch: The channel object.
        method: Method frame with delivery tag and other metadata.
        properties: Properties of the message.
        body: The actual message body.
    """
    print(f" [x] Received {body}")

def consume_messages(queue_name: str):
    """
    Consume messages from a specified RabbitMQ queue.
    
    Args:
        queue_name (str): The name of the queue to consume messages from.
    """
    # Set up credentials for connecting to RabbitMQ
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    # Establish a blocking connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials))
    # Create a channel for communication
    channel = connection.channel()

    # Declare a queue to ensure it exists
    channel.queue_declare(queue=queue_name, durable=True)
    # Set up consumption of messages from the queue with a callback function
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    # Start consuming messages
    channel.start_consuming()

# Entry point for running the consumer
if __name__ == "__main__":
    while True:  # Run the consumer in an infinite loop
        consume_messages('test_queue')
