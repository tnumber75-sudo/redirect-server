from flask import Flask, redirect, request
import logging

app = Flask(__name__)

# Set up logging to see incoming requests
logging.basicConfig(level=logging.INFO)

@app.route('/')
@app.route('/<path:path>')
def redirect_to_metadata(path=''):
    # Log the incoming request
    app.logger.info(f"Request received from: {request.remote_addr}")
    app.logger.info(f"Path requested: /{path}")
    
    # This is the internal AWS metadata endpoint we want to reach
    # WordPress will follow this redirect automatically
    internal_target = 'http://169.254.169.254/latest/user-data'
    
    # Return a 302 redirect response
    return redirect(internal_target, code=302)

# This is only for local testing
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
