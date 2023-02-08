#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip3 install requests web3

import argparse
import requests
import web3

parser = argparse.ArgumentParser(description="calculates fees in USD for the ethereum blockchain")
parser.add_argument("rpc_url")
parser.add_argument("gas_used", type=int)
args = parser.parse_args()

web3 = web3.Web3(web3.Web3.HTTPProvider(args.rpc_url))

response = requests.get("https://api.coingecko.com/api/v3/simple/price", {"ids": "ethereum", "vs_currencies": "usd"})
ethereum_price_in_usd = response.json()["ethereum"]["usd"]

print(f"1 ETH: {ethereum_price_in_usd}$")

gas_price_in_wei = web3.eth.gas_price
gas_price_in_gwei = web3.fromWei(gas_price_in_wei, "gwei")

print(f"gas price: {gas_price_in_gwei} gwei (also see https://etherscan.io/gastracker)")

wei_used = args.gas_used * gas_price_in_wei
fee_in_eth = float(web3.fromWei(wei_used, "ether"))
fee_in_usd = fee_in_eth * ethereum_price_in_usd

print(f"fee: {fee_in_eth:.8f} ETH <=> {fee_in_usd:.8f}$")
