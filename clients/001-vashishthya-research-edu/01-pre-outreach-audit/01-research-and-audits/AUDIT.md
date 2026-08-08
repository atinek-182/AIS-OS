---
title: 'Phase 01: Pre-Outreach Vulnerability Audit & Deep Entity Teardown'
domain: audit
summary: '**Client:** Vashishthya Research & Educational Academy / IJORAR & MJAP Journals **Client ID:** `001-vashishthya-research-edu`'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- 'Phase 01: Pre-Outreach Vulnerability Audit & Deep Entity Teardown'
- 1. Lead Acquisition & Metadata
- 2. Forensic Technical & Web Architecture Audit
- 3. SEO, Google Scholar & Indexing Audit
- 4. Operational Bottlenecks & Manuscript Friction
read_triggers:
- When working on audit in clients/001-vashishthya-research-edu/01-pre-outreach-audit/01-research-and-audits/AUDIT.md
- 'When reading context for Phase 01: Pre-Outreach Vulnerability Audit & Deep Entity Teardown'
tags:
- audit
- AUDIT
updated: '2026-08-08'
---

# Phase 01: Pre-Outreach Vulnerability Audit & Deep Entity Teardown
**Client:** Vashishthya Research & Educational Academy / IJORAR & MJAP Journals  
**Client ID:** `001-vashishthya-research-edu`  
**Lead Channel:** Sister Network Warm Referral (Former Employee on IJORAR & MJAP)  
**Date:** 2026-08-03  
**Status:** Ingested & Deep Research Completed  

---

