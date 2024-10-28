FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py

# Run flask with binding to all interfaces
CMD ["flask", "run", "--host=0.0.0.0"]