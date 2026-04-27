# Chapter 1 — Python Basics
# Topics: data types, variables, print(), f-strings, type conversion

# --- Data Types ---
age = 25            # int
learning_rate = 0.001   # float
model_name = "ResNet50"  # string
is_training = True       # boolean

# --- print() and f-strings ---
print(f"Model: {model_name}")
print(f"Learning rate: {learning_rate}")
print(f"Training mode: {is_training}")

# --- Type conversion ---
score = 0.94
print("Accuracy: " + str(score))

# --- len() ---
print(len(model_name))  # Output: 8

# Variables — storing values in memory. A variable is a named container.
# Variable naming rules: lowercase, use underscores, be descriptive. learning_rate not lr2 — your future self will thank you.

model = "ResNet50"
batch_size = 32
dropout = 0.5
is_training = True

# Variables can be updated
batch_size = 64
print(batch_size)

print("Training started...")
print("Accuracy:", 0.94)
print("Epoch", 3, "of", 10)

# f-strings (the clean way)
epoch = 3
acc = 0.94
print(f"Epoch {epoch} — accuracy: {acc}")


first = "neural"
second = "network"

# Concatenation — joining strings
full = first + " " + second
print(full)  # → "neural network"

# Length
print(len("transformer"))  # → 11

# Type conversion
score = 0.95
print("Score: " + str(score))  # str() converts float to string


# Chapter 1 Mini Project — variables, data types, f-strings
name = "Sara"
model = "ResNet50"
accuracy = 94.0  # float — accuracy is always a decimal in ML

print(f"Trained by {name} — Model: {model} — Accuracy: {accuracy}%")
