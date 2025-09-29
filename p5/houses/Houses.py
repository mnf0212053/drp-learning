# Class untuk rumah (Houses)


class Houses:  # mendeklarasikan class untuk perumaham
    def __init__(self, blok, nomor, harga):
        # nama blok
        # nama nomor
        # harga (dalam ratus juta)
        
        self.blok = blok
        self.nomor = nomor
        self.harga = harga

    def info_rumah(self):
        print('===========================================')
        print('Rumah ini berlokasi di:')
        print('blok: ' + self.blok)
        print('nomor: ' + str(self.nomor))
        print('dijual dengan harga ' + str(self.harga) + ' ratus juta')
        print('===========================================')


class Hotel(Houses):
    def __init__(self, lantai):
        self.lantai = lantai
