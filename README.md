# Campus FAQ Chatbot 🎓

A retrieval-based FAQ chatbot built with Python, Streamlit, and Scikit-learn. It matches user questions against a predefined FAQ dataset and returns the most relevant stored answer.

## Features

- Answers common college-related questions.
- Matches alternative phrasings of questions.
- Uses TF-IDF for text vectorization.
- Uses cosine similarity to compare questions.
- Provides a fallback response for low-similarity queries.
- Displays chat history, FAQ categories, and similarity scores.
- Includes automated test cases for expected chatbot behavior.

## Tech Stack

- Python
- Streamlit
- Scikit-learn

## Project Structure

```text
CodeAlpha_FAQChatbot/
├── app.py
├── chatbot.py
├── faq_data.py
├── test_chatbot.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone or download this repository, then open a terminal in the project directory.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## Run Tests

```bash
python test_chatbot.py
```

The current test suite checks admission, password reset, exam timetable, and an unrelated question.

**Current test result:** 4/4 test cases passed in the tested run.

## How It Works

1. FAQ questions and alternative phrasings are stored in `faq_data.py`.
2. TF-IDF converts stored questions into numerical feature vectors.
3. Cosine similarity compares the user's question with the stored questions.
4. The best match is returned if its score passes the configured threshold.
5. Otherwise, the chatbot displays a fallback response.

## Limitations

This is a basic retrieval-based chatbot, not a generative AI system. TF-IDF relies on word patterns and does not fully understand language meaning. Similarity scores are not probabilities of answer correctness, and some unrelated questions may still be matched incorrectly.

The FAQ content is for demonstration purposes. Verify college policies using official sources before relying on them.

## Future Improvements

- Expand the FAQ dataset.
- Improve matching and fallback accuracy.
- Add more automated tests and evaluation metrics.
- Support multilingual questions.
- Deploy the chatbot online.

## Author

AYUSH KUMAR SINGH
## Project Information

CodeAlpha AI Internship — Project 2: FAQ Chatbot