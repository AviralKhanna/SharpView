from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS
import os
import subprocess
import glob
import time  # Import time for unique filenames

app = Flask(__name__, static_folder="Frontend")
CORS(app)

# Define upload and enhanced folders
UPLOAD_FOLDER = 'uploads'
ENHANCED_FOLDER = r'C:\Users\kship\Desktop\Sagar\Frontend\Frontend\enhanced'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ENHANCED_FOLDER'] = ENHANCED_FOLDER

# Ensure the upload and enhanced directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

# Route for serving the index.html page
@app.route('/')
def serve_index():
    return send_from_directory('Frontend', 'index.html')


# Serve files from the static folder as needed
@app.route('/static/<path:filename>')
def serve_frontend(filename):
    return send_from_directory('static', filename)

# Route to handle static files, including CSS
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('Frontend', filename)

# Disable caching for enhanced images by adding cache control headers
@app.route('/images/<filename>')
def serve_image(filename):
    response = make_response(send_from_directory(ENHANCED_FOLDER, filename))
    response.headers['Cache-Control'] = 'no-store'  # Prevent caching of images
    return response

# New route to serve all images
@app.route('/images', methods=['GET'])
def get_all_images():
    all_images = []
    
    # Get images from the uploads folder
    upload_images = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], '*'))
    for img in upload_images:
        all_images.append(f'/uploads/{os.path.basename(img)}')

    # Get images from the enhanced folder
    enhanced_images = glob.glob(os.path.join(app.config['ENHANCED_FOLDER'], '*'))
    for img in enhanced_images:
        all_images.append(f'/enhanced/{os.path.basename(img)}')

    return jsonify(success=True, images=all_images)

def clear_enhanced_folder():
    # Remove all files in the enhanced folder before each enhancement process
    files = glob.glob(os.path.join(app.config['ENHANCED_FOLDER'], '*'))
    for file in files:
        os.remove(file)

@app.route('/enhance', methods=['POST'])
def enhance_image():
    clear_enhanced_folder()
    
    if 'image' not in request.files:
        return jsonify(success=False, message="No image part")
    
    file = request.files['image']
    if file.filename == '':
        return jsonify(success=False, message="No selected file")
    
    input_image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(input_image_path)

    try:
        # Use the full path to the Python executable
        subprocess.run([r"C:\Users\kship\AppData\Local\Programs\Python\Python311\python.exe", 'automation.py', input_image_path], check=True)

        # Rename the enhanced images with a unique identifier
        timestamp = str(int(time.time()))
        enhanced_images = glob.glob(os.path.join(ENHANCED_FOLDER, '*'))
        unique_enhanced_images = []
        for img_path in enhanced_images:
            new_filename = f"{timestamp}_{os.path.basename(img_path)}"
            new_path = os.path.join(ENHANCED_FOLDER, new_filename)
            os.rename(img_path, new_path)
            unique_enhanced_images.append(f'/images/{new_filename}')

        if not unique_enhanced_images:
            return jsonify(success=False, message="No enhanced images found.")

        return jsonify(success=True, images=unique_enhanced_images)

    except subprocess.CalledProcessError as e:
        return jsonify(success=False, message="Image enhancement failed", error=str(e))
    except Exception as e:
        return jsonify(success=False, message="An unexpected error occurred", error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
