# Make recap delivery measurable and safe

South has 20 late posts among 40 calls; its 34 posts have a 74-minute median delay ([log](calls.csv), [calculation](extra/metrics.py)). Marcus wants recaps posted in 10 to 15 minutes ([feedback](slack-thread.txt)). Instructions alone cannot provide call capture, delivery receipts or queue diagnostics.

Instrument call end, transcript readiness, queue wait, generation, review and channel-post receipt. Trace South misses before selecting a fix. Add a five-minute fallback alert, manual takeover and retry-safe posting. West records only 4/30 calls; scope consent-aware WhatsApp capture or confirmed notes with Lena ([context](brain/NOW.md)).

Accept when a pilot reports complete posts within 15/60 minutes over all held calls, failures remain visible, receipts verify delivery, and retry/manual-takeover tests produce no duplicate posts. Fix East's denominator: 21/30, not 21/28 ([dashboard](adoption.csv)).
