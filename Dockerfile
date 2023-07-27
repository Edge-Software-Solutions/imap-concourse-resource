FROM python:alpine3.18

# Install required libraries
RUN pip install imapclient

# Copy python script into the container
COPY scripts /opt/resource

# Make the script executable
RUN chmod +x /opt/resource/check
RUN chmod +x /opt/resource/in
RUN chmod +x /opt/resource/out

# Run the script when the container is started
#ENTRYPOINT ["/opt/resource/check.py"]
