# Load data
def load_data():
    with open('openwebtext.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Load the entire dataset
data = load_data()

# Split into training and testing sets
train_ratio = 0.8  # 80% for training, 20% for testing
train_size = int(len(data) * train_ratio)

train_data = data[:train_size]
test_data = data[train_size:]

# Save training data to a file
with open('train_data.txt', 'w', encoding='utf-8') as file:
    file.write(train_data)

# Save testing data to a file
with open('test_data.txt', 'w', encoding='utf-8') as file:
    file.write(test_data)
