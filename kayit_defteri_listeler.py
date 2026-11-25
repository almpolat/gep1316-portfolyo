# kayit_defteri_listeler.py - Aynı uygulama, sözlük kullanmadan yalnızca listelerle
# Her takım [takım adı, kayıt tarihi, üye sayısı, jüri puanı] sırasıyla bir listedir.
# Bilgilere sıra numarasıyla ulaşılır: [0]=ad, [1]=tarih, [2]=üye, [3]=puan

from datetime import datetime


def kayit_ekle(takimlar, takim_adi, kayit_tarihi, uye_sayisi, juri_puani):
    """Listeye yeni bir takım ekler ve eklenen kaydı döndürür."""
    # Bilgiler sabit bir sırayla iç içe bir listeye konuyor
    yeni_kayit = [takim_adi, kayit_tarihi, uye_sayisi, juri_puani]
    takimlar.append(yeni_kayit)
    return yeni_kayit


def kayitlari_listele(takimlar):
    """Bütün takımları tablo hâlinde yazdırır."""
    if len(takimlar) == 0:
        print("Henüz kayıtlı takım yok.")
        return
    print(f"{'No':<4}{'Takım adı':<26}{'Kayıt tarihi':<14}{'Üye':>5}{'Puan':>8}")
    print("-" * 57)
    for sira, takim in enumerate(takimlar, start=1):
        # takim[0] ad, takim[1] tarih, takim[2] üye, takim[3] puan
        print(f"{sira:<4}{takim[0]:<26}{takim[1]:<14}{takim[2]:>5}{takim[3]:>8.1f}")


def tarihten_sonrakileri_bul(takimlar, baslangic_tarihi):
    """Kayıt tarihi verilen tarihten sonra olan takımları döndürür."""
    sonuc = []
    for takim in takimlar:
        # takim[1] kayıt tarihi
        if takim[1] > baslangic_tarihi:
            sonuc.append(takim)
    return sonuc


def ozet_hesapla(takimlar):
    """[takım sayısı, toplam üye, ortalama puan, en iyi takım adı, en iyi puan] döndürür."""
    if len(takimlar) == 0:
        return None
    toplam_uye = 0
    toplam_puan = 0
    en_iyi = takimlar[0]
    for takim in takimlar:
        toplam_uye += takim[2]
        toplam_puan += takim[3]
        if takim[3] > en_iyi[3]:
            en_iyi = takim
    return [len(takimlar), toplam_uye, toplam_puan / len(takimlar), en_iyi[0], en_iyi[3]]


def metin_al(mesaj):
    while True:
        deger = input(mesaj).strip()
        if deger != "":
            return deger
        print("  ! Bu alan boş bırakılamaz.")


def tarih_al(mesaj):
    while True:
        deger = input(mesaj).strip()
        try:
            datetime.strptime(deger, "%Y-%m-%d")
            return deger
        except ValueError:
            print("  ! Tarihi YYYY-AA-GG biçiminde girin (ör. 2026-11-20).")


def sayi_al(mesaj, en_az, en_cok, ondalikli=False):
    while True:
        try:
            if ondalikli:
                deger = float(input(mesaj).replace(",", "."))
            else:
                deger = int(input(mesaj))
        except ValueError:
            print("  ! Lütfen geçerli bir sayı girin.")
            continue
        if en_az <= deger <= en_cok:
            return deger
        print(f"  ! Değer {en_az} ile {en_cok} arasında olmalı.")


def ana_menu():
    takimlar = []
    while True:
        print("\n=== GAME JAM TAKIM KAYIT DEFTERİ (yalnızca listeler) ===")
        print("1) Takım ekle")
        print("2) Tüm takımları listele")
        print("3) Belli bir tarihten sonra kaydolanlar")
        print("4) Özet")
        print("5) Çıkış")
        secim = input("Seçiminiz: ").strip()
        if secim == "1":
            ad = metin_al("Takım adı: ")
            tarih = tarih_al("Kayıt tarihi (YYYY-AA-GG): ")
            uye = sayi_al("Üye sayısı (1-10): ", 1, 10)
            puan = sayi_al("Jüri puanı (0-100): ", 0, 100, ondalikli=True)
            eklenen = kayit_ekle(takimlar, ad, tarih, uye, puan)
            print(f"  + {eklenen[0]} eklendi. Toplam takım: {len(takimlar)}")
        elif secim == "2":
            kayitlari_listele(takimlar)
        elif secim == "3":
            tarih = tarih_al("Hangi tarihten sonrakiler? (YYYY-AA-GG): ")
            bulunanlar = tarihten_sonrakileri_bul(takimlar, tarih)
            if len(bulunanlar) == 0:
                print(f"  {tarih} tarihinden sonra kaydolan takım yok.")
            else:
                kayitlari_listele(bulunanlar)
        elif secim == "4":
            ozet = ozet_hesapla(takimlar)
            if ozet is None:
                print("  Henüz kayıtlı takım yok.")
            else:
                print(f"  Takım sayısı      : {ozet[0]}")
                print(f"  Toplam katılımcı  : {ozet[1]}")
                print(f"  Ortalama puan     : {ozet[2]:.2f}")
                print(f"  En yüksek puan    : {ozet[3]} ({ozet[4]:.1f})")
        elif secim == "5":
            print("Görüşmek üzere!")
            break
        else:
            print("  ! Geçersiz seçim. 1-5 arası bir sayı girin.")


if __name__ == "__main__":
    ana_menu()
