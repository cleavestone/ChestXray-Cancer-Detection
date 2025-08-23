from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline
import traceback

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    try:
        os.system("python main.py")
        return jsonify({"message": "Training completed successfully!", "status": "success"})
    except Exception as e:
        return jsonify({"error": f"Training failed: {str(e)}", "status": "error"}), 500


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        # Check if file is uploaded
        if 'image' not in request.files:
            return jsonify({"error": "No image file uploaded", "status": "error"}), 400

        file = request.files['image']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({"error": "No file selected", "status": "error"}), 400
        
        # Validate file type
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
        file_extension = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
        
        if file_extension not in allowed_extensions:
            return jsonify({"error": "Invalid file type. Please upload an image file.", "status": "error"}), 400
        
        # Save the uploaded file
        file.save(clApp.filename)
        
        # Make prediction
        result = clApp.classifier.predict()
        
        return jsonify(result)
        
    except FileNotFoundError as e:
        return jsonify({"error": "Model file not found. Please ensure the model is trained and available.", "status": "error"}), 500
    except Exception as e:
        # Log the full traceback for debugging
        print("Prediction error:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": f"Prediction failed: {str(e)}", "status": "error"}), 500
    finally:
        # Clean up the uploaded file
        try:
            if os.path.exists(clApp.filename):
                os.remove(clApp.filename)
        except:
            pass  # Ignore cleanup errors


@app.route("/health", methods=['GET'])
@cross_origin()
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Application is running"})


if __name__ == "__main__":
    clApp = ClientApp()
    # Use environment variables for configuration
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 8080))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)