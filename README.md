# Medical DevOps Project

This project demonstrates a foundational, end-to-end data pipeline for ingesting and processing medical image metadata, designed with scalability for a real-world hospital environment in mind.

The pipeline uses a modern, open-source tech stack that can be run locally.

* **Ingestion**: A custom Python script using Pandas and SQLAlchemy.
* **Storage**: PostgreSQL running in a Docker container.
* **Processing**: Apache Spark (PySpark) for large-scale data transformation.
* **Containerization**: Docker and Docker Compose for a consistent environment.

## Project Architecture

This pipeline is a prototype for a scalable Medical DevOps (MLOps) system.

1.  **Ingestion**: `ingest_data.py` reads raw dataset metadata and loads it into a structured PostgreSQL database.
2.  **Storage**: The PostgreSQL database (`medical-data`), managed by Docker, serves as the central "source of truth" for the metadata.
3.  **Processing**: `process_data.py` uses PySpark to connect to the database and load the data into a distributed DataFrame, preparing it for machine learning tasks.
4.  **Scalability (Master-Slave Cluster)**: While this prototype runs on a single machine, it is designed to scale. The PySpark jobs can be deployed to a large, multi-node cluster to process terabytes of hospital data efficiently.

## How to Set Up and Run

1.  **Prerequisites**: Ensure you have Python, Git, and Docker Desktop installed and running.

2.  **Start the Database**: In the project's root directory, start the PostgreSQL database.
    ```bash
    docker-compose up -d
    ```

3.  **Install Dependencies**: Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download JDBC Driver**: For the Spark processing step, download the PostgreSQL JDBC driver (`.jar` file) from [https://jdbc.postgresql.org/download/](https://jdbc.postgresql.org/download/) and place it in the root of this project folder.

5.  **Run the Pipeline**: Execute the scripts in order.
    ```bash
    # Run ingestion first
    python ingest_data.py

    # Then run processing
    python process_data.py
    ```
