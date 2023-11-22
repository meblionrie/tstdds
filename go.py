
import requests
from concurrent.futures import ThreadPoolExecutor

def send_request(url):
    try:
        response = requests.get(url)
        # You can customize further based on your testing needs
        print(f"Request to {url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {str(e)}")

if __name__ == "__main__":
    # Replace 'http://example.com' with your server's URL
    base_url = 'http://example.com'
    
    # Number of requests to send
    num_requests = 1000000
    
    # Adjust the number of threads based on your system capabilities
    num_threads = 50

    urls = [base_url] * num_requests

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(send_request, urls)
