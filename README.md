### ethereum-fee-calculator

### Usage

```
usage: ethereum_fee_calculator.py [-h] rpc_url gas_used

calculates fees in USD for the ethereum blockchain

positional arguments:
  rpc_url
  gas_used
```

### Example

```
./ethereum_fee_calculator.py https://cloudflare-eth.com 21000

1 ETH: 1219.47$
gas price: 10.68920662 gwei (also see https://etherscan.io/gastracker)
fee: 0.00022447 ETH <=> 0.27373850$
```
