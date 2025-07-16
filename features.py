import pandas as pd

def extract_features(transactions):
    rows = []
    for tx in transactions:
        try:
            rows.append({
                "timestamp": pd.to_datetime(tx["timestamp"], unit='s'),
                "action": tx["action"].lower(),
                "amount": float(tx["actionData"]["amount"])
            })
        except (KeyError, ValueError):
            continue  

    if not rows:
        return {
            "total_deposited": 0,
            "total_borrowed": 0,
            "total_repaid": 0,
            "total_redeemed": 0,
            "repayment_ratio": 0,
            "borrow_to_deposit_ratio": 0,
            "num_liquidations": 0,
            "active_days": 0,
            "wallet_lifetime_days": 0,
            "tx_frequency": 0
        }

    df = pd.DataFrame(rows)

    total_deposited = df[df['action'] == 'deposit']['amount'].sum()
    total_borrowed = df[df['action'] == 'borrow']['amount'].sum()
    total_repaid = df[df['action'] == 'repay']['amount'].sum()
    total_redeemed = df[df['action'] == 'redeemunderlying']['amount'].sum()
    num_liquidations = len(df[df['action'] == 'liquidationcall'])
    active_days = df['timestamp'].dt.date.nunique()

    borrow_to_deposit_ratio = total_borrowed / total_deposited if total_deposited else 0
    repayment_ratio = total_repaid / total_borrowed if total_borrowed else 0

    lifetime_days = (df['timestamp'].max() - df['timestamp'].min()).days
    tx_frequency = lifetime_days / len(df) if len(df) > 1 else 0

    return {
        "total_deposited": total_deposited,
        "total_borrowed": total_borrowed,
        "total_repaid": total_repaid,
        "total_redeemed": total_redeemed,
        "repayment_ratio": repayment_ratio,
        "borrow_to_deposit_ratio": borrow_to_deposit_ratio,
        "num_liquidations": num_liquidations,
        "active_days": active_days,
        "wallet_lifetime_days": lifetime_days,
        "tx_frequency": tx_frequency
    }
