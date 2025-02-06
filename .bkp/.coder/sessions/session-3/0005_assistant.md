### README.md [coder:save]
```
# Project Name

This project is a web application that includes both a backend and a frontend. The backend is built with FastAPI, and the frontend is built with React.

## Backend Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/project-name.git
   cd project-name
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:

   Create a `.env.local` file in the root directory and add the following environment variables:

   ```env
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your_secret_key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   EXTERNAL_API_URL=https://dev.flow.ciandt.com/channels-service/v1
   EXTERNAL_API_TOKEN=your_external_api_token
   ```

### Running the Server

1. Navigate to the backend directory:

   ```bash
   cd backend/app
   ```

2. Start the FastAPI server using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` flag will auto-reload the server on code changes. The server will be running at `http://localhost:8000`.

### API Documentation

Once the server is running, you can access the API documentation at `http://localhost:8000/docs` for the interactive Swagger UI or `http://localhost:8000/redoc` for ReDoc.

## Frontend Setup

Refer to the frontend README for instructions on setting up and running the frontend.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
[coder:end]