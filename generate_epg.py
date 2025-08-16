
import requests
import datetime

# Senin kendi sunucundaki EPG kaynağı
url = "http://178.63.255.253:2701/turkey_fixed.xml"

try:
    r = requests.get(url, timeout=60)
    r.raise_for_status()

    with open("turkey.xml", "wb") as f:
        f.write(r.content)

    print("✅ EPG güncellendi:", datetime.datetime.now())

except Exception as e:
    print("❌ Hata:", e)
