from transformers import pipeline

# Text generation pipeline with specific model (gpt2)
generator = pipeline("text-generation", model="gpt2")

# Prompt de rahe hain
prompt = "Artificial Intelligence will transform the future because"

# Text generate karte hain
output = generator(prompt, max_length=50, num_return_sequences=1)

print("\n--- Generated Text ---")
print(output[0]['generated_text'])