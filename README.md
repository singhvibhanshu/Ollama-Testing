# Ollama-Testing

## Description

This repository demonstrates everything you need to know to start using Ollama, a fantastic, free, open-source tool for managing and running LLMs (Large Language Models) locally. It ensures privacy, security, and, best of all, it's completely free!

## Installation Instructions

1. **Install Ollama:**

   - Download Ollama from [here](https://ollama.com).
   - Follow the installation steps for your operating system.

2. **Install Models:**

   - After successfully installing Ollama, you can now install various models and run them locally on your machine.
   - Refer to the official Ollama GitHub repository for detailed instructions: [Ollama GitHub](https://github.com/ollama/ollama).
   - Ensure you have enough RAM to run the models.
   - Explore available models from [Ollama's Model Library](https://ollama.com/library).
   - To install a model, run:
     ```bash
     ollama run <modelname>
     ```
   - To view all installed models, run:
     ```bash
     ollama list
     ```

3. **HTTP API Testing:**

   - Download the `sample-request.py` file from this repository.
   - If the file doesn’t run, install the `requests` module using:
     ```bash
     pip install requests
     ```
   - Run the sample file with:
     ```bash
     python sample-request.py
     ```

4. **Simpler Code Alternative:**

   - Use the `alt-sample-request.py` file for a simpler approach.
   - This file directly imports the `ollama` module. If you don’t have it installed, run:
     ```bash
     pip install ollama
     ```

5. **Customization:**

   - You can customize models to behave in specific ways. For example, a model that generates responses like Mario.
   - Refer to the `mario-modelfile` in this repository.
     - Specify the model (e.g., `llama2` for testing purposes).
     - Add commands to customize responses.
   - To create a model using the `mario-modelfile`, run:
     ```bash
     ollama create <modelname> -f <location_of_model_file>
     ```
     Example:
     ```bash
     ollama create test-model -f ./mario-modelfile
     ```
   - To run your custom model, use:
     ```bash
     ollama run <modelname>
     ```
     Example:
     ```bash
     ollama run test-model
     ```

6. **Removing Models:**

   - To remove a model, run:
     ```bash
     ollama rm <modelname>
     ```

## Usage

You can use this repository and its examples for personal reference and to explore the capabilities of Ollama. It’s an excellent starting point for anyone looking to manage and customize LLMs locally.

---

Feel free to reach out for further assistance or suggestions!

Thanks for visiting my repo. If you like my work you can consider giving this repo a star