# auto_completion.py
import streamlit as st

# Load data
@st.cache_data
def load_data():
    with open('train_data.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Create n-grams
def create_ngrams(text, n=2):
    ngrams = {}
    words = text.split()
    for i in range(len(words)-n+1):
        context = ' '.join(words[i:i+n-1])
        if context not in ngrams:
            ngrams[context] = []
        ngrams[context].append(words[i+n-1])
    return ngrams

# Auto-completion function
def auto_complete(text, ngrams, n=2):
    context = ' '.join(text.split()[-(n-1):])
    suggestions = ngrams.get(context, [])
    return suggestions

# Load data
data = load_data()

# Sidebar for user input
#st.sidebar.header("Auto-Completion")
#text_input = st.sidebar.text_input("Enter text:", "I love")

# Select n-gram model
n_gram_model = st.sidebar.selectbox("Select N-gram Model", ["Unigram", "Bigram", "Trigram", "N-gram"])

# Define n-gram value based on user's choice
if n_gram_model == "Unigram":
    n = 1
elif n_gram_model == "Bigram":
    n = 2
elif n_gram_model == "Trigram":
    n = 3
else:
    n = st.sidebar.number_input("Enter value of N:", 4, 10, 5)  # For custom N-gram

# Create n-grams
ngrams = create_ngrams(data, n=n)  # Pass the loaded data as text

# Auto-completion
#suggestions = auto_complete(text_input, ngrams, n=n)

# Display suggestions with enhanced style
st.title("Text Auto-Completion")

# Display n-gram choice
st.sidebar.write(f"Selected N-gram Model: {n_gram_model}")

# Sidebar for user input
st.sidebar.header("User Input")
text_input = st.sidebar.text_area("Enter text:", "I love")

# Create n-grams
ngrams = create_ngrams(data, n=n)

# Auto-completion
suggestions = auto_complete(text_input, ngrams, n=n)

# Display suggestions
if suggestions:
    st.success("Suggestions for completion:")
    st.write(', '.join(suggestions))
else:
    st.info("No suggestions available.")

# Add some space for better appearance
st.markdown("---")
st.markdown("*Made with ❤️ by BHAVYA*")
