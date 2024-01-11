import requests
import json
class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                json_data = json.loads(response_body)
                return json_data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        else:
            print("Unable to load JSON data.")
            return None

# Example usage:
url = "https://dog.ceo/api/breeds/image/random"
requester = GetRequester(url)

# Get the response body
response_body = requester.get_response_body()
print(f"Response Body:\n{response_body}")

# Load JSON data
json_data = requester.load_json()
print(f"Loaded JSON:\n{json_data}")
