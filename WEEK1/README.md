# Week 1 – First LLM Experiment Using Gemini API

## About the Experiment

In this experiment, I learned how to get started with Generative AI using the Gemini API.

I created a Gemini API key from Google AI Studio and connected it to a Python program. I also learned how to use the API key securely with a `.env` file.

## What I Did

- Created a Gemini API key using Google AI Studio.
- Set up the Python project.
- Installed the required libraries.
- Stored the API key in a `.env` file.
- Connected Python with the Gemini API.
- Ran a basic program to ask Gemini a question about Artificial Intelligence.
- Displayed the response in the terminal.

## Technologies Used

- Python
- Gemini API
- Google AI Studio
- VS Code

## Libraries Installed

- `google-genai`
- `python-dotenv`
- `pytest`

## How to Run

1. Clone or download this project.
2. Open the project folder in VS Code.
3. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the Python program:

   ```bash
   python main.py
   ```

## Output

The program sends a simple question to Gemini:

"What is Artificial Intelligence? Explain in simple words."

Gemini generates an answer, which is displayed in the terminal.

## What I Learned

Through this experiment, I understood the basic process of connecting a Python application to a Large Language Model using an API. I also learned how to create and use an API key and get a response from Gemini.

This was my first hands-on experience with an LLM.
