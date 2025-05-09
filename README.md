#  Rule-Based Chatbot 🤖

## Project Overview
A Python chatbot that uses predefined rules to respond to user inputs. The chatbot demonstrates fundamental NLP concepts through pattern matching and conditional logic.

## Key Features
- **Natural Language Understanding**:
  - Recognizes greetings ("hi", "hello", "hey")
  - Identifies farewells ("bye", "exit")
  - Answers tech questions ("What is Python?")
- **Conversation Flow**:
  - Maintains contextual dialogue
  - Provides graceful exit handling
- **Additional Capabilities**:
  - Shares random jokes
  - Offers interesting tech facts

## Technical Implementation
```python
# Example rule-based logic
if "hello" in user_input.lower():
    response = "Hello! How can I help you today?"
elif "python" in user_input.lower():
    response = "Python is an interpreted, high-level programming language."

How to Run
Clone repository:
git clone https://github.com/AppProjapati83/CodSoft_Task1.git

Execute chatbot:
python chatbot.py

Learning Outcomes
Developed rule-based response system

Implemented basic NLP pattern matching

Designed conversational UI flow

Gained experience in conditional logic implementation

