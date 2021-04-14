import ipaddress
import socket
import re
import requests

def convert_host_to_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        ip = "unknown"
        return ip

def is_ip_or_hostname(host_ip):
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip = re.findall(re_ip, host_ip)
    if len(ip) == 0:
        return "hostname"
    else:
        return "ip"

def is_private_ip(ip_addy):
    priv_ip = ipaddress.ip_address(ip_addy).is_private
    return priv_ip

def convert_host_to_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        ip = "unknown"
        return ip

def get_block_list():
    block_list_req = requests.get("https://www.snort.org/downloads/ip-block-list")
    block_list_text = block_list_req.text
    
    block_list_array = block_list_text.splitlines()

    return block_list_array