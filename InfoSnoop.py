import requests
import json
import os
import configparser

#a Constants
API_URL = "https://api.proxynova.com/comb"
LIMIT = 100  # max results per request
CONFIG_FILE = "config.ini"

# Define ANSI escape codes for colors
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start_color, end_color):
    def interpolate(start, end, factor):
        return int(start + (end - start) * factor)

    length = len(text)
    result = ""

    for i, char in enumerate(text):
        factor = i / length
        r = interpolate(start_color[0], end_color[0], factor)
        g = interpolate(start_color[1], end_color[1], factor)
        b = interpolate(start_color[2], end_color[2], factor)
        result += rgb(r, g, b) + char

    return result + "\033[0m"  # Reset to default color

def hacker_green_text(text):
    return f"\033[38;2;0;255;0m{text}\033[0m"

def blood_red_text(text):
    return f"\033[38;2;139;0;0m{text}\033[0m"

def read_config():
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        return None
    config.read(CONFIG_FILE)
    return config['DEFAULT']['theme']

def save_config(theme):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'theme': theme}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def select_theme():
    print("Select a theme:")
    print("1. Gradient")
    print("2. Hacker Green Text")
    print("3. Blood Red Text")
    print("4. Normal (Plain)")
    choice = input("Enter your choice (1-4): ")

    themes = {
        '1': 'gradient',
        '2': 'hacker_green',
        '3': 'blood_red',
        '4': 'normal'
    }

    return themes.get(choice, 'normal')

def apply_theme(text, theme, start_color=(255, 0, 0), end_color=(0, 0, 255)):
    if theme == 'gradient':
        return gradient_text(text, start_color, end_color)
    elif theme == 'hacker_green':
        return hacker_green_text(text)
    elif theme == 'blood_red':
        return blood_red_text(text)
    else:
        return text

def search_query(query_value):
    params = {
        'query': query_value,
        'start': 0,
        'limit': LIMIT
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON response.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def print_results(results, theme):
    if results:
        print("Raw API Response:")
        print(apply_theme(json.dumps(results, indent=2), theme))  # Print the entire response with theme text

        if 'results' in results:
            for result in results['results']:
                print(apply_theme(json.dumps(result, indent=2), theme))
        else:
            print("No 'results' key found in the response.")
    else:
        print("No results found.")

def main():
    theme = read_config()
    if not theme:
        theme = select_theme()
        save_config(theme)

    print(apply_theme("Information obtained from https://www.proxynova.com/tools/comb\n", theme))
    print(apply_theme("To change the theme, delete the config.ini file\n", theme))

    while True:
        query_value = input(apply_theme("Enter target's email, username or a known password\n (or type 'exit' to quit): ", theme))
        
        if query_value.lower() == 'exit':
            break

        results = search_query(query_value)
        print_results(results, theme)

if __name__ == "__main__":
    main()
