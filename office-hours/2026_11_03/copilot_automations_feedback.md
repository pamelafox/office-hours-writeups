# GitHub Copilot app automations: Issues from the Nov 3 office hours demo

Recording: [Python + AI Office Hours, Nov 3, 2026](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=856)

## 1. CRON triggers can't run in the cloud

📹 [17:40](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=1060)

The CRON trigger has no "Run in the cloud" toggle, unlike Daily, Weekly, and Hourly. So CRON automations can't run in the cloud or be shared. I expected CRON to support cloud runs too.

## 2. Automations created from a description default to CRON

📹 [15:30](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=930)

I asked for an automation "every day at 10 p.m.", and it generated a CRON trigger (`0 22 * * *`) instead of Daily. Because of issue 1, it then couldn't run in the cloud or be shared. I'd expect it to prefer Daily/Weekly/Hourly when they fit.

## 3. "Repository not found" error when creating a shared cloud automation

📹 [29:25](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=1765)

Creating a shared cloud automation for `Azure-Samples/azure-search-openai-demo` failed with the error below, even though I already have other automations on that repo. Retrying didn't help, but `pamelafox/pamelafox-site` worked.

> Error: Could not check cloud automation availability. github API request failed (404): GitHub API request failed (404 Not Found): Repository not found [request_id=E8C7:336D37:1C6DBD:2863EC:6AEA37C5]

## Feature request: Generic webhook trigger

📹 [18:20](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=1100)

Triggers only cover schedules and GitHub events. An attendee asked for a generic webhook trigger to start automations from non-GitHub systems.

## Question: Can an existing automation be changed to shared?

📹 [28:27](https://www.youtube.com/watch?v=6Vu0_W1OzWk&t=1707)

**Shared** is available when creating an automation, but it's unclear whether an existing one can be switched to shared later.
