# Microsoft Summer Internship 2026 Application Tool
## How my Application works

To make the application works perfectly, the system must follow strict steps for Processing. Here is my strategy:

- 1. **Parse input**: First step, the app will read the file from the command line argument that the user give it.
- **2. Validate presence of a function:** I use a library called Pygments to lex the code and check if there is a function.
- **3. Remove any Comments or docstrings:** then I use Pygments to remove all the comments and docstring to avoid prompt injection
- 4. Send request to LLM API: After the code is clean, I send request to LLM API. I chose the Google Gemini model.
- 5. Constrain model with a system prompt: I write a very strict system prompt telling the AI to only write code.
- **6. Enforce deterministic output:** I used LangChain structured output with Pydantic to force the format. The Output must return tests only: no explanation, no markdown, no commentary, and no extra text.
- **7. second firewall:**  I also added a second Regex fallback to add 2nd level of security to format the output in the desire format in the case that the LLM hallucinate

## How to Install

The App is written in Python, so please make sure you have Python 3.12 or newer installed on your laptop.

1. First, clone this repo to your machine.
2. Open your terminal and go to the project folder.
3. Run `pip install -r requirements.txt` to install LangChain, Pygments, and dotenv.
4. Now for the environment variables. You can type the secrets (.env file) in the form. You have to create a new `.env` file in the root directory. write Google API key  in it like this: `GOOGLE_API_KEY="api_key"`
## How to use my Application

You just need to run the `main.py` file and give it the path of your code file.

Type this command in your terminal: `python main.py path/to/your_test_file.py`

For example, if you run `python main.py test_1.java`, it will read the Java file, parse it, and print JUnit tests in the terminal without any chat talk. If you run `python main.py test_2.txt` which just has 'hello world', it will fail. I already upload some test cases as an example.

Thanks a lot for this opportunity
