# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTION

*NAME*: YOGESH YADAV

*INTERN ID*: CT08IFE

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

Creating a Chatbot with Natural Language Processing*

I developed a chatbot using Python along with Natural Language Processing (NLP) libraries, specifically NLTK. The chatbot was designed to engage with users, understand their text inputs, and offer relevant responses drawn from a set list of question-answer pairs. This task showed how well NLP can work with user interactions, highlighting Python's ability to create smart systems.

*Goal*
The main goal was to build a chatbot that could understand what users were saying and reply in a fitting way. The chatbot's replies were based on a prepared dataset of usual questions and answers. The task also aimed to look into basic NLP methods for cleaning up text data to make matching more accurate.

*Tools and Libraries Used*
1. *Python*: I chose Python for its ease of use and the large variety of NLP libraries available.
2. *NLTK*:
   - It was used for breaking down user input into smaller parts, like words.
   - It also helped in removing common words and simplifying text to improve matching.
3. *Difflib*:
   - The `get_close_matches` function was used for fuzzy matching, enabling the chatbot to find the closest question even when the user's input wasn't exact.
4. *Integrated Development Environment (IDE)*:
   - I used **Visual Studio Code (VS Code)** for developing the chatbot, taking advantage of its debugging features and Python support.

*Steps Taken*
1. *Creating a Predefined Dataset*:
   - I established a list of common questions and their answers in a dictionary format. Some examples are:
     - "What is your name?" → "I am an AI-powered chatbot!"
     - "What can you do?" → "I can answer your questions, create reports, and more!"
   - This dataset served as the chatbot's knowledge base.

2. *Processing User Input*:
   - To prepare the user input for matching, several steps were necessary:
     - *Lowercasing*: Transforming all text to lowercase to avoid issues with case sensitivity.
     - *Tokenization*: Separating sentences into individual words using NLTK's `word_tokenize`.
     - *Stopword Removal*: Getting rid of less meaningful words (like "is" and "the") to keep the focus on the important parts.
     - *Lemmatization*: Changing words to their base forms (for instance, "running" becomes "run") for consistency.

3. *Matching User Input with Predefined Questions*:
   - The chatbot used the `get_close_matches` function to identify the closest predefined question based on the processed input. This way, it could handle minor differences or mistakes in the user input (like "What is your name?" vs. "What's your name?").
   - If no close match was found, it would reply with: "I'm sorry, I didn't understand that."

4. *Engaging in Chat*:
   - The chatbot functioned in a loop, allowing users to chat back and forth until they typed "bye" to finish the conversation.

5. *Handling Errors*:
   - I set up error handling to make sure that invalid inputs or unexpected issues wouldn’t crash the chatbot.

*Uses*
This chatbot can be applied in various real-life situations:
1. *Customer Support*:
   - It can act as a first point of contact for businesses, answering FAQs and directing users to helpful resources.
2. *Educational Tools*:
   - Functions as a teaching assistant, responding to student inquiries or offering tutorials.
3. *Virtual Assistants*:
   - Aids in scheduling, reminders, or addressing simple queries in personal assistant settings.
4. *Prototype Development*:
   - Acts as a foundation for creating more advanced AI chatbots with larger datasets and sophisticated models.

*Challenges and Learning*
- Making sure the chatbot accurately responded to similar but not identical questions required careful preprocessing and fuzzy matching techniques.
- This task highlighted how essential NLP methods are in creating smoother and more efficient interactions.

*Conclusion*
This task showcased how to combine NLP with Python to create an interactive chatbot. It illustrated how preprocessing and tools like `NLTK` and `Difflib` can improve the chatbot's performance. The design of the chatbot allows it to be expanded further, providing opportunities for use in customer service, education, and virtual assistance.
