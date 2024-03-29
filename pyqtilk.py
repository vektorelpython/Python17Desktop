import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from PyQt5 import uic
from PyQt5 import  QtCore
import DB



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.win =  uic.loadUi(r"GUI\AnaMenu.ui")
        self.win.btYeni.clicked.connect(self.tiklandi)
        self.win.cmbArtist.currentIndexChanged.connect(self.artistDegis)
        self.win.cmbAlbum.currentIndexChanged.connect(self.Tabladoldur)
        self.comboDoldur()
        self.PersonelDoldur()
        self.ArtistDoldur()
        self.PersonelDoldur()
        self.Tabladoldur()
        self.initUI()
        
    def initUI(self):
        self.win.show()

    def comboDoldur(self): 
        liste=DB.MusteriListe()
        self.win.cmbMusteri.addItem("Seçiniz","-1")
        for id,adi in liste:
              self.win.cmbMusteri.addItem(adi,int(id))
    
    def PersonelDoldur(self): 
        liste=DB.PersonelListe()
        self.win.cmbPersonel.addItem("Seçiniz","-1")
        for id,adi in liste:
              self.win.cmbPersonel.addItem(adi,int(id))
    def ArtistDoldur(self): 
        liste=DB.ArtistListe()
        self.win.cmbArtist.addItem("Seçiniz","-1")
        for id,adi in liste:
              self.win.cmbArtist.addItem(adi,int(id))
    def AlbumDoldur(self,ArtistID): 
        liste=DB.AlbumListe(ArtistID)
        self.win.cmbAlbum.addItem("Seçiniz","-1")
        for id,adi in liste:
              self.win.cmbAlbum.addItem(adi,int(id))


    def artistDegis(self):
        self.win.cmbAlbum.clear()
        print(self.win.cmbArtist.currentIndex())
        self.AlbumDoldur(self.win.cmbArtist.currentIndex())
    def tiklandi(self):
        print("buton çalıştı")

    def degisti(self):
        secilen = self.win.cmbMusteri.currentIndex()
        print(secilen)

    def Tabladoldur(self):
        self.win.tblParca.clear()
        albumID = self.win.cmbAlbum.itemData(self.win.cmbAlbum.currentIndex())
        if albumID != "-1" and albumID:
            self.win.tblParca.setRowCount(100)
            self.win.tblParca.setColumnCount(4)
            liste = DB.ParcaListe(albumID)
            index = 0
            for id,adi,ucret,byte in liste:
                item1 = QTableWidgetItem(str(id))
                item2 = QTableWidgetItem(adi)
                item3 = QTableWidgetItem(str(ucret))
                item4 = QTableWidgetItem(str(byte))
                self.win.tblParca.setItem(index,0,item1)
                self.win.tblParca.setItem(index,1,item2)
                self.win.tblParca.setItem(index,2,item3)
                self.win.tblParca.setItem(index,3,item4)
                index += 1
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 

