import requests


def getPoints(tkn):
 
  try:

    req = requests.request(
      "GET",
      f"https://gr-stake-to-reveal.vercel.app/api/nftPoints?apikey=xPrMeCccepKa&mintId={tkn}"
    )
    return req.json()["data"][tkn]
  except:
    return "Unknown.s"


def getListings():
  payload = {}
  headers = {}

  req_1 = requests.request(
    "GET",
    "https://api-mainnet.magiceden.dev/v2/collections/generousrobots/listings?offset=0&limit=10",
    headers=headers,
    data=payload)
  data = []
  for elem in req_1.json():
    data.append({
      "tkn": elem["tokenMint"],
      "price": elem["price"],
      "points": getPoints(elem["tokenMint"])
    })
  return data

print(getPoints("GoKB6CjpHwpvmPj53Le125bEmJcsEioXfxZEznaNjzvK"))
for x in getListings():print(x)
