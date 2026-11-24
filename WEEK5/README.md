# Week 5 – LLM Token Economics and Budget Planning

## About the Experiment

In this experiment, I learned how to estimate the cost and usage of Large Language Models (LLMs) before using them in a project.

I created a Python program that calculates the expected input tokens, output tokens, daily cost, and monthly cost based on the given usage details. It also checks whether the planned usage stays within the available API limits and budget.

## What I Did

- Created a basic LLM budget calculator using Python.
- Set the expected number of requests per day.
- Defined average input and output tokens.
- Added input and output token pricing.
- Calculated the estimated daily and monthly costs.
- Checked Requests Per Minute (RPM) limits.
- Checked Tokens Per Minute (TPM) limits.
- Added a safety margin to handle extra usage.
- Compared the estimated costs with daily and monthly budgets.
- Displayed PASS or REVIEW based on the results.
- Created test cases to check the calculations.

## Technologies Used

- Python
- VS Code

## Libraries Used

- `python-dotenv`
- `unittest` (Python built-in testing library)

## Project Files

- `budget.py` – Main Python program that calculates token usage, estimated costs, API limits, and budget status.
- `test_budget.py` – Contains test cases to check whether the budget calculations work correctly.
- `requirements.txt` – Contains the required Python library.
- `.env` – Stores the usage assumptions, pricing details, API limits, and budget values.

## How to Run

1. Open the project folder in VS Code.
2. Install the required library:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Make sure the `.env` file contains the required configuration values.
4. Run the main program:

   ```bash
   python budget.py
   ```

5. View the token economics report in the terminal.

## Testing

The project includes basic unit tests using Python's `unittest` module.

The tests check:
- Daily and monthly cost calculations.
- Whether RPM and TPM limits are satisfied.
- Whether the program detects when the RPM limit is exceeded.
- Whether the program detects when the monthly budget is exceeded.

Run the tests using:

```bash
python -m unittest test_budget.py
```

## Output

The program displays a Token Economics Report containing:

- Input tokens per day.
- Output tokens per day.
- Total tokens per day.
- Estimated daily cost.
- Estimated monthly cost.
- Peak RPM with safety margin.
- Peak TPM with safety margin.
- API capacity and budget checks.

At the end, it provides a recommendation based on whether all the configured limits are satisfied.

## What I Learned

Through this experiment, I understood how to estimate LLM usage costs and plan a budget before building an AI application.

I learned about input tokens, output tokens, RPM, TPM, and safety margins. I also understood how Python can be used to check API capacity and budget limits and how unit testing helps verify calculations.