## 1. Lead Acquisition & Metadata
- **Lead Source / Channel**: Warm Referral via Operator's Sister (Former Employee Network on IJORAR & MJAP)
- **Key Decision Makers**:
  - **Dr. Prashant Singh** (Founder, Director, Chief Editor) — [LinkedIn Profile](https://www.linkedin.com/in/dr-prashant-singh-bb6b24b9)
  - **Dr. Pooja Singh** (Co-Founder, Executive Management) — [LinkedIn Profile](https://www.linkedin.com/in/dr-pooja-singh-aa3319114)
- **Entities & Web Footprint**:
  - **Main Academy**: [vashisthyaresearchedu.com](https://www.vashisthyaresearchedu.com/) (Email: `parsjp17@gmail.com` | WhatsApp/Phone: `8319353139`, `8349687471`)
  - **Journal 1 (IJORAR)**: International Journal of Original Recent Advanced Research — [ijorarjournal.com](https://ijorarjournal.com/) (ISSN 3107-538X)
  - **Journal 2 (MJAP)**: Multidisciplinary Journal of Academic Publications — [mjapjournal.com](https://mjapjournal.com/)
- **Target Niche / Industry**: Academic Research Consultancy, PhD Thesis Assistance, Journal Publishing (Open Access, Peer-Reviewed), Patent Services & Academic Awards
- **Verified Services & Pricing Catalog**: Documented in canonical [SERVICES_CATALOG.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/SERVICES_CATALOG.md) (7 core services: PhD Writing ₹20k, PG Dissertation ₹5k, Book Publication ₹3k-5k, Paper Writing ₹2k, Plagiarism Reports ₹100-200, Patents ₹15k, Academic Awards & Grants).
- **Positioning & Strategy**: **100% Free Value-First / Case Study Agreement** (Zero upfront charge in exchange for proof of work, video testimonial, AI Consultant title, and warm university/business referrals after 30-45 days).

---

## 2. Forensic Technical & Web Architecture Audit
- **Outdated / Unoptimized Assets**: Hand-coded static HTML/PHP with zero modern frameworks or build pipelines. High-resolution raster DOI logos (e.g. `2026-04-14-11-44-33-DOI_logo.svg.png` rendering at 768×768px and scaling to 1024px) severely bloat initial page load times. Lack of meaningful `alt` attributes across image tags.
- **Broken Links & Critical UI Bugs**: 
  - On both IJORAR and MJAP homepages, "Join As Board" and "Submit Manuscript" incorrectly link to an external unrelated journal domain (`ijariie.com`).
  - Vashisthya's "About Us" page returns a 500 server error.
  - Testimonial slider freezes indefinitely at "Loading...".
  - Visible spelling errors in HTML ("Standardes" instead of "Standards").
- **Unoptimized Frontend**: No minified CSS/JS. Inline styles, duplicate markup (`<a href="wa.me">Get Quote</a>` duplicated across every service item instead of dynamic components), missing responsive grid system.
- **Security & Trust Signals**: HTTPS enabled, but lacks visible security/SSL trust seals or ISO 9001 certificate verification links.
- **Mobile & Accessibility Deficiencies**: Zero `<meta name="viewport">` tags found across source code. Un-adapted fixed 768px images cause severe horizontal scroll breakages on mobile viewports. Zero ARIA accessibility attributes.

---

## 3. SEO, Google Scholar & Indexing Audit
- **Missing Scholarly Metadata**: Zero `<meta name="citation_*">` tags (`citation_title`, `citation_author`, `citation_publication_date`, `citation_pdf_url`) or Dublin Core tags present. Article details are rendered strictly as un-parsed plain HTML text, rendering the journals invisible to Google Scholar crawlers.
- **Zero Schema.org / JSON-LD Data**: Lacks `AcademicJournal` or `ScholarlyArticle` structured data scripts. Search engine crawlers have zero machine-readable publication context.
- **Poor Crawlability & PDF Hiding**: Papers are hidden 4+ layers deep behind form-driven "Current Issue" dropdowns without HTML abstract landing pages. Neither journal appears in Google Scholar, WorldCat, or Scopus index searches.

---

## 4. Operational Bottlenecks & Manuscript Friction
- **100% Email/WhatsApp Submission Flow**: Authors submit via raw email (`editor@ijorarjournal.com`, `editor@mjapjournal.com`, `parsjp17@gmail.com`). Zero online author portal or dashboard.
- **Manual Guideline Enforcement**: Manual `.docx` downloads (`IJORAR Manuscript Templet.docx`). Guideline verification, formatting checks, and version control handled manually across spreadsheets.
- **Ad Hoc Peer-Review Routing**: Reviewers selected from static board lists manually via email without automated reminders, deadline tracking, or AI matching.
- **Leaky WhatsApp Lead Funnel**: Shared WhatsApp number (`+91-8349687471`) used for all student inquiries. Staff spend hours manually asking 10-20 qualification questions per prospect.

---

## 5. Quantified Wasted Time & Revenue Leakage
- **Staff Hours Lost**: **50–100 staff-hours/month** lost on manual manuscript routing, formatting checks, reviewer nudging, and repetitive WhatsApp intake screening.
- **Lost Lead Revenue Leakage**: ~30–50% candidate drop-off rate due to delayed manual responses. Estimated **60 lost PhD/consulting leads/month**, translating to hundreds of thousands INR in lost annual revenue.

---

## 6. 50-Capability AI Transformation Roadmap

### (1) Intake & Scholar Screening AI
1. **Interactive Research Scope Calculator**: AI intake widget estimating thesis scope, timeline, and preliminary cost.
2. **Automated Qualification Chatbot**: Web/WhatsApp bot screening candidates on eligibility and degree credentials.
3. **Resume/CV Analyzer**: Extracts research history and scores PhD candidacy.
4. **Content-Based Journal Recommender**: Recommends best-fit journal (IJORAR vs MJAP) based on draft abstract.
5. **Multilingual Intake AI**: Auto-detects and greets candidates in Hindi, Sanskrit, or English.
6. **Lead Scoring Agent**: Ranks incoming leads by conversion probability for priority follow-up.
7. **Automated Scheduling Assistant**: Self-service calendar booking for free counselor calls.
8. **AI FAQ Bot**: Instant answers to common timeline, pricing, and process questions.
9. **Document Eligibility Scanner**: OCR + AI scanner verifying uploaded certificates.
10. **Email Triage Assistant**: Auto-categorizes inbound emails and routes to relevant staff.

### (2) Editorial & Manuscript Processing AI
11. **Formatting & Guideline Checker**: Auto-flags font, margin, and layout violations against journal templates.
12. **Citation & Reference Reformatter**: Formats raw references into APA / IEEE / Vancouver standards.
13. **Instant Plagiarism/Similarity Estimator**: Fast cross-reference check against open databases.
14. **Grammar & Clarity AI Editor**: Academic NLP enhancement suggestions.
15. **Figure/Table Quality Checker**: Verifies 300+ DPI image resolution and table styling.
16. **Automated Blindness Tool**: Strips author metadata for double-blind peer review.
17. **Manuscript Conversion Service**: Auto-converts Word/LaTeX drafts into publication XML/PDF.
18. **Metadata Harvester**: Extracts titles, abstracts, and keywords directly into CRM.
19. **Version Control Integrator**: Tracks revision changes and auto-generates diff change logs.
20. **Email Response Generator**: Drafts editorial decision letters for quick staff approval.

### (3) Peer-Review & Author Communication AI
21. **Automated Reviewer Matching**: Semantic matching of paper topics with registered reviewer expertise.
22. **Reviewer Reminder Agent**: Automated gentle nudge sequences for pending peer reviews.
23. **Interactive Status Bot**: Authors check live manuscript status on website anytime.
24. **Review Summarization AI**: Summarizes reviewer feedback points for chief editor review.
25. **Language Translation for Reviews**: Translates comments across non-English reviewer profiles.
26. **Peer Review Quality Check**: Evaluates reviewer feedback depth before acceptance.
27. **Decision Drafting Assistant**: Pre-fills acceptance/revision letters with reviewer notes.
28. **Author Response Tracker**: Compares author revision updates against reviewer requests.
29. **Virtual Editorial Assistant**: Slack/Teams query bot for editorial status ("Who is assigned to Paper #42?").
30. **Community Feedback Aggregator**: Summarizes author and conference satisfaction metrics.

### (4) Journal SEO & Metadata AI
31. **Meta-Tag Generator**: Injects `citation_*` and Dublin Core meta tags dynamically for Google Scholar.
32. **DOI/CrossRef XML Creator**: Auto-generates CrossRef XML deposits upon acceptance.
33. **Schema.org JSON-LD Builder**: Generates `AcademicJournal` and `ScholarlyArticle` schemas.
34. **Automated Alt-Text Generator**: Visual recognition model creating descriptive figure alt texts.
35. **Google Scholar Robot Checker**: Simulates crawler indexing health and flags missing metadata.
36. **Citation Alert Scanner**: Tracks crossref and Google Scholar for new citations of published papers.
37. **Structured Data Validator**: Scheduled Rich Results testing to maintain zero schema errors.
38. **Automated Sitemap & RSS**: Auto-updates XML sitemap and Atom feeds on paper publication.
39. **Keyword & Tag Recommender**: Recommends high-ranking SEO keywords for paper abstracts.
40. **Analytical Dashboard**: Tracks journal traffic trends and top academic search queries.

### (5) Central Operations & CRM AI
41. **Editorial Dashboard Integration**: Centralized Notion/Airtable sync tracking manuscript lifecycles.
42. **Automated Invoicing & APC Receipt**: Generates and emails APC invoices upon paper acceptance.
43. **Appointment & Calendaring AI**: Syncs editorial board schedules for mock defense sessions.
44. **Smart Contract Generator**: Auto-fills copyright transfer agreements and author contracts.
45. **Lead CRM AI**: Auto-syncs WhatsApp/web leads into CRM with lead stage tags.
46. **Newsletter/Content AI**: Auto-composes monthly digest of newly published journal papers.
47. **Questionnaire Analytics**: Aggregates post-publication author satisfaction surveys.
48. **Document Archiver**: OCRs and indexes past email attachments into searchable knowledge base.
49. **Multi-Channel Notification Bot**: Automated SMS/WhatsApp notifications for deadlines and payments.
50. **Performance Metric Generator**: Generates quarterly executive reports (acceptance rate, time-to-publish).

---

## 7. Zero-Upfront Pilot Pitch Proposal
- **Free Value Delivery (Phase 1)**: Deploy AI Intake Calculator + Automated Manuscript Guideline Checker + Google Scholar Meta Tag Generator within 4–6 weeks at **₹0 upfront cost**.
- **Return Value Request**:
  1. Official Case Study & Video Testimonial from Dr. Prashant Singh & Dr. Pooja Singh.
  2. Designation as "Fractional AI Systems Consultant" for Vashishthya Research.
  3. Warm introductions & referrals to their university/academic network.
