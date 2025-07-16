def compute_score(f):
    score = 0
    score += min(f['total_deposited'] / 1000, 200)
    score += min((1 - f['borrow_to_deposit_ratio']) * 200, 200)
    score += min(f['repayment_ratio'] * 300, 300)
    score -= min(f['num_liquidations'] * 100, 200)
    score += min(f['active_days'] * 5, 100)
    score += min(f['total_redeemed'] / 1000, 100)  
    return round(max(min(score, 1000), 0))