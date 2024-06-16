# RAG_App_Wih_Azure_OpenAI

This is a simple chatbot application built using Flask. The chatbot sends user queries to an Azure Machine Learning (ML) endpoint, which leverages GPT-3.5 turbo as the language model, and displays the bot's response.

## Features

- Send user input to an Azure ML endpoint
- Display the bot's response
- Maintain conversation history using Flask sessions

## Architecture

The chatbot application architecture is based on the Azure cloud and uses GPT-3.5 turbo as the language model. Below is the architecture diagram:

![Architecture Diagram](https://github.com/riphunter7001x/RAG_App_Wih_Azure_OpenAI/blob/main/images/mode_Architecture.png)

## Requirements

- Python 3.10
- Flask
- openai

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/riphunter7001x/RAG_App_Wih_Azure_OpenAI.git
cd RAG_App_Wih_Azure_OpenAI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root directory and add the following environment variables:

```
ENDPOINT_URL=<your-endpoint-url>
API_KEY=<your-api-key>
```

### 5. Run the application

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to use the chatbot.

## File Structure

```
RAG_App_Wih_Azure_OpenAI/
│
├── templates/
│   └── chatbot.html
├── .env
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

This is the main Flask application file. It handles GET and POST requests, interacts with the Azure ML endpoint, and manages session data.

### `templates/chatbot.html`

This is the HTML template for the chatbot interface. It uses Bootstrap for basic styling.

### `.env`

This file contains the environment variables for the endpoint URL, API key, and secret key.

### `requirements.txt`

This file lists the required Python packages.

## Usage

1. Enter a message in the input box and submit.
2. The bot's response will be displayed below the input box.
3. Previous conversations will be maintained in the session.



