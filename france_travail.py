import http.client

conn = http.client.HTTPSConnection("api.francetravail.io")

headers = {
    'Authorization': "PAR_jobsearchminimal_827d7f36c266fb042b6fba77efac4c55a01948331177090df6a4f253a26327dc",
    'Accept': "application/json"
}

conn.request("GET", "/partenaire/offresdemploi/v2/offres/search?accesTravailleurHandicape=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))