---
name: ai-pricing-engine
description: AI Solution Pricing Calculator & Proposal Compiler based on Nate Herk's Masterclass. Calculates client-stated value ceiling, delivery cost floor, defensible price corridor (10%-20%), 10X ROI check, 3-option micro-service proof architecture, objective milestone breakdown, and maintenance retainers. Invokable via /ai-pricing-engine or natural language.
argument-hint: '[client_name_or_niche] [optional_workflow]'
---

# ZORIXEL AI Solution Pricing Engine (`/ai-pricing-engine`)

## ⚡ Overview & Tri-Mode Execution

This skill is the definitive pricing, proposal, and ROI calculator for ZORIXEL AI agency engagements. Built directly from Nate Herk's *How to Price AI Solutions: The Complete Masterclass*, it converts raw client discovery numbers into a mathematical, defensible price corridor, 10X ROI proof, and a staged 3-option micro-service proposal.

Invokable via:
- **Slash Command**: `/ai-pricing-engine [client_name]`
- **Dynamic Intent**: Triggered when discussing proposal pricing, ROI calculations, client quotes, or scoping project tiers.
- **Programmatic Inter-Skill Calling**: Called by parent skills (`/grill-me`, `/new-project`, `/website-design-engine`, `/mattpocock-to-spec`).

---

## 💎 Core Pricing Philosophy: "Cost Floor, Value Ceiling, Defensible Price"

> **The Single Golden Rule**: Never state a price before getting the client to state what the problem costs the business. Cost is your floor, Value is the client's ceiling, and Price lives between them.

```
+-----------------------------------------------------------------------+
|  VALUE CEILING  (Client-Stated First-Year Economic Impact)            |
|  • Annual Labor Saved + Error Costs Avoided + Revenue Capacity        |
+-----------------------------------------------------------------------+
                                  ▲
                                  │  Price Corridor (10% - 20% of Value)
                                  ▼
+-----------------------------------------------------------------------+
|  COST FLOOR  (Delivery Labor + Testing + Infra + Margin)               |
+-----------------------------------------------------------------------+
```

---

## 🛠️ Step-by-Step 8-Phase Pricing Protocol

### Phase 1: Baseline Capture (Time Lens & Income Lens)

Gather client-supplied numbers before discussing any solution:

1. **Time Lens (Manual Labor Capacity)**:
   $$\text{Annual Labor Value} = \text{Volume/Period} \times \text{Hours/Item} \times \text{Loaded Labor Rate} \times \text{Periods/Year}$$
   *(Loaded rate includes salary, benefits, overhead, taxes — typically 1.25x–1.4x base wage).*

2. **Avoided Error Cost**:
   $$\text{Annual Avoided Error Value} = \text{Incidents/Month} \times \text{Cost/Incident} \times 12 \times \text{Expected Reduction \%}$$
   *(Includes refunds, rework, missed appointments, rush shipping, churn).*

3. **Income Lens (Growth Constraints & Revenue Capacity)**:
   $$\text{Annual Revenue Capacity} = \text{Additional Qualified Opps} \times \text{Contribution/Outcome} \times \text{Conversion Rate}$$
   *(Use contribution margin, NOT gross revenue).*

4. **Credible First-Year Value Ceiling**:
   $$\text{First-Year Value} = (\text{Labor Value} + \text{Error Value} + \text{Revenue Value}) \times \text{Confidence Adjuster (50\%--90\%)}$$

---

### Phase 2: Calculate Delivery Cost Floor

Determine the lowest responsible price before adding profit:

1. **Delivery Labor**: Hours required for design, workflow build, UI dashboard, and testing $\times$ internal hourly rate.
2. **Testing & Evaluation Burden**: Add **$1,000 to $3,000** for model evals, adversarial test sets, and edge case validation.
3. **Specialist / Infrastructure Costs**: Contractor fees + temporary testing API usage.
4. **Target Gross Margin Check**:
   $$\text{Required Price Floor} = \frac{\text{Total Delivery Cost}}{1 - \text{Target Gross Margin (e.g. 0.60)}}$$

---

### Phase 3: Calculate Defensible Price Corridor & 10X Check

