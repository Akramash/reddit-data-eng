# Reddit Data Engineering Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview
This project is designed to ingest, process, and analyze data from Reddit using modern data engineering techniques. The goal is to build a robust ETL pipeline that extracts data, transforms it into a useful format, and loads it into a data warehouse for further analysis.

## Features
- **Data Ingestion:** Extract data from Reddit's API.
- **Data Transformation:** Clean and preprocess the data using Python.
- **Data Loading:** Load the transformed data into a data warehouse.
- **Scheduling:** Use Apache Airflow for scheduling and orchestrating ETL jobs.
- **Docker Support:** Containerized environment for easy deployment.

## Installation
To set up this project on your local machine, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Akramash/reddit-data-eng.git
    cd reddit-data-eng
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Environment:**
    Ensure you have Docker installed. Then, run:
    ```bash
    docker-compose up
    ```

4. **Configure Environment Variables:**
    Create a `.env` file and set the necessary environment variables as specified in `airflow.env`.

## Usage
1. **Start Airflow:**
    ```bash
    docker-compose up
    ```

2. **Access Airflow Web UI:**
    Open your browser and go to `http://localhost:8080`.

3. **Trigger the ETL Pipeline:**
    In the Airflow UI, trigger the `reddit_etl` DAG to start the data pipeline.

## Project Structure
- **dags/**: Contains the Airflow DAGs.
- **data/**: Directory for storing data files.
- **etls/**: Scripts for extracting, transforming, and loading data.
- **logs/**: Directory for Airflow logs.
- **pipelines/**: Contains pipeline scripts.
- **utils/**: Utility functions and helpers.

## Contributing
We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) to get started.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
