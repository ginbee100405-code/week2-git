import re
import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


# ============================
# Download required NLTK resources (run once)
# ============================
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")


# ============================
# Input Text (~50 words, diverse characters)
# ============================
text = (
    "Hi! My name is Cong Phuc (ID: 2026). I'm 20 years old; email: congphuc2026@gmail.com. "
    "I study Computational Linguistics and I love Python. My goals: learn NLP fast, build projects, "
    "and share results on GitHub! Symbols: ! @ # $ % ^ & * ( ) _ + - = { } [ ] | \\ : ; \" ' < > , . ? /"
)

print("INPUT TEXT:\n", text)
print("-" * 60)


# ============================
# 1) Tokenization
# ============================
tokens = word_tokenize(text)
print("TOKENS:\n", tokens)
print("-" * 60)


# ============================
# 2) Lowercasing
# ============================
lower_tokens = [t.lower() for t in tokens]
print("LOWERCASED TOKENS:\n", lower_tokens)
print("-" * 60)


# ============================
# 3) Stopword Removal
# ============================
stop_words = set(stopwords.words("english"))
filtered_tokens = [t for t in lower_tokens if t not in stop_words]
print("FILTERED TOKENS (STOPWORDS REMOVED):\n", filtered_tokens)
print("-" * 60)


# ============================
# 4) Punctuation Removal
# ============================
punctuation_table = str.maketrans("", "", string.punctuation)
punctuation_free_tokens = [
    t.translate(punctuation_table) for t in filtered_tokens if t.translate(punctuation_table) != ""
]
print("PUNCTUATION-FREE TOKENS:\n", punctuation_free_tokens)
print("-" * 60)


# ============================
# 5) Stemming
# ============================
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(t) for t in punctuation_free_tokens]
print("STEMMED TOKENS:\n", stemmed_tokens)
print("-" * 60)


# ============================
# 6) Lemmatization
# ============================
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(t) for t in punctuation_free_tokens]
print("LEMMATIZED TOKENS:\n", lemmatized_tokens)
print("-" * 60)


# ============================
# 7) Text Normalization
# (ở đây: dùng lemmatized_tokens làm normalized_tokens)
# ============================
normalized_tokens = lemmatized_tokens
final_normalized_string = " ".join(normalized_tokens)

print("FINAL NORMALIZED STRING:\n", final_normalized_string)
print("-" * 60)


# ============================
# 8) Regex-based Extraction (3 info: Name, Age, Email)
# ============================

# Email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Age (ví dụ: "20 years old")
age_pattern = r"\b(\d{1,3})\s*(?:years?\s*old|y/o)\b"
ages = re.findall(age_pattern, text)

# Name (bắt tên dạng 2-3 từ viết hoa chữ cái đầu)
name_pattern = r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2}\b"
names = re.findall(name_pattern, text)

print("EXTRACTED EMAILS:\n", emails)
print("EXTRACTED AGES:\n", ages)
print("EXTRACTED NAMES:\n", names)
print("-" * 60)
