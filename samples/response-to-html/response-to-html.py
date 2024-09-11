import requests

# Step 1: Make a GET request to the webpage
response = requests.get('https://gasprice.kapook.com/gasprice.php')

# Step 2: Check the encoding of the response
response.encoding = response.apparent_encoding  # Automatically detect the correct encoding

# Step 3: Save the response content to an HTML file
if response.status_code == 200:
    with open('gasprice.html', 'w', encoding=response.encoding) as file:
        file.write(response.text)
    print("HTML file has been saved successfully with correct encoding.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")