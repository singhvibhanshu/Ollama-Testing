import ollama  # Import the Ollama library to interact with the API

# Initialize the Ollama client for communicating with the API
client = ollama.Client()

# Define the model to use and the input prompt for the query
model = "llama2"  # Specify the model name (e.g., "llama2")
prompt = "Who is the current PM of India?"  # Define the user's input question

# Send the query to the specified model and get the response
response = client.generate(model=model, prompt=prompt)

# Print the response received from the model
print("Response from Ollama:")
print(response.response)  # Access and display the response content
