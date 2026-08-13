---
status: published
published: https://www.linkedin.com/feed/update/urn:li:activity:7493327003966656512/
---

# Accenture's token bill is a product roadmap

---

Leaked meeting audio from Accenture (via 404 Media, surfaced by Simon Willison): their biggest token chewer isn't the engineers. It's non-engineers converting PDFs to images to markdown, over and over.

The easy reaction is to laugh at the waste and send a memo telling people to stop.

The right reaction is to recognize what you're looking at: latent demand.

Boris Cherny (creator of Claude Code) calls latent demand the single most important principle in product. People repurpose whatever tool they have to do what they actually need. Facebook Marketplace exists because someone noticed 40% of Facebook group posts were people buying and selling stuff. Groups were never designed for commerce; the demand was just leaking through.

Non-engineers burning vision-model tokens on PDF conversion is the same signal. Nobody misusing anything; an unmet need shouting through your usage telemetry.

So don't police it. Productize it. Ship an MCP server or a local CLI: deterministic extraction for the easy 90% of PDFs, a vision-model fallback for the hard 10% (scans, gnarly tables). Spend tokens on judgment, not plumbing.

Tudor Girba's moldable development makes the general case: don't brute-force understanding with generic tools, mold small, deterministic, contextual tools around each recurring problem. That applies to business workflows just as much as to code.

The playbook: instrument your AI usage, read the telemetry like Cherny reads it, mold the tool like Girba would.

Your token bill might be the cheapest product research you'll ever get, if you treat it as telemetry.

---

## Sources

- Simon Willison: https://simonwillison.net/2026/Aug/7/pdfs-are-terrible/
- 404 Media, "The Tokenpocalypse Is Here" (June 24): https://www.404media.co/the-tokenpocalypse-is-here-companies-are-scrambling-to-stop-spending-so-much-on-ai/
- Boris Cherny on Lenny's Podcast, "What happens after coding is solved": https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens
- Glamorous Toolkit / moldable development: https://gtoolkit.com/
