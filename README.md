
# Coinbase Public Data API

Welcome to the Coinbase Public Data API project. This project provides a FastAPI application for retrieving public data from the Coinbase API. The data includes information about products, server time, order books, candles, and market trades.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetch all available products
- Retrieve the current server time
- Get order book data for a specific product
- Get detailed information for a specific product
- Get candle data (OHLCV) for a specific product
- Get market trade data for a specific product
- Publish and consume messages from a RabbitMQ queue

## Requirements

- Python 3.9+
- Docker (for containerization)
- RabbitMQ (for message queuing)

## Installation

### Using Docker

1. Clone the repository:
    \`\`\`sh
    git clone https://github.com/pedrosfaria2/market-data-api.git
    cd market-data-api
    \`\`\`

2. Build the Docker image:
    \`\`\`sh
    docker build -t coinbase-public-data-api .
    \`\`\`

3. Run the Docker container:
    \`\`\`sh
    docker run -d -p 8000:8000 --name coinbase-api coinbase-public-data-api
    \`\`\`

### Local Installation

1. Clone the repository:
    \`\`\`sh
    git clone https://github.com/pedrosfaria2/market-data-api.git
    cd market-data-api
    \`\`\`

2. Create a virtual environment and activate it:
    \`\`\`sh
    python -m venv venv
    source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
    \`\`\`

3. Install the dependencies:
    \`\`\`sh
    pip install -r requirements.txt
    \`\`\`

## Usage

### Running the Application

To run the application locally:
\`\`\`sh
uvicorn services.api.main:app --host 0.0.0.0 --port 8000
\`\`\`

Access the application at \`http://localhost:8000\`.

### API Endpoints

- \`GET /public/products\`: Fetch all products
- \`GET /public/server-time\`: Fetch the server time
- \`GET /public/product-book/{product_id}\`: Fetch the order book for a specific product
- \`GET /public/product/{product_id}\`: Fetch details for a specific product
- \`GET /public/candles/{product_id}?start={start}&end={end}&granularity={granularity}\`: Fetch candle data for a specific product
- \`GET /public/market-trades/{product_id}\`: Fetch market trades for a specific product
- \`POST /public/publish/{queue_name}\`: Publish a message to a RabbitMQ queue

### Environment Variables

To configure RabbitMQ, set the following environment variables:

- \`RABBITMQ_HOST\`: The host of the RabbitMQ server (default: \`rabbitmq\`)
- \`RABBITMQ_USER\`: The username for RabbitMQ (default: \`user\`)
- \`RABBITMQ_PASS\`: The password for RabbitMQ (default: \`password\`)

## Running the Application with Docker

To run the application using Docker, use the following command:
\`\`\`sh
docker run -d -p 8000:8000 -e RABBITMQ_HOST=rabbitmq -e RABBITMQ_USER=user -e RABBITMQ_PASS=password coinbase-public-data-api
\`\`\`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
