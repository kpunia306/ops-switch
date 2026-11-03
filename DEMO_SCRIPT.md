# 🎥 2-Minute Demo Video Script: OpsSwitch

> **Recording Tip:** Keep your video under 2 minutes 30 seconds. Speak clearly. Show your terminal/Mattermost/Switch Console screen.

---

### [0:00 - 0:25] Introduction & The Problem
**Visual:** Screen showing `#incident-war-room` in chat / terminal.  
**Voiceover:**
> *"Hi everyone, I'm Krish Punia, and this is **OpsSwitch: Autonomous Incident Commander & War Room**, built for the Flip the Switch Hackathon.  
> When production outages happen, engineering teams waste 30 to 45 minutes context-switching between monitoring tools, git logs, and Slack threads.  
> OpsSwitch brings an autonomous squad of specialized AI agents right into your team chat with Switch AI to solve incidents in under 90 seconds."*

---

### [0:25 - 1:15] The Live Incident Demo
**Visual:** Run `python3 simulate_incident.py` or trigger the alert in chat.  
**Voiceover:**
> *"Here, an alert fires on our checkout microservice: HTTP 500s due to a KeyError.  
> Watch the multi-agent relay:  
> First, **@ops-sentinel** immediately triages the alert, declares a SEV-2 incident, and hands off the stack trace to **@ops-sleuth**.  
> Next, **@ops-sleuth** dives into the repository, checks git blame and commit logs, and isolates the breaking commit: an unhandled promo code lookup in `service.py`.  
> Then, **@ops-releaser** prepares the exact fix, runs local verification tests, and pauses at our safety gate: asking me, the human lead, for explicit approval before touching production."*

---

### [1:15 - 1:45] Human Approval & Post-Mortem
**Visual:** Show typing `@ops-releaser Approve`, followed by the deployment and post-mortem output.  
**Voiceover:**
> *"I reply 'Approve'.  
> The agent deploys the patch, error rates drop back to zero, and **@ops-scribe** instantly publishes a comprehensive post-mortem report with timelines, root cause analysis, and preventative action items."*

---

### [1:45 - 2:00] Architecture & Conclusion
**Visual:** Show the `incident-war-room.template.yaml` and GitHub repo.  
**Voiceover:**
> *"Under the hood, Switch connects these agents to our chat bridge and enforces addressing rules and safety gates.  
> OpsSwitch turns AI coding agents into true teammates that get real work done when every second counts.  
> Thank you, and Flip the Switch!"*
