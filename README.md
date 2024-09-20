# LeetCode Problem Database

This project sets up a PostgreSQL database to store LeetCode problems, along with an ETL (Extract, Transform, Load) process to populate the database from a JSON file.

## Project Overview

The project consists of the following components:

1. A PostgreSQL database to store LeetCode problems
2. An ETL script (`etl.py`) to load data from a JSON file into the database
3. Docker configuration to set up the database and run the ETL process

## Data Source

The LeetCode problem data used in this project is sourced from the following dataset:

[LeetCode Dataset by greengerong](https://huggingface.co/datasets/greengerong/leetcode)

## Setup and Usage

1. Ensure you have Docker and Docker Compose installed on your system.
2. Clone this repository to your local machine.
3. Place the `leetcode-train.jsonl` file in the project root directory.
4. Run `docker-compose up` to start the PostgreSQL database and run the ETL process.

## Project Structure

- `docker-compose.yml`: Defines the services (PostgreSQL and ETL) and their configurations.
- `etl.py`: Python script to extract data from the JSON file and load it into the PostgreSQL database.
- `requirements.txt`: Lists the Python dependencies required for the ETL script.

## Database Schema

The PostgreSQL database contains a single table `leetcode_problems` with the following columns:

- `id`: Serial Primary Key
- `slug`: Text
- `title`: Text
- `difficulty`: Text
- `content`: Text
- `python`: Text

This schema allows for efficient storage and retrieval of LeetCode problem data.

## Acknowledgements

Special thanks to [greengerong](https://huggingface.co/greengerong) for providing the LeetCode dataset used in this project.
