# Back-End-Services-for-Accenture-AWS-Storage-System

This is a RESTful APIs for file management that serves as second task for the cloud-based storage system project. It enables functionalities for file uploads, downloads, and sharing.

## Task Outline

### Scenario:

Develop RESTful APIs for file management in a cloud-based storage system. Enable functionalities for file uploads, downloads, and sharing.

### Deliverable:

- Well-documented RESTful APIs implemented using Python or Java.
- Clean, well-structured, and well-commented code.

## Overview

This repository contains the backend implementation for a cloud-based storage system, providing RESTful APIs for file management. The implementation uses Python with the Flask framework and integrates with AWS S3 for file storage.

## Features

- File upload with AWS S3 integration
- File download with AWS S3 integration
- Authentication using JWT
- Simulated user database and file storage
- Error handling for various scenarios
- Very well documented code implementation

## Prerequisites

- Python
- Flask
- boto3 (AWS SDK for Python)
- JWT

## Setup

1. Install the required dependencies:

   ```bash
   pip install Flask boto3 PyJWT
   ```

2. Set up your AWS credentials by replacing `MY_AWS_ACCESS_KEY_ID` and `MY_AWS_SECRET_ACCESS_KEY` in the code.

3. Replace `MY-bucket-name` with your actual AWS S3 bucket name in the code.

4. Run the Flask application:
   ```bash
   python fileManagementRESTfulAPI.py
   ```

## Endpoints

### Upload File

- **Endpoint**: `/upload`
- **Method**: POST
- **Headers**: Authorization (Bearer token)
- **Parameters**: File (multipart/form-data)

### Download File

- **Endpoint**: `/download/<filename>`
- **Method**: GET
- **Headers**: Authorization (Bearer token)

## Authentication

- JWT (JSON Web Token) is used for authentication.
- The server checks for the Authorization header with a Bearer token.
- Tokens are decoded using the HS256 algorithm.

## Security Measures

- Encryption at rest is ensured through AWS S3.
- Data in transit is secured using HTTPS.
- Authorization checks are implemented for file access.

## Error Handling

- The application includes error handling mechanisms.
- Custom error messages and HTTP status codes are provided for better debugging.

## Additional Notes

- This implementation is a simplified example and may require additional security measures, error handling, and more robust functionalities for a production environment.

- Feel free to clone, modify, and use this repository as a starting point for your cloud-based storage system.

- For any questions or issues, please open an [issue](https://github.com/Farahat612/Accenture-Cloud-Based-Storage-System/issues).
