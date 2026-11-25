# kayit_defteri.py - Game jam takım kayıt defteri
# Takımlar sözlüklerden oluşan bir listede saklanır; menü "çıkış" seçilene kadar döner.

from datetime import datetime

def kayit_ekle(takimlar, takim_adi, kayit_tarihi, uye_sayisi, juri_puani):
    """Listeye yeni bir takım kaydı ekler ve eklenen kaydı döndürür."""
    # Gelen bilgilerden tek bir takımı temsil eden sözlük oluşturuyoruz
    yeni_kayit = {
        "takim_adi": takim_adi,
        "kayit_tarihi": kayit_tarihi,
        "uye_sayisi": uye_sayisi,
        "juri_puani": juri_puani,
    }
    # Sözlüğü takımlar listesinin sonuna ekliyoruz
    takimlar.append(yeni_kayit)
    # Eklenen kaydı geri veriyoruz; çağıran yer isterse onu ekrana yazdırabilir
    return yeni_kayit


def kayitlari_listele(takimlar):
    """Bütün takımları tablo hâlinde ekrana yazdırır; değer döndürmez."""
    # Liste boşsa tablo yerine kısa bir uyarı yazıp fonksiyondan çıkıyoruz
    if len(takimlar) == 0:
        print("Henüz kayıtlı takım yok.")
        return
    # Tablonun başlık satırını sabit genişlikli sütunlarla yazdırıyoruz
    print(f"{'No':<4}{'Takım adı':<26}{'Kayıt tarihi':<14}{'Üye':>5}{'Puan':>8}")
    # Başlığın altına ayırıcı çizgi çekiyoruz
    print("-" * 57)
    # enumerate ile her kaydı 1'den başlayan sıra numarasıyla birlikte geziyoruz
    for sira, takim in enumerate(takimlar, start=1):
        # Her takımın bilgilerini aynı sütun genişlikleriyle tek satırda yazdırıyoruz
        print(f"{sira:<4}{takim['takim_adi']:<26}{takim['kayit_tarihi']:<14}"
              f"{takim['uye_sayisi']:>5}{takim['juri_puani']:>8.1f}")


def tarihten_sonrakileri_bul(takimlar, baslangic_tarihi):
    """Kayıt tarihi verilen tarihten SONRA olan takımları yeni bir liste olarak döndürür."""
    # Koşula uyan takımları toplamak için boş bir liste açıyoruz
    sonuc = []
    # Bütün takımları tek tek geziyoruz
    for takim in takimlar:
        # "YYYY-AA-GG" biçimindeki tarihler metin olarak karşılaştırılabilir
        if takim["kayit_tarihi"] > baslangic_tarihi:
            # Koşula uyan takımı sonuç listesine ekliyoruz
            sonuc.append(takim)
    # Bulunan takımları döndürüyoruz; hiçbiri yoksa boş liste döner
    return sonuc


def ozet_hesapla(takimlar):
    """Takım sayısı, toplam üye, ortalama puan ve en yüksek puanlı takımı sözlük olarak döndürür."""
    # Hiç kayıt yoksa ortalama hesaplanamaz (sıfıra bölme olur); None döndürüyoruz
    if len(takimlar) == 0:
        return None
    # Toplamları tutacak değişkenleri sıfırdan başlatıyoruz
    toplam_uye = 0
    toplam_puan = 0
    # En yüksek puanlı takımı bulmak için ilk takımı başlangıç kabul ediyoruz
    en_iyi = takimlar[0]
    # Bütün takımları tek tek geziyoruz
    for takim in takimlar:
        # Takımın üye sayısını ve puanını toplamlara ekliyoruz
        toplam_uye += takim["uye_sayisi"]
        toplam_puan += takim["juri_puani"]
        # Bu takımın puanı şimdiye kadarki en yüksekten büyükse onu yeni en iyi yapıyoruz
        if takim["juri_puani"] > en_iyi["juri_puani"]:
            en_iyi = takim
    # Sonuçları anlaşılır anahtarlarla tek bir sözlükte topluyoruz
    ozet = {
        "takim_sayisi": len(takimlar),
        "toplam_uye": toplam_uye,
        "ortalama_puan": toplam_puan / len(takimlar),
        "en_yuksek_takim": en_iyi["takim_adi"],
        "en_yuksek_puan": en_iyi["juri_puani"],
    }
    # Özet sözlüğünü döndürüyoruz
    return ozet


