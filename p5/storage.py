import json

from houses.Houses import Houses


class Storage:
    def __init__(self):
        filename = 'data.json'

        try:
            with open(filename, 'r') as f:
                json_data = json.load(f)
                data = [
                    Houses(house['blok'], house['nomor'], house['harga'])
                for house in json_data]
        except Exception as err:
            with open(filename, 'w') as f:
                data = []
                json.dump(data, f)

        self.data = data

    def write_to_file(self):
        with open('data.json', 'w') as f:
            json.dump([
                {
                    'blok': d.blok,
                    'nomor': d.nomor,
                    'harga': d.harga
                } for d in self.data
            ], f)

    def append(self, house: Houses):
        self.data.append(Houses(house.blok, house.nomor, house.harga))

        self.write_to_file()
        