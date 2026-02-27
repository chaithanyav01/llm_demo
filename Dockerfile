FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

# Copy dependencies first
COPY requirements.txt .

# Install dependencies (CPU torch)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Lambda entry point
CMD ["main.handler"]