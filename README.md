# 🚇 İstanbul Metro Durak ve Sefer Süreleri Veri Seti

Bu depo, İstanbul'daki tüm aktif metro hatlarının (M1-M8) ve Marmaray'ın güncel durak isimlerini, seyahat sürelerini ve bilet tarifelerini içeren kapsamlı bir **JSON** veri seti sunar.

## 🔗 Canlı Uygulamalar
* 🚇 **Metro Süre Hesaplama:** [metrodakikahesapla.com](https://metrodakikahesapla.com/)
* 🚆 **Marmaray Durak ve Ücret Hesaplama:** [metrodakikahesapla.com/marmaray-durak-hesaplama](https://metrodakikahesapla.com/marmaray-durak-hesaplama)
* 🌐 **Canlı Dokümantasyon (GitHub Pages):** [Veri Önizleme Paneli](https://asildavutoglu.github.io/istanbul-metro-durak-ve-sefer-sureleri-dataset/)

---

## 📊 Veri Seti İçeriği
`istanbul-metro-data.json` dosyası şu bilgileri kapsamaktadır:
- **Hatlar:** M1A, M1B, M2, M3, M4, M5, M6, M7, M8 ve Marmaray.
- **İstasyonlar:** Hatlar üzerindeki tüm durakların sıralı listesi.
- **Süreler:** Duraklar arası geçiş süreleri (dakika).
- **Ücretler:** İBB güncel toplu taşıma tarifesi.

## 🛠 Kurulum ve Kullanım
Veri setini projelerinizde kullanmak için JSON dosyasını indirmeniz yeterlidir. Python ile hızlı bir test yapmak için:

1. Depoyu klonlayın.
2. `python hesapla.py` komutunu çalıştırın.

## 📊 Kapsanan Hatlar
- **M1A & M1B** (Havalimanı / Kirazlı)
- **M2** (Yenikapı - Hacıosman)
- **M4** (Kadıköy - Sabiha Gökçen)
- **M5, M7, M8** ve daha fazlası...

---
*Bu proje açık kaynaklı bir toplu taşıma veri girişimidir. Katkıda bulunmak için Pull Request gönderebilirsiniz.*
