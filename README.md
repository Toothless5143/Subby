# Subby
A simple tool written in python to enumerate live subdomains(both http & https). It uses the `requests` library to send HTTP requests to constructed subdomains of a given domain. It prompts the user to enter a domain and the path to a wordlist file containing subdomain names. It then reads the wordlist file, splits its content into individual subdomains, and iterates over each subdomain.

For each subdomain, the script constructs two URLs: one with "http://" and another with "https://". It then sends HTTP GET requests to these URLs using `requests.get()` and checks if the requests are successful (status code 200). If a request is successful (status code 200), it indicates that the subdomain exists, and the script prints the URL to the console.


### Installation
First clone the repo in your local machine, to do so follow the below command. <br>
```shell
git clone https://github.com/Toothless5143/Subby.git && cd Subby
```

Download all the requried modules.
```shell
pip install requests
```

Use the below command to launch the tool, and provide the main domain & wordlist:
```shell
python3 subby.py
```

### License
This tool is open source and available under the [MIT License.](/LICENSE)
