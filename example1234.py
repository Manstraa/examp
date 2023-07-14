class Ucus():
    sirket="OHY"
    def __init__(self,kod,kalkis,varis,kapasite,sure,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.kapasite=kapasite
        self.sure=sure
        self.yolcu=yolcu
    def anons(self):
        return "{} numarali {}-{} arasi kalkisli ucagimizda {} kisi yolculuk yapacaktir".format(self.kod,self.kalkis,self.varis,self.yolcu)
    def koltuk_sayisi(self):
        return "Kalan koltuk sayisi {} . ".format(self.kapasite - self.yolcu)
    def satis(self,bilet_adedi=0):
        if self.yolcu+bilet_adedi <= self.kapasite:
            self.yolcu+=bilet_adedi
            return "Toplamda {} adet bilet satilmistir".format(self.yolcu)
        else :
            return "Uzgunum yetersiz bilet sayisi "
    def iptal(self,iptal_sayisi=0):
        if iptal_sayisi<=self.yolcu:
            self.yolcu -= iptal_sayisi
            return "{} bilet iptal edildigi icin toplam bilet sayisi {} olmustur ".format(iptal_sayisi, self.yolcu)
        else:
            return "Uzgunum iptal etmek istediginiz bilet {} kadar yolcu bulunmamaktadir ".format(iptal_sayisi)
ucus1=Ucus('TK123','MRD','ANT',123,90,77)
print(ucus1.satis(11))
print(ucus1.satis(10))
print(ucus1.iptal(7))
print(ucus1.iptal(92))

class yolculuk() :
    def __init__(self,baslangic,varis):
        self.baslangic=baslangic
        self.varis=varis
    def anoons(self):
        return '{} {} yolculugumuza hosgeldiniz'.format(self.baslangic,self.varis)
class otobus(yolculuk):
    def __init__(self,baslangic,varis,mola_alani):
        yolculuk.__init__(self,baslangic,varis)
        self.mola_alani=mola_alani
oto1= otobus('ADN','IST','ERG')
print(oto1.anoons())
print(oto1.mola_alani)

class Kutuphane():
    def __init__(self,isim,s_isim,kitap,film):
        self.isim=isim
        self.s_isim = s_isim
        self.kitap=kitap
        self.film=film
class Ogrenci(Kutuphane):
    def __init__(self,numara,sinif):
        Kutuphane.__init__(self,isim,s_isim,kitap,film)
        self.numara = numara
        self.sinif = sinif
