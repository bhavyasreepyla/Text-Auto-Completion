def load_data():
    with open('openwebtext.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text
