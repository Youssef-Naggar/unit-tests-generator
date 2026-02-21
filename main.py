import argparse
import sys
import os
from dotenv import load_dotenv

from input_firewall import InputCleaner, FunctionValidator
from brain import Brain
from output_formatter import OutputFormatter


def main():
    load_dotenv()

    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not found in .env file.")
        sys.exit(1)

    # take input
    parser = argparse.ArgumentParser(description="Generate unit tests for a given function.")
    parser.add_argument("filepath", type=str, help="Path to the source code file")
    args = parser.parse_args()

    try:
        with open(args.filepath, 'r', encoding='utf-8') as file:
            source_code = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    # check if there is a function
    validator = FunctionValidator()
    if not validator.has_function(args.filepath, source_code):
        print("Error: This tool only generates unit tests for functions.")
        sys.exit(1)

    # clean input to avoid prompt injection
    cleaner = InputCleaner()
    cleanup_code = cleaner.clean(args.filepath, source_code)

    orchestrator = Brain()
    try:
        raw_output = orchestrator.generate_tests(cleanup_code)
    except Exception as e:
        print(f"Error generating tests: {e}")
        sys.exit(1)

    formatter = OutputFormatter()
    final_test_code = formatter.format(raw_output)

    print(final_test_code)


if __name__ == "__main__":
    main()