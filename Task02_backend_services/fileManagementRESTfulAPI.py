from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename  # Utility for securing filenames
import boto3  # AWS SDK for Python
import jwt  # JSON Web Token library for authentication

app = Flask(__name__) # Create a Flask app



# AWS S3 client setup
s3 = boto3.client('s3',
                  aws_access_key_id='My_AWS_ACCESS_KEY_ID',
                  aws_secret_access_key='MY_AWS_SECRET_ACCESS_KEY') # AWS credentials



# Simulated user database (for demonstration)
users = {
    'user1': 'password1',
    'user2': 'password2'
} # In a real system, we would use a database like MySQL or MongoDB



# Simulated database or storage
files = {} # In a real system, we would use a database like MySQL or MongoDB



# JWT secret key (for demonstration, in production, we will use a secure, secret key)
JWT_SECRET = 'MY-secret-key' # In a real system, we would use a secure, secret key



# Error Handling decorator
def handle_errors(func): # This decorator handles errors and returns a JSON response
    def wrapper(*args, **kwargs): # This function is called when an error occurs
        try: 
            return func(*args, **kwargs) 
        except Exception as e: 
            return jsonify({'error': str(e)}), 500 # Internal server error
    return wrapper # Return the wrapper function



# Authentication
def authenticate(username, password): # In a real system, we would use a more secure authentication mechanism
    if username in users and users[username] == password: 
        return True
    return False



# Authorization
def authorize_access(username, filename): 
    # In a real system, permissions and access control would be more complex for sure, I just wrote these lines for demonstration
    return True



# File Upload API with AWS S3 integration, error handling, and security measures
@app.route('/upload', methods=['POST']) # This API accepts only POST requests
@handle_errors # Decorator for error handling
def upload_file(): # This function is called when a POST request is sent to /upload
    auth_header = request.headers.get('Authorization') # Get the Authorization header from the request
    if not auth_header: # If no Authorization header is provided
        return jsonify({'error': 'Authorization header is required'}), 401 # Unauthorized

    token = auth_header.split('Bearer ')[1]
    try: # If the token is invalid or expired
        jwt.decode(token, JWT_SECRET, algorithms='HS256') # Decode the token
    except jwt.ExpiredSignatureError: # If the token is expired
        return jsonify({'error': 'Token has expired'}), 401 # Unauthorized
    except jwt.InvalidTokenError: # If the token is invalid
        return jsonify({'error': 'Invalid token'}), 401 # Unauthorized

    if 'file' not in request.files: # If no file is provided
        return jsonify({'error': 'No file part'}), 400 # Bad request

    uploaded_file = request.files['file'] # Get the file from the request
    if uploaded_file.filename == '': # If no file is selected
        return jsonify({'error': 'No selected file'}), 400 # Bad request

    if uploaded_file and authenticate('user1', 'password1'): # If the file is uploaded successfully
        filename = secure_filename(uploaded_file.filename) # Secure the filename
        s3.put_object(Bucket='MY-bucket-name', Key=filename, Body=uploaded_file) # Upload the file to AWS S3
        files[filename] = {'content': filename, 'shared_with': []} # Add the file to the database
        return jsonify({'message': 'File uploaded successfully'}) # Return a success message

    return jsonify({'error': 'Upload failed'}), 500 # Internal server error



# File Download API with AWS S3 integration and error handling
@app.route('/download/<filename>', methods=['GET']) # This API accepts only GET requests
@handle_errors # Decorator for error handling
def download_file(filename): # This function is called when a GET request is sent to /download/<filename>
    if authenticate('user1', 'password1') and authorize_access('user1', filename):
        # If the user is authenticated and authorized
        response = s3.get_object(Bucket='MY-bucket-name', Key=filename) # Download the file from AWS S3
        file_content = response['Body'].read() # Get the file content
        return file_content # Return the file content
    return jsonify({'error': 'File not found or access denied'}), 404 # Not found



if __name__ == '__main__': # If the script is run directly
    app.run(debug=True) # Run the Flask app in debug mode


