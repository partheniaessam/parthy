import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

# Read the text file
with open('C:\\Users\\Administrator\\Desktop\\random_paragraphs.txt', 'r') as file:
    text = file.read()

# Convert text to lowercase
text = text.lower()

# Tokenize the text into words
words = word_tokenize(text)

# Remove Stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Calculate word frequency
word_freq = Counter(filtered_words)

# Display word frequency
for word, freq in word_freq.items():
    print(f'{word}: {freq}')
