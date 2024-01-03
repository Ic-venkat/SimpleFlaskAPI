import requests

def post_data(api_url, json_data):
    try:
        # Make a POST request to the API endpoint with JSON data
        response = requests.post(api_url, json=json_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
            return data
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example API endpoint (replace it with the actual endpoint you want to send a POST request to)
api_endpoint = "http://127.0.0.1:5000/users"

# Example JSON data to be sent in the POST request

json_data_list = [{
    "name" : "Heamanth",
    "age": 20
},
{
    "name" : "",
    "age": 20

},
{
    "name" : "Heamanth",
    "age": ""
},
{
    "name" : "",
    "age": ""
},
{
    "name" : "agjahsdjghoisavodjiodsjgiojgioasdjosajoidjgoiasdgoihsdiohg",
    "age": 20
},
{

},
{
    "name" : "Heamanth"
},
{
    "age": 20
},
{
    "name" : "",
    "age": 10
},
{
    "name" : "",
    "age": "20"

},
{
    "name" : "Heamanth",
    "age": 10

}
]

# Send a POST request with JSON data to the API endpoint
for i in json_data_list:
    result = post_data(api_endpoint, i)
    print(i)

# Check if data was successfully posted
    if result:
        print("Data posted successfully:")
        print(result)
    else:
        print("Failed to post data.")

    print("\n")
