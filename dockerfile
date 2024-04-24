# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and random_paragraphs file into the container
COPY  script.py random_paragraphs.txt /app/

# Install any needed dependencies specified in random_paragraphs.txt
RUN pip install --no-cache-dir requests numpy pandas

# Run the Python script when the container launches
CMD ["python", "script.py"]

 