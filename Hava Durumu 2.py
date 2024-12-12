

class Sehir:
    def __init__(self, ad, sicaklik=None):
        self.ad = ad
        self.sicaklik = sicaklik

    def __str__(self):
        sicaklik_info = f"{self.sicaklik}°C" if self.sicaklik is not None else "Bilinmiyor"
        return f"{self.ad} - Sıcaklık: {sicaklik_info}"


class HavaDurumu:
    def __init__(self):
        self.sehirler = []

    def sehir_ekle(self, ad):
        yeni_sehir = Sehir(ad)
        self.sehirler.append(yeni_sehir)
        print(f"{ad} şehri eklendi.")

    def sicaklik_guncelle(self, ad, sicaklik):
        for sehir in self.sehirler:
            if sehir.ad.lower() == ad.lower():
                sehir.sicaklik = sicaklik
                print(f"{ad} şehri için sıcaklık güncellendi: {sicaklik}°C")
                return
        print(f"{ad} şehri bulunamadı. Önce eklemelisiniz!")

    def hava_durumu_sorgula(self, ad):
        for sehir in self.sehirler:
            if sehir.ad.lower() == ad.lower():
                print(sehir)
                self.sicaklik_tavsiyesi(sehir.sicaklik)
                return
        print(f"{ad} şehri bulunamadı.")

    def sicaklik_tavsiyesi(self, sicaklik):
        if sicaklik is None:
            print("Sıcaklık bilgisi mevcut değil.")
        elif sicaklik < 0:
            print("Soğuk, sıkı giyinin.")
        elif 0 <= sicaklik <= 15:
            print("Serin, mont almayı unutmayın.")
        else:
            print("Hava güzel, rahat giyin.")

    def listele(self):
        if not self.sehirler:
            print("Henüz eklenmiş şehir yok.")
            return

        print("\nEklenmiş Şehirler:")
        for sehir in self.sehirler:
            print(sehir)


