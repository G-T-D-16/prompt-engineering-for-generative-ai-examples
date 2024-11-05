import requests
import re
from bs4 import BeautifulSoup


def fetch_document_content(url):
    # Fetch the content of the Google Docs URL
    response = requests.get(url)

    # Debugging: Check the status and content type of the response
    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    # Raise an error if the response is not successful
    response.raise_for_status()

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all visible text from the HTML
    content = soup.get_text(separator='\n')

    # Debug: Print the extracted text to inspect its structure
    print("Extracted Text Content (first 1000 characters):\n", content[:1000])
    return content


def parse_characters(content):
    # Split content into lines
    lines = content.splitlines()

    characters = []
    i = 0
    while i < len(lines):
        # Try to find patterns like x-coordinate, character, y-coordinate in sequence
        if re.match(r'^\d+$', lines[i]):  # x-coordinate (line with just a number)
            x = int(lines[i])
            if i + 1 < len(lines) and len(lines[i + 1]) == 1:  # Character (1-character line)
                char = lines[i + 1]
                if i + 2 < len(lines) and re.match(r'^\d+$', lines[i + 2]):  # y-coordinate
                    y = int(lines[i + 2])
                    characters.append((char, x, y))
                    i += 3  # Move to the next set of data
                    continue
        i += 1

    if not characters:
        raise ValueError("No characters were found in the document. Please check the document format.")

    return characters


def create_grid(characters):
    # Determine the grid size based on the maximum x and y coordinates
    max_x = max(char[1] for char in characters)
    max_y = max(char[2] for char in characters)

    # Initialize the grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place each character in its specified position, inverting the y-coordinate
    for char, x, y in characters:
        grid[max_y - y][x] = char  # Invert y-coordinate to align top-down

    return grid


def print_grid(grid):
    # Print each row in the grid
    for row in grid:
        print(''.join(row))


def decode_message(url):
    # Step 1: Fetch document content
    content = fetch_document_content(url)

    # Step 2: Parse characters and their coordinates
    characters = parse_characters(content)

    # Step 3: Create the grid and populate it
    grid = create_grid(characters)

    # Step 4: Print the grid to display the secret message
    print_grid(grid)


# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_message(url)