1. **Starting Price Range**: $10\% \text{ to } 20\%$ of Credible First-Year Value Ceiling.
2. **The 10X ROI Check**:
   $$\text{Value Multiple} = \frac{\text{Credible First-Year Value}}{\text{Proposed Project Price}}$$
   - **$\ge 10\text{X}$**: Extremely easy sale; client sees $10 value for every $1 invested.
   - **$5\text{X}$ to $10\text{X}$**: Solid strategic project; present upside case.
   - **$< 5\text{X}$**: Re-scope down to high-impact micro-services or reduce risk.

---

### Phase 4: Staged Micro-Service Proof & Option Architecture

To prevent client anxiety and eliminate price friction, present **3 Distinct Options** (never quote a single number):

| Option Tier | Scope & Deliverables | Target Pricing | Target ROI |
|---|---|---|---|
| **Option 1: Essential** *(Micro-Service Proof)* | **1–2 Priority Micro-Service Workflows**, core API integration, basic approval card UI, 30-day proof review. | **$1,500 – $3,000** *(or 10% of base labor value)* | **10X+ ROI** |
| **Option 2: Growth** *(Recommended)* | **Everything in Essential + connected secondary workflows**, custom Next.js control dashboard, team training, 60-day optimization window. | **$5,000 – $10,000** | **7X–10X ROI** |
| **Option 3: Scale** *(Enterprise)* | **Everything in Growth + multi-team RBAC permissions**, advanced evals, executive analytics dashboard, priority SLA retainer. | **$12,000 – $25,000+** | **5X–10X ROI** |

---

### Phase 5: Objective Milestone Payment Structure

Limit unpaid exposure to 30 days. Payments follow observable test milestones, NOT emotional approval:

- **Milestone 1 (33% at Signing)**: Project kickoff, access collection, process map finalization.
- **Milestone 2 (33% at Proof of Concept)**: System testable in staging environment with synthetic sample data.
- **Milestone 3 (34% at Production Handoff)**: Credentials transferred to client-owned accounts, live launch, documentation delivered.

---

### Phase 6: Production Utilities & Client Ownership

- **Client Card / Client Account Mandate**: API keys (Anthropic, OpenAI), cloud subscriptions (Supabase, Vercel), telephony, and scraping tokens sit strictly in the **client's account and on the client's payment card**.
- **Run Cost Estimate**: State expected monthly model/cloud utility costs clearly in proposal (e.g. *"Estimated production run cost: $150/mo at 10,000 items"*).

---

### Phase 7: Maintenance Retainers vs. Roadmap Retainers

Separation of ongoing health from new feature development:

- **System Maintenance Retainer ($400 – $1,200/mo)**: Health monitoring, error log review, API schema updates, model version changes. *No new features.*
- **Roadmap & Expansion Retainer ($1,500 – $3,500+/mo)**: Dedicated monthly engineering capacity to build next backlog items and new workflow integrations.

---

### Phase 8: One-Minute Price Script Generator

Generate the exact mathematical closing script for Atinek Maurya:

> *"Your team is currently spending [X hours/week] on [Process], costing roughly $[First-Year Value] in manual labor and avoidable errors each year. Our Option 1 Micro-Service Proof is priced at $[Option 1 Price], which represents just [X%] of that annual cost and delivers a [Value Multiple]X return on your investment in the first 30 days. The system runs on your own API accounts, includes a human-in-the-loop approval dashboard, and comes with full code ownership. Should we start with Option 1 or Option 2?"*

---

## 📝 Output Artifact Format (`proposals/pricing-{client-slug}.md`)

When executing this skill, output a structured proposal pricing sheet containing:
1. Client Baseline & Value Calculation Table
2. Cost Floor & Margin Check
3. 3-Option Proposal Table (Essential, Growth, Scale)
4. Objective Milestone Payment Schedule
5. Estimated Monthly Production Run Costs
6. 1-Minute Closing Script

---

## 🔗 Inter-Skill Connections
- **Discovery Input**: Ingests client numbers from **`/grill-me`** and **`context/aios-intake.md`**.
- **Spec Architecture**: Feeds pricing tiers into **`/mattpocock-to-spec`** and **`/jsmastery-scope`**.
- **Audit Gate**: Passes proposed pricing and contract terms to **`/roast`** for margin validation.
