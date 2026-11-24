# Week 3 – LLM Usage Tracking and Monitoring

## About the Experiment

In this experiment, I learned how to monitor the usage of Large Language Models (LLMs).

I extended my previous week's project by adding usage tracking. The program allows users to choose between Gemini and Ollama, enter a question, and receive an AI-generated response.

It also tracks details such as the number of input and output tokens, response time, and estimated API cost. These details are stored in MongoDB for monitoring.

## What I Did

- Continued working with Gemini and Ollama.
- Created an LLM usage tracking system.
- Measured the response time (latency) of the AI models.
- Tracked input tokens and output tokens.
- Calculated the estimated API cost for Gemini.
- Added a retry mechanism to handle temporary errors.
- Connected the project to MongoDB.
- Stored API usage details in a MongoDB database.
- Created a basic test to check the LLM client.

## Technologies Used

- Python
- Gemini API
- Ollama
- MongoDB
- VS Code

## Libraries Used

- `google-genai`
- `python-dotenv`
- `requests`
- `pymongo`
- `pytest`

## Project Files

- `main.py` – Main program to select the provider, enter a question, and display the response.
- `llm_client.py` – Handles Gemini and Ollama connections, response time, token usage, cost estimation, and retries.
- `usage_logger.py` – Saves LLM usage details into MongoDB.
- `test_client.py` – Tests the LLM client using a sample provider.
- `requirements.txt` – Contains the required Python libraries.
- `.env` – Stores API and MongoDB connection details securely.

## How to Run

1. Open the project folder in VS Code.
2. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Add your Gemini API key and MongoDB connection string to the `.env` file:

   ```env
   GEMINI_API_KEY=your_api_key_here
   MONGODB_URI=your_mongodb_connection_string
   ```

4. Make sure MongoDB is accessible and Ollama is running if you want to use Ollama.
5. Run the program:

   ```bash
   python main.py
   ```

6. Choose either `gemini` or `ollama`.
7. Enter your question and view the AI response along with usage details.

## Testing

A basic unit test is included to check whether the LLM client generates the expected response and correctly records usage details.

Run the test using:

```bash
python -m unittest test_client.py
```

## What I Learned

Through this experiment, I learned how to track the usage of LLMs and monitor their performance. I understood how to measure response time, count tokens, estimate API costs, and store usage information in MongoDB.

I also learned about handling temporary errors using retries and testing the LLM client using a sample provider.
