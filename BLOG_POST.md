# How We Built an Autonomous Incident War Room with Switch AI

*Published for the WeMakeDevs × DevTools Academy "Flip the Switch" Hackathon*  
*By Krish Punia*

---

Imagine getting paged at 3:15 AM on a Saturday. Production is throwing HTTP 500s on the checkout endpoint. You log onto Slack, ping three teammates, search Datadog for error traces, sift through dozens of recent GitHub commits, and debate whether to rollback or hotfix.

By the time the patch is live and the post-mortem is written, over 45 minutes have elapsed.

What if your team chat wasn't just a place where humans panic, but an active **War Room** where autonomous AI agents collaborate alongside you to diagnose, reproduce, patch, and document the incident in under 90 seconds?

In this article, I'll walk you through how I built **OpsSwitch** using **Switch AI**—an open-source platform that brings AI coding agents directly into team chat.

---

## 1. What is Switch AI?

Most AI coding tools (Claude Code, Cursor, Codex, OpenCode) live isolated inside a developer's terminal or IDE. But real engineering happens in teams, and team coordination happens in chat (Slack, Mattermost, Microsoft Teams, Discord).

Switch solves this by providing:
1. **Chat as a Room:** Every channel becomes an environment where multiple agents and humans coexist.
2. **First-Class Agent Identity:** Agents get their own avatars, names, and addressing rules (`addressing: anyone` or `addressing: owner-agents`).
3. **Agent Protocol:** Agents communicate via Server-Sent Events (SSE) and HTTP, allowing any custom agent or LLM framework to participate.
4. **Human-in-the-Loop Governance:** Built-in gates ensure that dangerous actions (like production deploys) require explicit human sign-off.

---

## 2. Designing the Incident Response Squad

In OpsSwitch, we created a specialized four-agent squad:

```
[ PagerDuty Alert ]
        │
        ▼
[@ops-sentinel] (Commander)  ──► Assesses SEV, summarizes impact
        │
        ▼
[@ops-sleuth]   (Investigator)──► Git blame, commit diff, root cause
        │
        ▼
[@ops-releaser] (Remediation) ──► Generates patch, verifies tests
        │
        ▼
[ Human Engineer ] (Gate)     ──► Replies "Approve"
        │
        ▼
[@ops-scribe]   (Chronicler)  ──► Markdown Post-Mortem delivered
```

### The Switch Template (`template.yaml`)

Switch allows you to define your entire multi-agent topology in a clean YAML template:

```yaml
version: 1

params:
  team:
    type: string
    default: ops
  repo_path:
    type: string
    default: "{$agents_dir}/demo-service"

agents:
  - name: "{team}-sentinel"
    description: Incident Commander
    addressing: anyone
    instructions: |
      Triage incoming error reports. Assign SEV-1, SEV-2, or SEV-3.
      Hand off code investigation to @{team}-sleuth with the exact stack trace.

  - name: "{team}-sleuth"
    description: Git & Code Investigator
    addressing: owner-agents
    instructions: |
      Inspect the repository. Run git log -n 5 and git blame.
      Pinpoint the exact commit and line causing the failure.
      Hand off to @{team}-releaser.

  - name: "{team}-releaser"
    description: Remediation & Deployment
    addressing: owner-agents
    instructions: |
      Prepare the hotfix and run local tests.
      SAFETY: Never deploy without explicit "Approve" from {$creator}.

  - name: "{team}-scribe"
    description: Incident Chronicler
    addressing: owner-agents
    instructions: |
      Compile the comprehensive post-mortem report once remediation is confirmed.

room:
  name: "{team}-incident-war-room"
  agents: ["{team}-sentinel", "{team}-sleuth", "{team}-releaser", "{team}-scribe"]
  users: ["{$creator}"]
```

---

## 3. The Live Walkthrough: From Outage to Resolution

### The Incident
In our test microservice (`cart-service`), a junior engineer pushed commit `8bae34d`:
```python
# Broken line in calculate_total():
discount = COUPONS[cart.coupon_code]  # Raises KeyError when coupon is invalid!
```

### The Autonomous Relay in Action
1. **Detection:** An error alert hits `#incident-war-room`:
   > `CRITICAL: 500 Spike on /api/v2/checkout (KeyError: 'INVALID_PROMO')`
2. **Triage:** `@ops-sentinel` declares SEV-2, notes that unauthenticated shoppers with promo codes are blocked, and addresses `@ops-sleuth`.
3. **Investigation:** `@ops-sleuth` runs `git blame` and catches commit `8bae34d` within 15 seconds. It notes that `COUPONS.get(cart.coupon_code, 0.0)` was needed.
4. **Remediation & Human Gate:** `@ops-releaser` prepares the patch, executes `python3 test_service.py` to confirm 2/2 tests pass, and tags me:
   > *"@Krish Punia: Hotfix verified locally. Reply 'Approve' to deploy."*
5. **Approval & Deploy:** I review the one-line diff and type `"Approve"`.
6. **Documentation:** `@ops-scribe` posts a complete Markdown post-mortem with 5 Whys, timeline, and action items.

Total resolution time: **91 seconds**.

---

## 4. Key Takeaways & What I Learned

1. **Multi-Agent Specialization Beats Monolithic Prompts:** Giving each agent a distinct role (Sentinel vs. Sleuth vs. Releaser vs. Scribe) prevented context pollution and hallucinations.
2. **Human Gates Are Mandatory for Enterprise Trust:** Autonomous agents must be safe by design. Switch's addressing model makes human sign-offs natural and reliable.
3. **Chat is the Natural Home for AI Teammates:** Instead of switching between 5 browser tabs and terminals during an emergency, having your agents live in your team chat keeps everyone aligned.

---

## 5. Try It Yourself

You can explore the complete repository, Switch template, and reproduction harness here:
👉 **[GitHub: kpunia306/ops-switch](https://github.com/kpunia306/switch)**

Special thanks to **WeMakeDevs**, **DevTools Academy**, and the **Switch AI** team for hosting this fantastic hackathon!
