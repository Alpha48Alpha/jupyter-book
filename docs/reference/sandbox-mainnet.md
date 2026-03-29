# Move from a sandbox/test network to Ethereum mainnet safely

If you are currently connected to a **sandbox/test RPC** (for example a temporary BuildBear endpoint), you can switch to Ethereum mainnet by adding/selecting the official network.

## 1) Secure your wallet first (critical)

If your private key was ever exposed in screenshots, chat, cloud backups, or messages, treat that wallet as compromised.

1. Create a **new wallet** (new seed phrase / private key).
2. Back up the new seed phrase offline.
3. Move funds/assets to the new wallet only after confirming destination details.
4. Stop using the exposed key permanently.

## 2) Add/select Ethereum Mainnet network

In most wallets:

1. Open **Wallet Settings → Networks**.
2. Choose **Ethereum Mainnet** from the default list.
3. If manual entry is required, use:
   - **Network Name:** Ethereum Mainnet
   - **RPC URL:** `https://ethereum.publicnode.com` (or your trusted provider)
   - **Chain ID:** `1`
   - **Currency Symbol:** `ETH`
   - **Block Explorer URL:** `https://etherscan.io`
4. Save and switch to this network.

## 3) Verify you are on mainnet

- Chain ID must read `1`.
- Explorer links should open on `etherscan.io` (not a sandbox explorer).
- Addresses still look the same format; only the network context changes.

## 4) Important notes

- Testnet/sandbox ETH is not real ETH and cannot be bridged 1:1 to mainnet.
- Mainnet transactions require real ETH for gas.
- Send a tiny test transaction first when using a new address.
