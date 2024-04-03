import requests

url = "https://indonesian-identification-card-ktp.p.rapidapi.com/api/v3/check"

querystring = {"nik":"NIK YANG MAU DI CEK"}

headers = {
	"X-RapidAPI-Key": "39a36edf2amsh2ac7cbe83dd5ad3p1c2d56jsn4300569c2998",
	"X-RapidAPI-Host": "indonesian-identification-card-ktp.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
