import requests  # Import the requests library for handling HTTP requests
import json      # Import the json library for working with JSON data

# Define the base URL for the local Ollama API endpoint
url = "http://localhost:11434/api/chat"

# Define the payload, which includes the model and the user's input
payload = {
    "model": "llama2",  # Specify the model to be used (e.g., "llama2")
    "messages": [{"role": "user", "content": "What is Blackhole?"}]  # User's input prompt
}

# Send an HTTP POST request to the Ollama API, enabling streaming for response
response = requests.post(url, json=payload, stream=True)

# Check if the API request was successful (HTTP status code 200)
if response.status_code == 200:
    print("Streaming response from Ollama:")
    # Iterate over each line in the streamed response
    for line in response.iter_lines(decode_unicode=True):
        if line:  # Process non-empty lines only
            try:
                # Attempt to parse the line as a JSON object
                json_data = json.loads(line)
                # Check if the parsed JSON contains a message with content
                if "message" in json_data and "content" in json_data["message"]:
                    # Print the assistant's response content without adding newlines
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:  # Handle JSON parsing errors
                print(f"\nFailed to parse line: {line}")
    print()  # Add a final newline after the complete response
else:
    # Print the error status and response content if the API call fails
    print(f"Error: {response.status_code}")
    print(response.text)
