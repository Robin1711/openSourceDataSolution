FROM bitnami/spark:latest

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PYSPARK_PYTHON=/usr/bin/python3

# Create working directory
WORKDIR $SPARK_HOME

# Expose Spark UI and worker ports
EXPOSE 8080 7077 4040

# Default command to start Spark
CMD ["/opt/spark/bin/spark-submit"]
