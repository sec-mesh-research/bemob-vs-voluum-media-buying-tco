#!/usr/bin/env python3
"""
BeMob vs Voluum Media Buying TCO Calculator 2026.
"""
import argparse

def calculate(events, bot_ratio):
    # BeMob Basic: $49/mo (1M events, $0.05/k overage)
    bm_base = 49.0
    bm_overage = (max(0, events - 1000000) / 1000.0) * 0.05
    bm_total = bm_base + bm_overage

    # Voluum Profit: $199/mo (1M events, $0.06/k overage). Includes Anti-Fraud Shield
    vol_base = 199.0
    vol_overage = (max(0, events - 1000000) / 1000.0) * 0.06
    vol_total = vol_base + vol_overage

    # Saved ad spend by detecting bots ($0.03 avg CPC on pop/native)
    detected_bot_clicks = events * bot_ratio
    bot_waste_saved = detected_bot_clicks * 0.03
    net_voluum = vol_total - bot_waste_saved

    print("=" * 60)
    print("Media Buying TCO: BeMob vs Voluum + Fraud Detection")
    print("=" * 60)
    print(f"Monthly Traffic:         {events:,} events")
    print(f"Estimated Bot Traffic:   {bot_ratio*100:.1f}% ({int(detected_bot_clicks):,} clicks)")
    print(f"BeMob Monthly Cost:      ${bm_total:.2f}/mo")
    print(f"Voluum Monthly Cost:     ${vol_total:.2f}/mo")
    print(f"Voluum Bot Waste Saved:  ${bot_waste_saved:,.2f}/mo (@ $0.03/CPC)")
    print(f"Effective Net Voluum:    ${net_voluum:.2f}/mo")
    print("=" * 60)
    return bm_total, net_voluum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BeMob vs Voluum Calculator")
    parser.add_argument("--events", type=int, default=2000000)
    parser.add_argument("--bot-ratio", type=float, default=0.08)
    args = parser.parse_args()
    calculate(args.events, args.bot_ratio)
