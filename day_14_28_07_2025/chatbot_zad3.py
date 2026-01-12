from transformers import pipeline
# pip install tf-keras
# chatbot = pipeline("text-generation",
#                    model="mistralai/Ministral-3-3B-Base-2512")
# chatbot = pipeline(
#     "text-generation",
#     model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     device_map="auto"
# )
# response = chatbot("Cześć, jak mogę Ci pomóc?")
# print(response)
# print(response[0]['generated_text'])
#
# chatbot = pipeline(
#     "text-generation",
#     model="distilgpt2",
#     device_map="auto"
# )
#
# response = chatbot(
#     "Cześć, jak mogę Ci pomóc?",
#     max_new_tokens=50
# )

# print(response[0]["generated_text"])
chatbot = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device_map="auto"
)

prompt = "<|user|>Cześć, jak mogę Ci pomóc?<|assistant|>"

response = chatbot(
    prompt,
    max_new_tokens=80,
    temperature=0.7,
    top_p=0.9
)

print(response[0]["generated_text"])