import requests


URL = "https://coronavirus-monitor-v2.p.rapidapi.com/coronavirus/cases_by_country.php"

HEADERS = {
    'x-rapidapi-host': "coronavirus-monitor-v2.p.rapidapi.com",
    'x-rapidapi-key': "9732f3e6admshe35951f9d4aaf81p192067jsn148dce589b57"
    }

RESPONSE = requests.request("GET", URL, headers=HEADERS)
DATA = RESPONSE.json()
FILE = open('api_usage.json', 'w')
FILE.write(str(DATA))
FILE.close()
