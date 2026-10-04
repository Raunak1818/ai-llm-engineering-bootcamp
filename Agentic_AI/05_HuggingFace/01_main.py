from transformers import pipeline

# Sentiment Analysis pipeline initialize ho raha hai
classifier = pipeline("sentiment-analysis")

# Text analyze kar rahe hain
result = classifier("I am learning Hugging Face and it is working smoothly!")

print("\n--- Output ---")
print(result)