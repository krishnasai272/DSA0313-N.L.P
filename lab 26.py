from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Loading model... please wait")

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = "Machine learning is powerful"

inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs)

translated = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Translated Text:", translated)
