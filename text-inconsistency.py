import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline
import random

nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Problem Definition
# Detecting and converting negative sentences into positive ones

# Step 2: Dataset Collection
# Creating synthetic data with 1000 sentences
def generate_synthetic_sentences(size):
    sentences = []
    for i in range(size):
        if i % 2 == 0:
            sentences.append(f"This is a negative statement number {i}, indicating a problem.")
        else:
            sentences.append(f"This is a positive statement number {i}, reflecting a solution.")
    return sentences

large_data = generate_synthetic_sentences(1000)

# Convert the dataset into a DataFrame
df = pd.DataFrame(large_data, columns=["text"])

# Step 3: Data Preprocessing
def preprocess_text(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    # Simple tokenization without sent_tokenize
    words = text.split()  
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return " ".join(words) 
# def preprocess_text(text):
#     stop_words = set(stopwords.words('english'))
#     words = word_tokenize(text)
#     words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
#     return " ".join(words)

df['cleaned_text'] = df['text'].apply(preprocess_text)

# Step 4: Sentence Transformation using Hugging Face
# Load the pipelines outside the loop for efficiency
positivity_detector = pipeline("sentiment-analysis")
transformer = pipeline("text2text-generation", model="google/flan-t5-base")

# Function to detect and transform sentences with additional validation
def detect_and_transform(sentence):
    try:
        input_text = f"Turn this negative statement into a positive one, keeping its meaning: {sentence}"
        result = transformer(input_text, max_length=50, truncation=True)
        positive_sentence = result[0]['generated_text'].strip()
        # Validate output to ensure transformation
        if positive_sentence.lower() == sentence.lower():
            # Retry with a different prompt if transformation failed
            input_text_retry = f"Rewrite negatively phrased sentence to sound positive: {sentence}"
            result_retry = transformer(input_text_retry, max_length=50, truncation=True)
            positive_sentence = result_retry[0]['generated_text'].strip()
        if positive_sentence.lower() == sentence.lower():
            return "Could not transform the sentence. Please try rephrasing."
        return positive_sentence
    except Exception as e:
        return f"Error transforming sentence: {e}"

# Step 5: User Input for Real-Time Detection and Conversion
while True:
    user_input = input("Enter a sentence (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    sentiment = positivity_detector(user_input)[0]
    if sentiment['label'] == 'NEGATIVE':
        print("Detected negative sentiment.")
        transformed_sentence = detect_and_transform(user_input)
        print(f"Original negative sentence: {user_input}")
        print(f"Transformed to positive: {transformed_sentence}\n")
    else:
        print(f"The sentence is already positive: {user_input}\n")

# Expected Outcomes
# The system will detect whether a sentence is negative and, if so, convert it to a positive one.