# Trace South recap delivery and expose missing receipts

South has 20 late posts among 40 calls; its 34 posts have a 74-minute median delay ([data](calls.csv), [calculation](extra/metrics.py)). Marcus wants delivery in 10 to 15 minutes ([feedback](slack-thread.txt)). The slow stage is unknown; a skill cannot diagnose queues or verify Slack delivery.

Deliver one call-ID-linked event trail: call end, transcript ready, queue entry/exit, generation complete and confirmed channel-post receipt. Show failed and pending stages, including calls that never enter generation. Keep transcript content out of telemetry.

Accept when every call in the agreed pilot roster has either a verified post receipt or an explicit missing/failed status; injected queue and posting failures remain visible. Recompute 15/60-minute delivery over all held calls from receipts. Missing timestamps must remain unknown, never zero-duration successes. Use traces to choose the next fix.
