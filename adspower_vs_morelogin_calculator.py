#!/usr/bin/env python3
"""AdsPower vs MoreLogin Cloud Phone & Browser Hybrid TCO Calculator 2026."""
import argparse

def calculate(desktop_profiles=100, cloud_phones=10, annual=True):
    # AdsPower: 100 desktop prof ~$40/mo (annual). Cloud phone add-ons ~$2.50/instance -> $25/mo. Total ~$65/mo.
    adsp_desktop = 40.0 if annual else 50.0
    adsp_phone = cloud_phones * 2.50
    adsp_total = adsp_desktop + adsp_phone

    # MoreLogin: Pro 100 prof $32/mo (annual). Cloud phone add-ons ~$2.00/instance -> $20/mo. Total ~$52/mo.
    more_desktop = 32.0 if annual else 40.0
    more_phone = cloud_phones * 2.00
    more_total = more_desktop + more_phone

    monthly_diff = adsp_total - more_total
    annual_diff = monthly_diff * 12.0

    print("=" * 65)
    print("AdsPower vs MoreLogin: Hybrid Browser + Cloud Phone TCO")
    print("=" * 65)
    print(f"Fleet Scale:               {desktop_profiles} Desktop Profiles + {cloud_phones} Cloud Phones")
    print(f"AdsPower Hybrid Monthly:   ${adsp_total:.2f}/mo (${adsp_total * 12:.2f}/yr)")
    print(f"MoreLogin Hybrid Monthly:  ${more_total:.2f}/mo (${more_total * 12:.2f}/yr)")
    print(f"Monthly Cost Difference:   ${monthly_diff:.2f}/mo (MoreLogin Advantage)")
    print(f"Annual Capital Saved:      ${annual_diff:.2f}/yr")
    print("=" * 65)
    return more_total, adsp_total, annual_diff

if __name__ == "__main__":
    calculate()
