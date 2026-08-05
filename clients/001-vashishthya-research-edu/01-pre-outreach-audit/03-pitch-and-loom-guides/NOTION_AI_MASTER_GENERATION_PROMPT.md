# Master Notion AI Prompt: Vashishthya Master Client OS Database

Copy and paste the exact prompt below into Notion AI (press `Spacebar` or click `Ask AI` on a blank page in Notion):

```text
Create a complete Master Database named "Vashishthya Master Client Desk" for an academic research consultancy foundation.

Structure this database with the following 18 properties, exact select options, formulas, and 3 custom views:

1. PROPERTIES SETUP:
- "Scholar Name" (Title)
- "Contact / WhatsApp Number" (Phone)
- "Email Address" (Email)
- "Services Required" (Multi-select) with options:
  1. Ph.D. Writing & Thesis (₹20,000)
  2. PG Project & Dissertation (MCA/MBA/MSc/MA/MTech) (₹5,000)
  3. Book Writing (₹3,000) / Hard Copy Publication (₹5,000)
  4. Paper Writing & Peer-Reviewed Journal Publication (₹2,000)
  5. Academic Reports & Removal (Turnitin ₹100 / Drillbit ₹200 / Plagiarism Removal)
  6. Patent Services (UK/Germany/South Africa/India - Utility & Design) (₹15,000)
  7. Academic Certificates & Awards (Reviewer / Board / Proposals: AICTE/UGC/DST/DRDO/ISRO)
- "Agreed Total Fee (INR)" (Number, Currency: Indian Rupee)
- "Advance Received (INR)" (Number, Currency: Indian Rupee)
- "Balance Due (INR)" (Formula): prop("Agreed Total Fee (INR)") - prop("Advance Received (INR)")
- "Payment Status" (Select): Unpaid (Red), Partially Paid (Yellow), Fully Settled (Green)
- "Status" (Status): New Intake (Gray), In Progress (Blue), Client Review (Yellow), Completed (Green)
- "Assigned Team Member" (Select): Dr. Prashant Singh, Dr. Pooja Singh, Assigned Staff Lead
- "Target Deadline" (Date)
- "Step 1: Scope & Topic Confirmation" (Checkbox)
- "Step 2: Outline & Literature Gathering" (Checkbox)
- "Step 3: Draft Writing & Data Analysis" (Checkbox)
- "Step 4: Plagiarism (<10%) & Format Check" (Checkbox)
- "Step 5: Final Delivery & Archive" (Checkbox)
- "Progress Bar" (Formula, Display as Bar): (if(prop("Step 1: Scope & Topic Confirmation"), 1, 0) + if(prop("Step 2: Outline & Literature Gathering"), 1, 0) + if(prop("Step 3: Draft Writing & Data Analysis"), 1, 0) + if(prop("Step 4: Plagiarism (<10%) & Format Check"), 1, 0) + if(prop("Step 5: Final Delivery & Archive"), 1, 0)) * 0.20
- "1-Click WhatsApp Link" (Formula): "https://wa.me/91" + replaceAll(prop("Contact / WhatsApp Number"), "[^0-9]", "") + "?text=Hello%20" + encodeURIComponent(prop("Scholar Name")) + "%2C%20status%3A%20" + encodeURIComponent(prop("Status"))

2. SAMPLE DEMO ROWS TO CREATE:
Row 1: Scholar Name: "Dr. Rajesh Sharma", Contact: "8319353139", Services: "1. Ph.D. Writing & Thesis (₹20,000)", "6. Patent Services (₹15,000)", Agreed Fee: 35000, Advance: 15000, Status: "In Progress", Assigned: "Dr. Prashant Singh", Checkboxes: Step 1, Step 2, Step 3 ticked.
Row 2: Scholar Name: "Priya Verma", Contact: "8349687471", Services: "2. PG Project & Dissertation (MCA/MBA/MSc/MA/MTech) (₹5,000)", Agreed Fee: 5000, Advance: 5000, Status: "Completed", Assigned: "Dr. Pooja Singh", Checkboxes: All 5 steps ticked.
Row 3: Scholar Name: "Amit Patel", Contact: "9826012345", Services: "4. Paper Writing & Peer-Reviewed Journal Publication (₹2,000)", Agreed Fee: 2000, Advance: 1000, Status: "New Intake", Assigned: "Assigned Staff Lead", Checkboxes: None ticked.

3. DATABASE VIEWS:
- View 1: "Call Intake Desk" (Form / Simple Table showing intake fields)
- View 2: "My Work Queue" (Board view grouped by Status)
- View 3: "Executive Master Overview" (Full Table view)
```
