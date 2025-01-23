import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Ensure required NLTK resources are downloaded
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Predefined dataset of question-answer pairs
qa_pairs = {
    "what is your name": "I am an AI-powered chatbot!",
    "how are you": "I'm just a bunch of code, but I'm here to help you!",
    "what can you do": "I can answer your questions, generate reports, and much more!",
    "who created you": "I was created using Python and NLP libraries like NLTK!",
    "bye": "Goodbye! Have a great day!"
}

# Preprocessing function
def preprocess_input(user_input):
    # Convert to lowercase
    user_input = user_input.lower()
    # Tokenize
    tokens = word_tokenize(user_input)
    # Remove punctuation and stopwords
    tokens = [word for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

# Chatbot function
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Preprocess user input
        processed_input = preprocess_input(user_input)

        # Find the most relevant response
        response = None
        for question, answer in qa_pairs.items():
            if processed_input in preprocess_input(question):
                response = answer
                break

        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()