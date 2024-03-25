import requests
def order_request():
    url = "http://127.0.0.1:3000/order"
    headers = {"Content-Type": "application/json"}  # Add any required headers
    data = {"book": "rich dad","quantity":"2","price":"20$"}  # Replace with your request payload

    try:
        response = requests.post(url, headers=headers,json=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response data
            print("Response:", response.json())
        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def payment_request():
    url = "http://127.0.0.1:3000/payment"
    headers = {"Content-Type": "application/json"}  # Add any required headers
    data = {"order_id":1 , "book": "rich dad","quantity":2,"price":20}  # Replace with your request payload

    try:
        response = requests.post(url, headers=headers,json=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response data
            print("Response:", response.json())
        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    payment_request()