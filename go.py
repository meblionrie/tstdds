import requests
from concurrent.futures import ThreadPoolExecutor
import time

def send_request(url):
    try:
        response = requests.get(url)
        # You can customize further based on your testing needs
        print(f"Request to {url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {str(e)}")

if __name__ == "__main__":
    # Get user input for testing parameters
    base_url = input("Enter the website URL to test: ")
    num_threads = int(input("Enter the number of threads: "))
    num_requests = int(input("Enter the number of requests: "))
    test_duration = int(input("Enter the time duration for testing (in seconds): "))
    
    # Create a list of URLs based on user input
    urls = [base_url] * num_requests
    
    # Measure the start time
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Run until either the specified duration is reached or all requests are sent
        while (time.time() - start_time) < test_duration:
            executor.map(send_request, urls)

    print(f"Testing completed in {time.time() - start_time:.2f} seconds.")
