# Masterblog API

## Overview

Masterblog API is a RESTful API built with Flask that allows users to create, read, update, delete, search, and sort blog posts. It includes API documentation using Swagger UI.

## Features

- **List Posts:** Retrieve all blog posts.
- **Create Post:** Add a new blog post.
- **Delete Post:** Remove a blog post by its ID.
- **Update Post:** Modify the title and/or content of a blog post.
- **Search Posts:** Find posts by title or content.
- **Sort Posts:** Sort posts by title or content in ascending or descending order.
- **API Documentation:** Interactive documentation via Swagger UI.

## Getting Started

### Prerequisites

- **Python 3.x**
- **Pip**
- **Git**

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/F-Fleron-G/Masterblog-API.git
    cd Masterblog-API/backend
    ```

2. **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *If `requirements.txt` does not exist, install manually:*
    ```bash
    pip install flask flask-cors flask-swagger-ui
    ```

### Running the Application

1. **Start the Backend Server:**
    ```bash
    python3 backend/backend_app.py
    ```
    - The server will run on `http://0.0.0.0:5002`.

2. **Access API Documentation:**
    - Open your browser and navigate to `http://localhost:5002/api/docs`.

### Testing the Frontend

1. **Start the Frontend Application:**
    ```bash
    cd ../frontend
    python3 frontend_app.py
    ```

2. **Open the Frontend in Your Browser:**
    - Navigate to `http://127.0.0.1:5001`.

3. **Configure the API Base URL:**
    - Enter the Codio API URL (e.g., `http://<codio-url>:5002/api`) in the frontend's API Base URL field.
    - Click **"Load Posts"** to display the blog posts.

## API Endpoints

### List Posts
- **URL:** `/api/posts`
- **Method:** `GET`
- **Description:** Retrieves all blog posts, optionally sorted by title or content.

### Create Post
- **URL:** `/api/posts`
- **Method:** `POST`
- **Description:** Creates a new blog post.
- **Body:**
    ```json
    {
      "title": "Post Title",
      "content": "Post Content"
    }
    ```

### Delete Post
- **URL:** `/api/posts/<id>`
- **Method:** `DELETE`
- **Description:** Deletes a blog post by its ID.

### Update Post
- **URL:** `/api/posts/<id>`
- **Method:** `PUT`
- **Description:** Updates the title and/or content of a blog post.
- **Body:**
    ```json
    {
      "title": "Updated Title",
      "content": "Updated Content"
    }
    ```

### Search Posts
- **URL:** `/api/posts/search`
- **Method:** `GET`
- **Description:** Searches for posts by title and/or content.
- **Query Parameters:**
    - `title` (optional)
    - `content` (optional)

## License

This project is licensed under the MIT License.
