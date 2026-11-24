# Week 2 – Working with Multiple LLM Providers

## About the Experiment

In this experiment, I learned how to connect and work with different Large Language Models (LLMs) using Python.

I created a simple program that allows the user to choose between two providers: Gemini and Ollama. Based on the selected provider, the program takes a question from the user and displays the AI-generated response.

## What I Did

- Created a common LLM client using Python.
- Connected Gemini API as one of the LLM providers.
- Added Ollama as another provider to run a model locally.
- Created a program to select the provider (Gemini or Ollama).
- Allowed the user to enter their own questions.
- Displayed the generated response in the terminal.
- Created a basic test program to check whether the LLM client works correctly.

## Technologies Used

- Python
- Gemini API
- Ollama
- VS Code

## Libraries Used

- `google-genai`
- `python-dotenv`
- `requests`
- `pytest`

## Project Files

- `main.py` – Main program where the user selects the LLM provider and enters a question.
- `llm_client.py` – Contains the code for connecting Gemini and Ollama.
- `test_client.py` – Used to test the LLM client with a sample response.
- `requirements.txt` – Contains the required Python libraries.
- `.env` – Stores the Gemini API key securely.

## How to Run

1. Open the project folder in VS Code.
2. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Add your Gemini API key in the `.env` file:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the main program:

   ```bash
   python main.py
   ```

5. Choose your preferred provider:

   - Enter `gemini` to use Gemini.
   - Enter `ollama` to use Ollama.

6. Enter your question and view the generated response.

**Note:** To use Ollama, it must be installed and running locally, and the `llama3.2` model must be available.

## Testing

A basic test was created using Python's `unittest` module to check whether the LLM client returns the expected response.

Run the test using:

```bash
python -m unittest test_client.py
```

## What I Learned

Through this experiment, I learned how to work with multiple LLM providers in a single Python project. I understood how Gemini API and Ollama can be connected using a common client and how to take user input and generate AI responses.

I also got a basic understanding of testing Python programs.
