# Wallet Credit Scoring - Aave V2

## Overview

This assignment aims to assign a credit score (ranging from 0 to 1000) to wallets based on their historical transaction behavior with the Aave V2 protocol. The score reflects the reliability of a user in decentralized finance (DeFi) and is derived from raw transaction-level data. Higher scores indicate more responsible and trustworthy behavior, while lower scores suggest risky, exploitative, or bot-like activity.

## Objective

Given a JSON file of historical Aave V2 transactions, the task is to:
- Engineer relevant financial and behavioral features.
- Score each wallet based on its activity.
- Output a CSV file containing wallet addresses and their scores.

## Methodology

### Feature Engineering

We analyze each wallet's interaction with Aave V2 and extract the following features:

- `total_deposited`: Sum of all deposits made.
- `total_borrowed`: Sum of all borrow actions.
- `total_repaid`: Total repayments made.
- `total_redeemed`: Funds withdrawn through the `redeemUnderlying` action.
- `repayment_ratio`: Ratio of repayments to borrowed amount.
- `borrow_to_deposit_ratio`: Ratio of borrowed to deposited value.
- `num_liquidations`: Count of liquidation events.
- `active_days`: Number of unique days with wallet activity.
- `wallet_lifetime_days`: Number of days between the first and last transaction.
- `tx_frequency`: Average number of days between transactions.

These features provide insight into a wallet's risk profile, repayment behavior, and consistency of protocol usage.

### Scoring Logic

The scoring is a rule-based approach computed as:
- +200 max for total deposited (scaled)
- +200 max for low borrow-to-deposit ratio
- +300 max for high repayment ratio
- -200 max for number of liquidations
- +100 max for activity days
- +100 max for amount redeemed

The total score is clamped between 0 and 1000.

## Architecture and File Structure

```
aave-credit-scoring/
│
├── data/
│   └── user-wallet-transactions.json   # Raw input JSON
│
├── features.py                         # Extracts transaction features
├── model.py                            # Scoring logic
├── score_wallets.py                    # Main runner script
├── wallet_scores.csv                   # Output wallet scores
├── README.md                           # Project overview
└── analysis.md                         # Post-score analysis
```


## Processing Flow

1. **Data Load:** Read JSON transaction file into Python.
2. **Wallet Grouping:** Group transactions by unique wallet address.
3. **Feature Extraction:** Extract features from grouped transactions using `features.py`.
4. **Score Computation:** Use `model.py` to compute score per wallet.
5. **CSV Export:** Save the final output to `wallet_scores.csv`.

## How to Run

### Prerequisites

- Python 3.8+
- pandas

### Steps

1. Clone this repository or download the files.
2. Place the transaction JSON file into the `data/` directory.
3. Create a virtual environment and install dependencies:
    pip install pandas
4. Run the scoring script:
    python score_wallets.py
5. The output will be saved as `wallet_scores.csv`.
