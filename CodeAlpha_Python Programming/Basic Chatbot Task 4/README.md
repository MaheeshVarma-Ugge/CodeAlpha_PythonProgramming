# Task 4 - Basic Chatbot

## Overview
A simple rule-based chatbot built in Python that responds to a fixed set of predefined user inputs using basic conditional matching.

## How It Works
- The chatbot runs in a continuous loop, prompting the user for input.
- User input is converted to lowercase and matched against a small set of known phrases:
  - `"hello"` → `"Bot: Hi!"`
  - `"how are you"` → `"Bot: I'm fine, thanks!"`
  - `"bye"` → `"Bot: Goodbye!"` (exits the loop)
  - Any other input → `"Bot: Sorry, I don't understand."`
- The conversation continues until the user types `bye`.

## File
- `Task 4.py` - Main chatbot script.

## How to Run
```bash
python "Task 4.py"
```

## Sample Conversation
```
Simple Chatbot
Type 'bye' to exit.

You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

## Notes
- Uses simple `if`/`elif`/`else` string matching - no external libraries or NLP involved.
- Designed as an introductory, rule-based chatbot example (no machine learning or intent classification).
