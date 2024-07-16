# Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [System Setup](#system-setup)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

## Overview
The pipeline is designed to:
- Extract data from Reddit using its API.
- Store the raw data into an S3 bucket from Airflow.
- Transform the data using AWS Glue and Amazon Athena.
- Load the transformed data into Amazon Redshift for analytics and querying.

## Architecture
![Architecture Diagram](path/to/Screenshot 2024-07-16 at 12.18.43 PM.png)

1. **Reddit API:** Source of the data.
2. **Apache Airflow & Celery:** Orchestrates the ETL process and manages task distribution.
3. **PostgreSQL:** Temporary storage and metadata management.
4. **Amazon S3:** Raw data storage.
5. **AWS Glue:** Data cataloging and ETL jobs.
6. **Amazon Athena:** SQL-based data transformation.
7. **Amazon Redshift:** Data warehousing and analytics.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation
- Python 3.9 or higher

## System Setup
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Akramash/reddit-data-eng.git
    cd reddit-data-eng
    ```

2. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables:**
    Create a `.env` file and set the necessary environment variables as specified in `airflow.env`.

5. **Starting the Containers:**
    ```bash
    docker-compose up -d
    ```

6. **Launch the Airflow Web UI:**
    Open your browser and go to `http://localhost:8080`.

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

## Acknowledgements
This project was greatly inspired and guided by the video ["Data Engineering Project: Reddit Data Pipeline with Airflow, AWS"](https://youtu.be/LSlt6iVI_9Y?si=qfvF1EvqfVTU7xkr) by Code With Yu. Many thanks to the creator for providing such a comprehensive tutorial.
