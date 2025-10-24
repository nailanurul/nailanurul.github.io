import requests

latitude = -6.2088
longtude = 106.8456

url = f"https://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method=20"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    timings = data["data"]["timings"]
    date = data["data"]["date"]["readable"]

    print(f" Jadwal Salat untuk Tanggal {date}")
    print("-" * 40)
    print(f"Imsak   : {timings['Imsak']}")
    print(f"Subuh   : {timings['Fajr']}")
    print(f"Terbit  : {timings['Sunrise']}")
    print(f"Dzuhur  : {timings['Dhuhr']}")
    print(f"Ashar   : {timings['Asr']}")
    print(f"Magrib  : {timings['Magrib']}")
    print(f"Isya    : {timings['Isya']}")
    print("-" * 40)
else:
    print(f" Gagal ambil data dari API. Status code: {response.status_code}")