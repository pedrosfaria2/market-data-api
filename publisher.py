import pika  # Import the Pika library for RabbitMQ
import json  # Import the json library for JSON handling
import os  # Import the os library for environment variable handling

# Get RabbitMQ connection details from environment variables, with default values
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
rabbitmq_user = os.getenv("RABBITMQ_USER", "user")
rabbitmq_pass = os.getenv("RABBITMQ_PASS", "password")

def publish_message(queue_name: str, message: str):
    """
    Publish a message to a specified RabbitMQ queue.
    
    Args:
        queue_name (str): The name of the queue to publish the message to.
        message (str): The message to be published.
    """
    # Set up credentials for connecting to RabbitMQ
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    # Establish a blocking connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials))
    # Create a channel for communication
    channel = connection.channel()
    
    # Declare a queue to ensure it exists and is durable
    channel.queue_declare(queue=queue_name, durable=True)
    
    # Publish the message to the specified queue with persistence properties
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps({'message': message}),  # Convert the message to JSON format
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        )
    )
    
    # Close the connection to RabbitMQ
    connection.close()
