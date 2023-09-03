# Subby

The Subby is a robust Python tool designed to enumerate live subdomains for a given domain. By utilizing the `requests` library, this tool sends HTTP requests to constructed subdomains of the target domain. It prompts the user to enter the domain and the path to a wordlist file containing subdomain names. The tool reads the wordlist file, splits its content into individual subdomains, and iterates over each subdomain.

For each subdomain, the tool constructs two URLs: one with "http://" and another with "https://". It then sends HTTP GET requests to these URLs using `requests.get()` and checks if the requests are successful (status code 200). If a request is successful, indicating that the subdomain exists, the tool prints the URL to the console.

## Features

- Simple and effective subdomain enumeration tool.
- Enumerates both HTTP and HTTPS subdomains.
- Utilizes a wordlist file to generate subdomains for scanning.
- Provides clear output of discovered subdomains.

## Installation

To install and run the Subdomain Enumerator tool, follow these steps:

1. Clone the repository to your local machine using the following command:
   ```shell
   git clone https://github.com/Toothless5143/Subby.git && cd Subby
   ```

2. Install the required modules by executing the following command:
   ```shell
   pip install requests
   ```

3. Launch the tool and provide the main domain and wordlist by running the following command:
   ```shell
   python3 subby.py
   ```

## License

This tool is open source and available under the [MIT License](/LICENSE).

