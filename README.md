# InfoSnoop

## Disclaimer

This tool is for educational purposes only. The developers are not responsible for any misuse of this tool. Do not use this tool for illegal activities.

## Introduction

InfoSnoop is a powerful and versatile info-gathering tool designed for cybersecurity enthusiasts, ethical hackers, and penetration testers. With InfoSnoop, you can search for sensitive information such as usernames, emails, and known passwords across multiple platforms with ease and efficiency. The tool supports various themes for a customizable user experience.

## Features

- Search by username, email, or known password.
- Customizable themes: Gradient, Hacker Green, Blood Red, Normal.
- Save user preferences to a config file.
- Easy-to-use terminal interface.
- Retrieves and displays results from the ProxyNova API.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/un1xr00t/InfoSnoop.git
    cd InfoSnoop
    ```

2. Create and activate a virtual environment **(OPTIONAL)**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script:

```sh
python3 InfoSnoop.py

## Tips

If you want to change to a different theme, go to the directory that InfoSnoop.py is in and delete 'config.ini'. This will allow you to change the theme the next time you launch InfoSnoop.py.
