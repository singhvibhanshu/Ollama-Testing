# Ollama-Testing

## Description

This repository provides a comprehensive guide to getting started with Ollama, a powerful, free, open-source tool for managing and running Large Language Models (LLMs) locally. Ollama prioritizes privacy, security, and accessibility—and it’s entirely free to use.

## Installation Instructions

### 1. Install Ollama
   - Download Ollama from [the official website](https://ollama.com).
   - Follow the installation steps specific to your operating system.

### 2. Install Models
   - After installing Ollama, you can explore and install various models to run locally.
   - Check detailed instructions on the official Ollama GitHub repository: [Ollama GitHub](https://github.com/ollama/ollama).
   - Ensure your machine meets the hardware requirements (e.g., sufficient RAM) for running models.
   - Browse available models in [Ollama’s Model Library](https://ollama.com/library).
   - To install a model, use the following command:
     ```bash
     ollama run <modelname>
     ```
   - To list all installed models, use:
     ```bash
     ollama list
     ```

### 3. HTTP API Testing
   - Download the `sample-request.py` file from this repository.
   - If necessary, install the `requests` module with:
     ```bash
     pip install requests
     ```
   - Run the sample file using:
     ```bash
     python sample-request.py
     ```

### 4. Simpler Code Alternative
   - Use the `alt-sample-request.py` file for a more straightforward approach.
   - This file imports the `ollama` module directly. Install it using:
     ```bash
     pip install ollama
     ```

### 5. Customization
   - Customize models to suit specific needs. For example, you can create a model that generates responses as if it were a character like Mario.
   - Refer to the `mario-modelfile` included in this repository for customization examples.
     - Specify the base model (e.g., `llama2`).
     - Add commands to configure responses.
   - To create a customized model, use:
     ```bash
     ollama create <modelname> -f <path_to_model_file>
     ```
     Example:
     ```bash
     ollama create test-model -f ./mario-modelfile
     ```
   - Run your custom model with:
     ```bash
     ollama run <modelname>
     ```
     Example:
     ```bash
     ollama run test-model
     ```

### 6. Removing Models
   - To delete a model, use:
     ```bash
     ollama rm <modelname>
     ```

## Usage

This repository serves as a practical reference for exploring Ollama’s capabilities. Use it to:
- Install and manage models locally.
- Customize models to create unique behaviors.
- Experiment with HTTP API integrations.

Feel free to fork this repository and make modifications as needed.

---

If you find this repository helpful, please consider giving it a star. Your feedback and contributions are welcome!

