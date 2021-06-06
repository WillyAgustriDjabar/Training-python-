class rektor:

  jumlah_rektor = 0
  def __init__(self, Nama, Kelas):
    self.Nama = Nama
    self.Kelas = Kelas

    rektor.jumlah_rektor +=1

  def camat(self):
    print(self.Nama, self.Kelas, "Adalah camat ")

  def gubernur(self, masa):
    print(self.Nama, self.Kelas, "adalah gubernur", masa)
  

  
  


budiman = rektor('budiman', 2000)
budimans = rektor('budimans', 2000)
budiman.camat()
budimans.camat()

print(rektor.jumlah_rektor)

