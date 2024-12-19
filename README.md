# E-Commerce Chatbot

A full-stack e-commerce chatbot application that integrates a **React frontend** with a **Flask backend**. The chatbot allows users to search for products on the platform and retrieve relevant product details.

## Features
- Chatbot interface for product search and recommendations.
- Backend API built using **Flask** and connected to a **SQLite** database.
- **React.js** frontend for real-time user interaction with the chatbot.
- Product search functionality based on a relational database (SQLite).

## Project Structure

```
/ecommerce-chatbot
|-- /backend
|   |-- app.py           # Flask app for handling API requests
|   |-- models.py        # Database model definitions (Product)
|   |-- populate_db.py   # Script to populate the database with mock data
|
|-- /frontend
|   |-- /src
|       |-- /components  # React components for the chatbot interface
|       |-- /services    # Services for API communication
|       |-- App.js       # Main React component
|       |-- index.js     # React entry point
|
|-- README.md           # Project documentation
```

## Getting Started

### **Backend Setup (Flask + SQLite)**

1. **Install Backend Dependencies**:
   Navigate to the backend folder and install the required Python dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

   Make sure `requirements.txt` contains the following libraries:

   ```txt
   Flask
   Flask-SQLAlchemy
   flask-cors
   ```

2. **Run Flask Backend**:
   Start the Flask server:

   ```bash
   python app.py
   ```

   The backend will run on `http://localhost:5000`.

3. **Populate Database with Mock Products**:
   To populate your SQLite database with 100 mock e-commerce products, run the following:

   ```bash
   python populate_db.py
   ```

   This will create an SQLite database (`db.sqlite3`) and insert mock product entries.

4. **Test API**:
   You can manually test the backend by sending a POST request to `http://localhost:5000/api/chat` with the following JSON body:

   ```json
   {
     "message": "product"
   }
   ```

   You should get a JSON response with matching product details or an error message if no products are found.

---

### **Frontend Setup (React)**

1. **Install Frontend Dependencies**:
   Navigate to the frontend folder and install the necessary JavaScript dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. **Run React Development Server**:
   Start the React frontend by running:

   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`.

3. **Configure API URL**:
   Ensure that the frontend is set up to communicate with the correct backend API URL (`http://localhost:5000`). This is defined in the `Chatbot.js` component.

   Example:
   ```javascript
   const response = await axios.post('http://localhost:5000/api/chat', { message: input });
   ```

4. **Testing**:
   Open the app in your browser. The chatbot interface should load, and you can start chatting by typing a query, e.g., "laptop". The chatbot will search for products related to the query and display relevant results.

---

## Troubleshooting

1. **CORS Issues**:
   If you're encountering CORS issues, ensure that the `flask-cors` library is properly installed and configured in your backend (`CORS(app)` in `app.py`).

2. **API Not Responding**:
   - Ensure that the Flask server is running (`python app.py`).
   - Test the API using Postman or `curl` to verify it is responding correctly.
   - Check the browser's **console** and **network tab** for errors related to the API request.

3. **Error Communicating with Server**:
   If you see an error like "Error communicating with server", check the **backend logs** to ensure the API is running. Also, verify that the frontend is sending the request to the correct URL.

---

## API Endpoints

### **POST** `/api/chat`
- **Description**: Processes a user message and returns relevant products from the database.
- **Request Body**:

  ```json
  {
    "message": "product query"
  }
  ```

- **Response**:
  - **Success**: A JSON object containing matching products:

    ```json
    {
      "reply": "Here are the matching products:",
      "products": [
        {
          "id": 1,
          "name": "Product 1",
          "price": 20.99
        },
        {
          "id": 2,
          "name": "Product 2",
          "price": 15.49
        }
      ]
    }
    ```

  - **Error**: If no products are found or an error occurs:

    ```json
    {
      "error": "No products found for 'query'"
    }
    ```

---

## Built With

- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Database**: SQLite
- **CORS**: flask-cors (to allow cross-origin requests)

---

