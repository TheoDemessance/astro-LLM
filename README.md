# astro-LLM

## Chatbot Web Application
### Introduction
This project is a Flask-based web application for a chatbot interface. It allows users to interact with a chatbot through a simple and intuitive web interface. The backend is built with Flask, a lightweight WSGI web application framework in Python, making it easy to extend and maintain.

### Features
- Chat interface for user-bot interaction.
- Flask backend with REST API.
- Environment variable management for secure configuration.
- Modular and scalable project structure.

### Getting Started
#### Prerequisites
- Python 3.6+
- pip (Python package manager)
- Virtual environment (recommended)

#### Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Set up a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a .env file in the root directory and add the necessary environment variables:

```makefile
ADB_BEARER_TOKEN=your_bearer_token
ADB_SERVINGENDPOINT_URL=your_endpoint_url
```

5. Run the application
```bash
python run.py
The application will be available at http://localhost:5000.
```

### Usage
After starting the application, navigate to http://localhost:5000 in your web browser. You can interact with the chatbot by typing messages and receiving responses.

### Structure
- app/: Main application directory.
    - templates/: HTML templates.
    - static/: Static files like CSS and JavaScript.
    - __init__.py: Initializes the Flask application.
    - routes.py: Contains all the route definitions.
    - utils.py: Utility functions.

- venv/: Virtual environment for project dependencies.
- .env: Environment variables.
- run.py: Entry point to start the Flask application.

### Contributing

Contributions to this project are welcome! Here are a few ways you can help:
- Report bugs and issues.
- Suggest new features or improvements.
- Submit pull requests with bug fixes or new features.