import subprocess
import json
import os
import sys

def run_gws_json(args, payload_dict):
    os.makedirs("scratch", exist_ok=True)
    temp_file = os.path.abspath("scratch/temp_gws_body.json")
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(payload_dict, f, ensure_ascii=False, indent=2)
    
    cmd = ["gws"] + args + ["--json", temp_file]
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if os.path.exists(temp_file):
        try:
            os.remove(temp_file)
        except Exception:
            pass
            
    if res.returncode != 0:
        print("ERROR STDOUT:", res.stdout, file=sys.stderr)
        print("ERROR STDERR:", res.stderr, file=sys.stderr)
        sys.exit(1)
    return json.loads(res.stdout) if res.stdout.strip() else {}

def main():
    print("Creating Google Sheet Vashishthya-01Master-OS on personal account...")
    
    # 1. Create Spreadsheet
    create_payload = {
        "properties": {
            "title": "Vashishthya-01Master-OS"
        },
        "sheets": [
            {"properties": {"title": "Scholars Intake"}},
            {"properties": {"title": "Services Catalog & Pricing"}},
            {"properties": {"title": "Monthly Revenue Ledger"}},
            {"properties": {"title": "Team Task Distribution"}}
        ]
    }
    
    sheet_res = run_gws_json(["sheets", "spreadsheets", "create"], create_payload)
    spreadsheet_id = sheet_res["spreadsheetId"]
    spreadsheet_url = sheet_res["spreadsheetUrl"]
    
    print(f"\nSUCCESS! Spreadsheet Created.")
    print(f"Spreadsheet ID: {spreadsheet_id}")
    print(f"Spreadsheet URL: {spreadsheet_url}\n")
    
    # 2. Populate Scholars Intake
    intake_data = [
        [
            "Scholar Name", "Contact / WhatsApp Number", "Email Address", "Services Required",
            "Agreed Total Fee (INR)", "Advance Received (INR)", "Balance Due (INR)", "Payment Status",
            "Status", "Assigned Team Member", "Target Deadline", "Progress Bar", "1-Click WhatsApp Link",
            "Step 1: Scope & Topic Confirmation", "Step 2: Outline & Literature Gathering",
            "Step 3: Draft Writing & Data Analysis", "Step 4: Plagiarism (<10%) & Format Check",
            "Step 5: Final Delivery & Archive"
        ],
        [
            "Dr. Rajesh Sharma", "8319353139", "rajesh.sharma@example.com",
            "1. Ph.D. Writing & Thesis (₹20,000), 6. Patent Services (₹15,000)",
            35000, 15000, "=E2-F2", "Partially Paid", "In Progress", "Dr. Prashant Singh",
            "2026-08-25", "60%", "https://wa.me/918319353139", True, True, True, False, False
        ],
        [
            "Priya Verma", "8349687471", "priya.v@example.com",
            "2. PG Project & Dissertation (MCA/MBA/MSc/MA/MTech) (₹5,000)",
            5000, 5000, "=E3-F3", "Fully Settled", "Completed", "Dr. Pooja Singh",
            "2026-08-10", "100%", "https://wa.me/918349687471", True, True, True, True, True
        ],
        [
            "Amit Patel", "9826012345", "amit.patel@example.com",
            "4. Paper Writing & Peer-Reviewed Journal Publication (₹2,000)",
            2000, 1000, "=E4-F4", "Partially Paid", "New Intake", "Assigned Staff Lead",
            "2026-08-30", "0%", "https://wa.me/919826012345", False, False, False, False, False
        ]
    ]
    
    params_intake = json.dumps({"spreadsheetId": spreadsheet_id, "range": "Scholars Intake!A1", "valueInputOption": "USER_ENTERED"})
    run_gws_json(["sheets", "spreadsheets", "values", "update", "--params", params_intake], {"values": intake_data})
    print("Populated Tab 1: Scholars Intake")
    
    # 3. Populate Services Catalog & Pricing
    catalog_data = [
        ["Service Name", "Target Audience / Degrees", "Standard Price (INR)", "Turnaround SLA", "Included Deliverables"],
        ["Ph.D. Writing & Thesis Support", "Ph.D. Scholars (All Subjects)", 20000, "15-30 Days", "Synopsis, Thesis, Turnitin Plagiarism (<10%), 2 Research Papers, 2 Conference Papers, Plagiarism Report"],
        ["PG Project & Dissertation", "MCA, MBA, MSc, MA, M.Tech", 5000, "7-15 Days", "Complete Project/Dissertation, Data Analysis, Source Code, Plagiarism Report"],
        ["Book Writing & Publication", "Academicians & Researchers", 3000, "10-20 Days", "Book Writing (₹3,000) / Hard Copy Publication with ISBN (₹5,000)"],
        ["Paper Writing & Journal Pub", "Faculty & Scholars", 2000, "5-10 Days", "Paper Writing & Peer-Reviewed International Journal Publication"],
        ["Academic Reports & Removal", "Research Scholars", 100, "Instant / 24 Hours", "Turnitin Report (₹100), Drillbit Report (₹200), Plagiarism Removal Support"],
        ["Patent Services (Pub & Grant)", "Inventors & Faculty", 15000, "15-45 Days", "UK, Germany, South Africa, India - Utility & Design Patent Filing & Grant"],
        ["Certificates & Award Support", "Faculty & Reviewers", 5000, "3-7 Days", "Reviewer / Editorial Board Member Certificates, Proposal Support (AICTE, UGC, DST, SERB, DRDO, ISRO)"]
    ]
    params_cat = json.dumps({"spreadsheetId": spreadsheet_id, "range": "Services Catalog & Pricing!A1", "valueInputOption": "USER_ENTERED"})
    run_gws_json(["sheets", "spreadsheets", "values", "update", "--params", params_cat], {"values": catalog_data})
    print("Populated Tab 2: Services Catalog & Pricing")
    
    # 4. Populate Monthly Revenue Ledger
    revenue_data = [
        ["Month", "Total Scholars Enrolled", "Gross Revenue Agreed (INR)", "Advance Collected (INR)", "Pending Balance (INR)"],
        ["August 2026", 3, 42000, 21000, "=C2-D2"]
    ]
    params_rev = json.dumps({"spreadsheetId": spreadsheet_id, "range": "Monthly Revenue Ledger!A1", "valueInputOption": "USER_ENTERED"})
    run_gws_json(["sheets", "spreadsheets", "values", "update", "--params", params_rev], {"values": revenue_data})
    print("Populated Tab 3: Monthly Revenue Ledger")
    
    # 5. Populate Team Task Distribution
    team_data = [
        ["Team Member Name", "Active Assignments", "Completed Orders", "Pending Balance Followup (INR)"],
        ["Dr. Prashant Singh", 1, 0, 20000],
        ["Dr. Pooja Singh", 0, 1, 0],
        ["Assigned Staff Lead", 1, 0, 1000]
    ]
    params_team = json.dumps({"spreadsheetId": spreadsheet_id, "range": "Team Task Distribution!A1", "valueInputOption": "USER_ENTERED"})
    run_gws_json(["sheets", "spreadsheets", "values", "update", "--params", params_team], {"values": team_data})
    print("Populated Tab 4: Team Task Distribution")
    
    print("\n========================================================")
    print("ALL TABS FULLY CREATED AND POPULATED IN YOUR PERSONAL GOOGLE ACCOUNT!")
    print(f"Spreadsheet URL: {spreadsheet_url}")
    print("========================================================\n")

if __name__ == "__main__":
    main()
