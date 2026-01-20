# İstanbul Metro Durak ve Sefer Süreleri Veri Seti

Bu depo, İstanbul'daki tüm aktif metro hatlarının (M1A, M1B, M2, M3, M4, M5, M6, M7, M8) verilerini yapılandırılmış JSON formatında sunar.

## 🚀 Canlı Uygulama
Bu veri seti kullanılarak geliştirilen mesafe ve süre hesaplama aracına buradan ulaşabilirsiniz:
[**metrodakikahesapla.com**](https://metrodakikahesapla.com/)

## 📊 Veri İçeriği
- **Hatlar:** M1'den M8'e kadar tüm hat bilgileri.
- **Duraklar:** Hat üzerindeki tüm istasyon isimleri.
- **Süreler:** Duraklar arası ortalama seyahat süreleri (dakika).
- **Ücretler:** Güncel İBB toplu taşıma tarifesi (Tam, Öğrenci, Sosyal).

## 🛠 Kullanım
Veriyi kendi projelerinizde (Python, JavaScript, C# vb.) doğrudan kullanabilirsiniz.

```json
// Örnek kullanım (Python)
import json
with open('istanbul-metro-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
