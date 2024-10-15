This project involves creating a simple rule-based chatbot that provides responses based on a dataset of pre-defined questions and answers. The chatbot uses the difflib library's get_close_matches function to match user inputs with similar questions in the dataset and return the corresponding answers.

Key Components:
Dataset: The chatbot uses a CSV file (chatbot_data.csv) containing two columns: question and answer. The question column holds possible user inputs, and the answer column contains the corresponding responses.

Functionality:

get_response(user_input):
Converts the user's input to lowercase to ensure case-insensitive matching.
Uses the get_close_matches function from Python's difflib module to find the most similar question from the dataset.
If a match is found (with a minimum similarity threshold of 50%), the corresponding answer is retrieved and returned to the user.
If no match is found, the chatbot returns a default message: "I'm not sure how to answer that. Can you ask something else?"
User Interaction:

The chatbot prompts the user to ask a question.
The user's input is processed through the get_response function, and the chatbot either responds with a matching answer or asks the user to rephrase the question.
The chatbot continues the conversation until the user types 'exit', which ends the chat.
Key Features:
Simple String Matching: The chatbot uses a straightforward approach to find the closest question to the user's input. This allows the chatbot to handle slight variations in phrasing.
User-Friendly Interaction: The chatbot offers continuous dialogue until the user decides to quit, making it interactive and engaging.
CSV Data Source: The chatbot's knowledge base comes from a CSV file, making it easy to modify or expand by updating the dataset.