def metin_al(mesaj):
    """Boş olmayan bir metin alana kadar tekrar sorar ve metni döndürür."""
    while True:
        # Baştaki ve sondaki boşlukları silerek cevabı alıyoruz
        deger = input(mesaj).strip()
        # Cevap boş değilse döndürüp fonksiyondan çıkıyoruz
        if deger != "":
            return deger
        print("  ! Bu alan boş bırakılamaz.")


def tarih_al(mesaj):
    """YYYY-AA-GG biçiminde geçerli bir tarih alana kadar tekrar sorar."""
    while True:
        deger = input(mesaj).strip()
        try:
            # strptime tarihi kontrol eder; 2026-02-30 gibi geçersiz tarihlerde hata verir
            datetime.strptime(deger, "%Y-%m-%d")
            return deger
        except ValueError:
            print("  ! Tarihi YYYY-AA-GG biçiminde girin (ör. 2026-11-20).")


def sayi_al(mesaj, en_az, en_cok, ondalikli=False):
    """Belirtilen aralıkta bir sayı alana kadar tekrar sorar; hatalı girdide çökmez."""
    while True:
        try:
            # ondalikli=True ise float, değilse int'e çeviriyoruz
            if ondalikli:
                # Türkçede ondalık ayırıcı virgül olduğu için "82,5" yazılırsa "82.5"e çeviriyoruz
                deger = float(input(mesaj).replace(",", "."))
            else:
                deger = int(input(mesaj))
        except ValueError:
            print("  ! Lütfen geçerli bir sayı girin.")
            continue
        # Sayı aralıktaysa döndürüyoruz, değilse uyarıp tekrar soruyoruz
        if en_az <= deger <= en_cok:
            return deger
        print(f"  ! Değer {en_az} ile {en_cok} arasında olmalı.")


def ana_menu():
    """Kullanıcı çıkış seçene kadar menüyü gösterir ve seçilen işlemi yapar."""
    # Bütün kayıtların tutulacağı liste
    takimlar = []
    # Kullanıcı "5" seçene kadar dönen menü döngüsü
    while True:
        print("\n=== GAME JAM TAKIM KAYIT DEFTERİ ===")
        print("1) Takım ekle")
        print("2) Tüm takımları listele")
        print("3) Belli bir tarihten sonra kaydolanlar")
        print("4) Özet")
        print("5) Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            # Bilgileri menüde alıp ekleme fonksiyonuna veriyoruz
            ad = metin_al("Takım adı: ")
            tarih = tarih_al("Kayıt tarihi (YYYY-AA-GG): ")
            uye = sayi_al("Üye sayısı (1-10): ", 1, 10)
            puan = sayi_al("Jüri puanı (0-100): ", 0, 100, ondalikli=True)
            eklenen = kayit_ekle(takimlar, ad, tarih, uye, puan)
            print(f"  + {eklenen['takim_adi']} eklendi. Toplam takım: {len(takimlar)}")
        elif secim == "2":
            kayitlari_listele(takimlar)
        elif secim == "3":
            tarih = tarih_al("Hangi tarihten sonrakiler? (YYYY-AA-GG): ")
            bulunanlar = tarihten_sonrakileri_bul(takimlar, tarih)
            if len(bulunanlar) == 0:
                print(f"  {tarih} tarihinden sonra kaydolan takım yok.")
            else:
                print(f"  {tarih} tarihinden sonra kaydolan {len(bulunanlar)} takım:")
                kayitlari_listele(bulunanlar)
        elif secim == "4":
            ozet = ozet_hesapla(takimlar)
            if ozet is None:
                print("  Henüz kayıtlı takım yok.")
            else:
                print(f"  Takım sayısı      : {ozet['takim_sayisi']}")
                print(f"  Toplam katılımcı  : {ozet['toplam_uye']}")
                print(f"  Ortalama puan     : {ozet['ortalama_puan']:.2f}")
                print(f"  En yüksek puan    : {ozet['en_yuksek_takim']} ({ozet['en_yuksek_puan']:.1f})")
        elif secim == "5":
            print("Görüşmek üzere!")
            # break ile while döngüsünden çıkıyoruz; program sonlanıyor
            break
        else:
            # Menüde olmayan bir seçim girildiğinde çökmek yerine uyarıyoruz
            print("  ! Geçersiz seçim. 1-5 arası bir sayı girin.")


# Dosya doğrudan çalıştırıldığında menüyü başlatıyoruz
if __name__ == "__main__":
    ana_menu()
