import requests
 def main():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    
    print("Status code :", response.status_code)
    print("Response content :", response.text)
    
if __name__ == "__main__":
    main()