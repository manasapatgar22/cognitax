from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
import cv2
import os
import pymongo

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"  # Change if using MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client["TaxAssistantDB"]
collection = db["TaxRecords"]

# Ensure uploads directory exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# OCR Function to Extract Data from Images
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    extracted_text = extract_text(file_path)

    # Store extracted data in MongoDB
    record = {"filename": file.filename, "extracted_text": extracted_text}
    collection.insert_one(record)

    return jsonify({'extracted_text': extracted_text, 'message': 'Data saved to MongoDB'})

@app.route('/records', methods=['GET'])
def get_records():
    records = list(collection.find({}, {"_id": 0}))  # Fetch all records
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)
