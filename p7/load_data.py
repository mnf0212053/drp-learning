import json

def load_file():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    data = load_file()
    print(data)