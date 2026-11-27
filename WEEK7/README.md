# Week 7 – Next Token Prediction Using GPT-2

## About the Project

This project demonstrates how a pre-trained language model predicts the next word or token based on the given input.

For this experiment, I used **DistilGPT-2**, a lightweight version of GPT-2 available through the Hugging Face Transformers library.

The program takes a sample sentence as input, processes it using the tokenizer, and predicts the most likely next tokens along with their probability scores.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- DistilGPT-2

## Project Structure

```text
week-7/
│
├── main.py
└── requirements.txt
```

## How It Works

1. First, the required libraries are imported.
2. The DistilGPT-2 model and its tokenizer are loaded.
3. A sample prompt, `"The sun rises in the"`, is provided.
4. The tokenizer converts the input text into tokens that the model can understand.
5. The model processes the input and calculates the probabilities of possible next tokens.
6. Using the Top-K method, the program selects the five tokens with the highest probabilities.
7. Finally, it displays the predicted tokens along with their probability values.

## Installation

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Open the project folder in your terminal and execute:

```bash
python main.py
```

The model will load, process the given prompt, and display the top five possible next-token predictions.

**Note:** The model may download its files from Hugging Face the first time it runs, so an internet connection is required initially.

## Expected Output

The program displays:

- The input prompt.
- The top five next-token candidates.
- The probability associated with each candidate.
- A completion message confirming that the experiment ran successfully.

The exact predicted tokens and probability values may vary depending on the model version and environment.

## Learning Outcome

Through this experiment, I understood how a pre-trained language model processes text and predicts possible next tokens. I also got practical exposure to tokenization, model inference, probability calculation using Softmax, and Top-K selection.

## Conclusion

This experiment helped me understand the basic working of next-token prediction in language models. It also gave me hands-on experience with PyTorch and the Hugging Face Transformers library.
