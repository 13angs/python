# URL Accessibility Checker

This Python script checks the accessibility of image URLs listed in a `URLs.txt` file. The script reads each URL from the file, sends an HTTP GET request, and logs whether the URL is accessible or not. Comprehensive logging is implemented to record the status of each URL and any errors encountered during the process.

## Features

- **URL Accessibility Check**: The script verifies whether each URL in `URLs.txt` is accessible (returns HTTP status code 200).
- **Error Handling**: Handles exceptions such as connection timeouts, invalid URLs, and other request-related errors gracefully.
- **Comprehensive Logging**: Logs detailed information about the accessibility of each URL, including a summary of accessible and inaccessible URLs.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

1. **Prepare the `URLs.txt` File**: Create a text file named `URLs.txt` in the same directory as the script. This file should contain one URL per line.

Example `URLs.txt`:

```
https://example.com/image1.jpg
https://example.com/image2.png
https://nonexistent.com/image.jpg
```

2. **Run the Script**: Execute the script by running the following command in your terminal:

```bash
python check_urls.py
```


3. **Check the Logs**: After the script has finished running, check the `url_check.log` file in the same directory for the results. The log file will contain detailed information about each URL's accessibility.

## Logging Details

The script logs the following information:

- **Accessible URLs**: Logged with the message `Accessible: {url}`.
- **Inaccessible URLs**: Logged with the message `Inaccessible (status code {status_code}): {url}`.
- **Errors**: If an exception occurs, the error is logged with the message `Error accessing {url}: {exception_message}`.
- **Summary**: After processing all URLs, the script logs the total number of accessible and inaccessible URLs.

## Example Log Output

An example of what the log file might contain:

```
2024-08-22 10:00:00,000 - INFO - Accessible: https://example.com/image1.jpg
2024-08-22 10:00:02,000 - WARNING - Inaccessible (status code 404): https://example.com/image2.png
2024-08-22 10:00:04,000 - ERROR - Error accessing https://nonexistent.com/image.jpg: HTTPSConnectionPool(host='nonexistent.com', port=443): Max retries exceeded with url: /image.jpg (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7fddb5b5f7c0>: Failed to establish a new connection: [Errno -2] Name or service not known'))
2024-08-22 10:00:05,000 - INFO - Total accessible URLs: 1
2024-08-22 10:00:05,000 - INFO - Total inaccessible URLs: 2
```

## Customization

- **Timeout**: The script uses a timeout of 5 seconds for each HTTP request. You can modify this value in the `check_url_accessibility` function.
- **Log Level**: The logging level is set to `INFO`, but you can adjust it to include more or fewer details by changing the `level` parameter in the `logging.basicConfig()` function.