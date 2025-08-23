import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts", "training", "trained_model.h5"))
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Get raw predictions (probabilities)
        predictions = model.predict(test_image)
        result = np.argmax(predictions, axis=1)
        
        # Calculate confidence scores
        confidence_scores = predictions[0]
        max_confidence = float(np.max(confidence_scores))
        
        # Class labels
        class_labels = ['Adenocarcinoma Cancer', 'Normal']
        predicted_class = class_labels[result[0]]
        
        # Get confidence for each class
        adenocarcinoma_confidence = float(confidence_scores[0])
        normal_confidence = float(confidence_scores[1])
        
        print(f"Prediction: {predicted_class}")
        print(f"Confidence: {max_confidence:.2%}")
        
        return {
            "prediction": predicted_class,
            "confidence": round(max_confidence * 100, 2),
            "class_probabilities": {
                "Adenocarcinoma Cancer": round(adenocarcinoma_confidence * 100, 2),
                "Normal": round(normal_confidence * 100, 2)
            },
            "status": "success"
        }