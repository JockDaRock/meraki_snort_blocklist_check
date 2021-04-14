import requests

def meraki_network_traffic(net_ID, api_key, time_span):

    url = "https://api.meraki.com/api/v1/networks/{0}/traffic".format(net_ID)

    querystring = {"timespan": time_span}

    headers = {
        'Accept': "*/*",
        'X-Cisco-Meraki-API-Key': api_key,
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #insert logging here

    return response.json()