# AI Tax Assistant - Backend

## 📌 Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd backend
2.Install dependencies:
pip install -r requirements.txt

3.Run the API:
python app.py


📌 API Endpoints
Method	Endpoint	Description
GET    	/	        Check API status
POST	  /upload	  Upload tax document for OCR processing

📌 Deployment
To deploy on Heroku, run:
git push heroku main

## **Frontend (React) Files**

### **7️⃣ `index.js` (React Entry Point)**
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';

ReactDOM.render(<App />, document.getElementById('root'));


# AI Tax Assistant - Frontend

## 📌 Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd frontend
2.Install dependencies:
npm install

3.Run the React App:
npm start

📌 Deployment
To deploy on GitHub Pages:
npm run build
npm run deploy

## **Final Steps: Upload to GitHub**
### **1️⃣ Initialize Git Repository**
```sh
git init
git add .
git commit -m "Initial commit"
2️⃣ Push Backend to GitHub
cd backend
git remote add origin <backend_repo_url>
git push -u origin main
3️⃣ Push Frontend to GitHub
cd frontend
git init
git add .
git commit -m "Initial frontend commit"
git remote add origin <frontend_repo_url>
git push -u origin main
