import nltk
import re
import string  

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer 

# =====================
# INPUT TEXT (thông tin của bạn)
# =====================
text = (
    "My name is Cong Phuc. I am a student. "
    "I like learning Computational Linguistics because it is interesting and useful. "
    "This is my friend Minh Anh. She is kind and helpful."
)

# In văn bản gốc
print("ORIGINAL TEXT:\n", text)
print("-" * 60)

# Tokenization
tokens = word_tokenize(text)
print("TOKENS:\n", tokens)
print("-" * 60)

# Lowercasing
lower_tokens = [token.lower() for token in tokens]
print("LOWERCASED TOKENS:\n", lower_tokens)
print("-" * 60)
# =====================
# Stopword Removal
# =====================
stop_words = set(stopwords.words('english'))

filtered_tokens = [
    token for token in lower_tokens
    if token not in stop_words
]

print("FILTERED TOKENS (STOPWORDS REMOVED):\n", filtered_tokens)
print("-" * 60)

# =====================
# Punctuation Removal
# =====================
punctuation_table = str.maketrans("", "", string.punctuation)

punctuation_free_tokens = [
    token.translate(punctuation_table)
    for token in filtered_tokens
    if token.translate(punctuation_table) != ""
]

print("PUNCTUATION-FREE TOKENS:\n", punctuation_free_tokens)
print("-" * 60)
