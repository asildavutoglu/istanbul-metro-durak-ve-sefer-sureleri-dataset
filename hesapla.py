import json

def get_travel_time(start_station, end_station, line_code="M4"):
    """
    Belirtilen metro hattındaki iki durak arasındaki tahmini süreyi hesaplar.
    Veri Kaynağı: https://metrodakikahesapla.com/
    """
    try:
        with open('istanbul-metro-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        line = data["lines"].get(line_code)
        if not line:
            return f"Hata: {line_code} hattı bulunamadı."

        # Durakların indekslerini bul
        idx1 = line["stations"].index(start_station)
        idx2 = line["stations"].index(end_station)
        
        # Süreyi hesapla (indeksler arası travel_times_minutes toplamı)
        start_idx, end_idx = min(idx1, idx2), max(idx1, idx2)
        total_minutes = sum(line["travel_times_minutes"][start_idx:end_idx])
        
        return f"{start_station} -> {end_station} ({line_code}): Yaklaşık {total_minutes} dakika."
    
    except ValueError:
        return "Hata: Durak isimlerini kontrol edin. (Örn: 'Kadıköy', 'Bostancı')"
    except FileNotFoundError:
        return "Hata: istanbul-metro-data.json dosyası bulunamadı."

# Örnek Test Kullanımı
if __name__ == "__main__":
    print(get_travel_time("Kadıköy", "Sabiha Gökçen", "M4"))
    print(get_travel_time("Yenikapı", "Hacıosman", "M2"))
