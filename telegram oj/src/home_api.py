import requests

def get_gender_by_name(name):
    url = "https://api.genderize.io"

    params = {"name": name}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "ERROR"
    else:
        data = response.json()

        gender = data["gender"]
        probability = data["probability"]

        return (gender, probability)


if __name__ == "__main__":
    name = input("Enter a name: ")
    result = get_gender_by_name(name)
    print(f"Result: {result}")