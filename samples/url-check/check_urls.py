import requests
import logging

# Configure logging
logging.basicConfig(
    filename='url_check.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def check_url_accessibility(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout for the request
        if response.status_code == 200:
            logging.info(f"Accessible: {url}")
            return True  # URL is accessible
        else:
            logging.warning(f"Inaccessible (status code {response.status_code}): {url}")
            return False  # URL returned a non-200 status code
    except requests.RequestException as e:
        logging.error(f"Error accessing {url}: {e}")
        return False  # URL is not accessible due to an exception

def check_urls_in_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    accessible_urls = []
    inaccessible_urls = []

    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if check_url_accessibility(url):
            accessible_urls.append(url)
        else:
            inaccessible_urls.append(url)

    logging.info(f"Total accessible URLs: {len(accessible_urls)}")
    logging.info(f"Total inaccessible URLs: {len(inaccessible_urls)}")

    return accessible_urls, inaccessible_urls

accessible_urls, inaccessible_urls = check_urls_in_file('./URLs.txt')
# Example usage:
# file_path = "URLs.txt"
# accessible_urls, inaccessible_urls = check_urls_in_file(file_path)