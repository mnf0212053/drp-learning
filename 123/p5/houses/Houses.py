# Class untuk rumah (Houses)


class Houses:  # mendeklarasikan class untuk perumaham
    def __init__(self, blok, nomor, harga):
        # nama blok
        # nama nomor
        # harga (dalam ratus juta)
        
        self.blok = blok
        self.nomor = nomor
        self.harga = harga

    def _info_rumah(self):
        print('blok: ' + self.blok)
        print('nomor: ' + str(self.nomor))
        print('dijual dengan harga ' + str(self.harga) + ' ratus juta')

    def info_rumah(self):
        print('===========================================')
        print('Info properti:')
        self._info_rumah()
        print('===========================================')


class Hotel(Houses):  # Parent: Houses; Child: Hotel
    def __init__(self, blok, nomor, harga, lantai):
        super().__init__(blok, nomor, harga)
        self.lantai = lantai

    def info_rumah(self):
        print('===========================================')
        print('Info properti:')
        print('blok: ' + self.blok)
        print('nomor: ' + str(self.nomor))
        print('lantai: ' + str(self.lantai))
        print('dijual dengan harga ' + str(self.harga) + ' ratus juta')
        print('===========================================')


class Ruko(Houses):
    def __init__(self, harga, nama_pt):
        super().__init__("", "", harga)
        self.nama_pt = nama_pt

    def info_rumah(self):
        print('===========================================')
        print('Info Properti:')
        print('Nama PT: ' + str(self.nama_pt))
        print('dijual dengan harga ' + str(self.harga) + ' ratus juta')
        print('===========================================')

