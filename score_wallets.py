import json
import pandas as pd
from collections import defaultdict
from features import extract_features
from model import compute_score

with open("data/user-wallet-transactions.json") as f:
    transactions = json.load(f)

wallets = defaultdict(list)

# Group by 'userWallet'
for tx in transactions:
    if 'userWallet' in tx:
        wallets[tx['userWallet']].append(tx)

# Score each wallet
results = []
for wallet, txns in wallets.items():
    features = extract_features(txns)
    score = compute_score(features)
    results.append({'wallet': wallet, 'score': score})

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("wallet_scores.csv", index=False)
print("Output saved to wallet_scores.csv")

