#!/usr/bin/env python3
"""
OpsSwitch War Room Simulation
Simulates the autonomous multi-agent incident response flow powered by Switch AI.
"""

import time
import sys

def print_message(sender, role, text, delay=1.0):
    time.sleep(delay)
    badge = f"[{role.upper()}]" if role else ""
    print(f"\n💬 \033[1;36m{sender}\033[0m \033[33m{badge}\033[0m")
    print(f"   {text}")

def main():
    print("="*70)
    print("🚨 OPSSWITCH INCIDENT WAR ROOM - LIVE RUNTIME DEMO")
    print("   Room: #incident-checkout-500s | Bridge: Mattermost / Slack")
    print("="*70)

    # 1. Human / Alert trigger
    print_message("PagerDuty Webhook", "ALERT", 
                  "CRITICAL: 500 Internal Server Error spike on /api/v2/checkout (cart-service).\n"
                  "   Error Signature: KeyError: 'INVALID_PROMO' at service.py:31 in calculate_total", 
                  delay=0.5)

    # 2. Sentinel acknowledges & triages
    print_message("ops-sentinel", "Commander",
                  "🚨 **SEV-2 INCIDENT DECLARED: Checkout Service Failure**\n"
                  "   - **Impact**: Customers using unrecognized coupon codes are blocked at checkout.\n"
                  "   - **Affected Endpoint**: `POST /api/v2/checkout`\n"
                  "   - **State**: Triage complete. Handing off to code investigator.\n"
                  "   @ops-sleuth please inspect `demo-service` git history and pinpoint the breaking commit.", 
                  delay=1.0)

    # 3. Sleuth investigates
    print_message("ops-sleuth", "Investigator",
                  "🔍 **Root Cause Identified via Git Blame & Commit History**:\n"
                  "   - **Culprit Commit**: `8bae34d` ('feat(coupons): direct discount calculation v1.2.1')\n"
                  "   - **Author**: junior-dev@example.invalid\n"
                  "   - **Root Cause**: `COUPONS[cart.coupon_code]` does an unchecked dictionary lookup instead of `COUPONS.get(cart.coupon_code, 0.0)`. Any invalid promo code crashes checkout.\n"
                  "   @ops-releaser: Recommended remediation is applying safe `.get()` fallback or rolling back to `v1.2.0`.", 
                  delay=1.2)

    # 4. Releaser prepares hotfix & asks for human approval
    print_message("ops-releaser", "Remediation",
                  "🛠️ **Hotfix Prepared & Local Verification Passed**:\n"
                  "   ```diff\n"
                  "   - discount = COUPONS[cart.coupon_code]\n"
                  "   + discount = COUPONS.get(cart.coupon_code, 0.0)\n"
                  "   ```\n"
                  "   ✅ Local test suite: 2/2 tests passed in `test_service.py`.\n\n"
                  "   🛡️ **SAFETY GATE**: @Krish Punia please review the diff above and reply **'Approve'** to deploy hotfix to production.", 
                  delay=1.2)

    # 5. Human approval
    print_message("Krish Punia", "Human Lead",
                  "@ops-releaser Approved. Roll it out immediately.", 
                  delay=1.5)

    # 6. Releaser deploys
    print_message("ops-releaser", "Remediation",
                  "🚀 **Hotfix Deployed to Production**: v1.2.2 is live. /api/v2/checkout error rate dropped to 0.0%.\n"
                  "   @ops-scribe please generate the official post-mortem review.", 
                  delay=1.0)

    # 7. Scribe documents post-mortem
    print_message("ops-scribe", "Chronicler",
                  "📝 **INCIDENT POST-MORTEM REPORT**\n"
                  "   - **Incident**: Checkout 500s on Unrecognized Coupons (SEV-2)\n"
                  "   - **Time to Triage**: 14 seconds (via @ops-sentinel)\n"
                  "   - **Time to Root-Cause**: 32 seconds (via @ops-sleuth)\n"
                  "   - **Time to Remediation**: 45 seconds (Human Sign-off via @Krish Punia)\n"
                  "   - **Total Downtime**: 1m 31s (Saved ~45 minutes vs manual engineer paging)\n"
                  "   - **Action Item**: Add mandatory schema validation on coupon input fields before release.", 
                  delay=1.5)

    print("\n" + "="*70)
    print("✅ INCIDENT SUCCESSFULLY RESOLVED & ARCHIVED VIA SWITCH")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
