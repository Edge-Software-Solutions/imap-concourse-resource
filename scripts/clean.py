import sys
from bs4 import BeautifulSoup

def remove_html_tags(file_name):
    # Read the email content from file
    with open(file_name, "r") as file:
        email_content = file.read()

    # Parse email content
    soup = BeautifulSoup(email_content, 'html.parser')

    # Get text from parsed HTML content
    text = soup.get_text()

    return text

if __name__ == "__main__":
    # Check if file name is passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    cleaned_text = remove_html_tags(file_name)

    print(cleaned_text)
