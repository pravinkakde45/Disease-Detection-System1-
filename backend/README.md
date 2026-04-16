# Disease Detection System - Phase 1 Foundation

## Project Structure

- **backend/**: Contains the server-side logic and machine learning components.
  - **api/**: The Flask application serving the API, routes, and prediction interface.
  - **ml/**: Stores datasets, training scripts, trained models, and prediction logic.
  - **requirements.txt**: Python dependencies for the backend.
  - **README.md**: This file.
- **frontend/**: Placeholder for the future Flutter application.
- **docs/**: Documentation for the project.

## Setup Instructions (Windows)

1.  **Create a Virtual Environment**:
    Open a terminal in the project root (`Disease Detection System1`) and run:
    ```powershell
    python -m venv venv
    ```

2.  **Activate the Virtual Environment**:
    ```powershell
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```powershell
    pip install -r backend/requirements.txt
    ```

4.  **Run the Flask Server**:
    ```powershell
    python backend/api/app.py
    ```
    The server will start at `http://localhost:5000`.

5.  **Test the Health Endpoint**:
    Open your browser or Postman and visit:
    `http://localhost:5000/health`
    Expected response: `{"status": "API is running"}`
