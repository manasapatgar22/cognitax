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
