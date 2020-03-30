import requests

url = "https://coronavirus-monitor-v2.p.rapidapi.com/coronavirus/cases_by_country.php"

headers = {
    'x-rapidapi-host': "coronavirus-monitor-v2.p.rapidapi.com",
    'x-rapidapi-key': "9732f3e6admshe35951f9d4aaf81p192067jsn148dce589b57"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)
