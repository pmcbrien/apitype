import requests

def determine_endpoint_type(url):
    response = requests.get(url)
    # check if it's a RESTful API endpoint
    if 'json' in response.headers['Content-Type']:
        print(url + " is a RESTful API endpoint.")
    # check if it's a GraphQL API endpoint
    elif response.json().get('data'):
        print(url + " is a GraphQL API endpoint.")
    else:
        print(url + " is of an unknown type.")

# Example usage
determine_endpoint_type("https://jsonplaceholder.typicode.com/posts")
determine_endpoint_type("https://graphql-pokemon.now.sh/")
