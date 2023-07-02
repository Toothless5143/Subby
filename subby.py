import requests

# Prompt the user to enter the domain
domain = input("Enter domain: ")

# Prompt the user to enter the path to the wordlist file
wordlist_path = input("Enter the path to the wordlist file: ")

# Read the wordlist file
with open(wordlist_path, 'r') as file:
    content = file.read()

# Split the wordlist content into individual subdomains
subdomains = content.splitlines()

# Iterate over each subdomain
for subdomain in subdomains:
    # Construct URLs using subdomain and domain
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    
    try:
        # Send HTTP requests to the URLs
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        
        # Check if the requests are successful (status code 200)
        if response1.status_code == 200:
            print(url1)
        
        if response2.status_code == 200:
            print(url2)
    except requests.ConnectionError:
        # Ignore connection errors
        pass
