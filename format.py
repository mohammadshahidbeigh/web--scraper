import re

def format_text(input_file, output_file):
    try:
        # Read content from the input file
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Apply formatting rules
        # Example: Add line breaks after periods, question marks, and exclamation marks
        formatted_content = re.sub(r'(?<=[.!?])\s+', '\n', content)

        # Remove excessive whitespace
        formatted_content = re.sub(r'\n{3,}', '\n\n', formatted_content)  # Remove consecutive line breaks

        # Write the formatted content to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_content)

        print("Text file formatted successfully.")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Example usage:
input_file = "scraped__data.txt"
output_file = "output.txt"
format_text(input_file, output_file)
