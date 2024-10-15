import pandas as pd
from difflib import get_close_matches

# Load the dataset
data = pd.read_csv('chatbot_data.csv')  # Ensure this path is correct


def get_response(user_input):
    """Get the response from the chatbot based on user input."""
    user_input = user_input.lower()  # Convert user input to lowercase

    # Extracting the questions from the dataset for matching
    questions = data['question'].str.lower().tolist()

    # Get the closest matches from the dataset
    closest_matches = get_close_matches(user_input, questions, n=1, cutoff=0.5)

    if closest_matches:
        # If there is a close match, return the corresponding answer
        matched_index = questions.index(closest_matches[0])
        return data['answer'].iloc[matched_index]

    return "I'm not sure how to answer that. Can you ask something else?"


def chatbot():
    print("Chatbot: Hi! Ask me anything (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot()
