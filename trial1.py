import os

data_folder = 'openwebtext-master'
output_file = 'openwebtext.txt'

all_text = ''
num_files = 0

for subdir, _, files in os.walk(data_folder):
    for file in files:
        with open(os.path.join(subdir, file), 'r', encoding='utf-8', errors='ignore') as f:
            all_text += f.read()
            num_files += 1

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"Combined {num_files} files into {output_file}")

# auto_completion.py
import streamlit as st

# Load data
@st.cache_data
def load_data():
    with open('openwebtext.txt', 'r', encoding='utf-8') as file:
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
st.sidebar.header("Auto-Completion")
text_input = st.sidebar.text_input("Enter text:", "I love")

# Create n-grams
ngrams = create_ngrams(data)  # Pass the loaded data as text

# Auto-completion
suggestions = auto_complete(text_input, ngrams)

# Display suggestions with enhanced style
st.write("## Suggestions for Completion")
if suggestions:
    st.success(', '.join(suggestions))
else:
    st.info("No suggestions available.")

# Add some space for better appearance
st.markdown("---")
st.markdown("*Made with ❤️ by BHAVYA*")
