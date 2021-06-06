class Manusia:
    def __init__(self,nama,__makanan):
      self.__nama = nama
      self.__makanan = __makanan

    def login(self):
      print('selamat {} berhasil mendaftar di website ini'.format(self.__nama),'silakan memilih menu {} diatas'.format(self.__makanan))


Sup_Ayam = Manusia('Sup Ayam', 'marica')
Sup_Ayam.login()
