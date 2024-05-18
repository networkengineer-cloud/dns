# Write a python script to get the egress IP by DNS lookup and web request to a public IP address. Log the result to stdout.

import socket
import requests
import logging

DNS_SERVER = 'myip.opendns.com'
REQUESTS_SERVER = 'ipinfo.io/ip'

def get_dns_egress_ip():
    try:
      ip = socket.gethostbyname(DNS_SERVER)
    except Exception as e:
      logging.error(f'Error: {e}')
      return
    logging.info(f'DNS egress IP: {ip}')

def get_requests_egress_ip():
    try:
      ip = requests.get(f'http://{REQUESTS_SERVER}').text
    except Exception as e:
      logging.error(f'Error: {e}')
      return
    logging.info(f'Requests egress IP: {ip}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    get_dns_egress_ip()
    get_requests_egress_ip()
