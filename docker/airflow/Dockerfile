FROM apache/airflow:latest

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Create necessary directories
RUN mkdir -p $AIRFLOW_HOME/dags $AIRFLOW_HOME/logs $AIRFLOW_HOME/plugins

# Expose the Airflow webserver port
EXPOSE 8080

# Set entrypoint to Airflow
ENTRYPOINT ["airflow"]

# Default command to start the webserver
CMD ["webserver"]
