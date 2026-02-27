# Pertama install dulu: pip install requests
import requests

# Mengambil data cuaca dari API publik
url = 'https://api.open-meteo.com/v1/forecast'
params = {
'latitude': -0.9471, # Padang
'longitude': 100.4172,
'current_weather': True
}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status() # raise error jika status bukan 200
    data = response.json()
    suhu = data['current_weather']['temperature']
    print(f'Suhu saat ini: {suhu} C')
except requests.exceptions.ConnectionError:
    print('Tidak ada koneksi internet!')
except requests.exceptions.Timeout:
    print('Request timeout!')