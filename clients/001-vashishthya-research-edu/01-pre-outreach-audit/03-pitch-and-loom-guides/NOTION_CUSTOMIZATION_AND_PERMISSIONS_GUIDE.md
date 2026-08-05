# Vashishthya Notion OS: Customization, Permissions & Google Sheets Sync Guide

**Target Operator:** Atinek Maurya  
**Goal:** Complete Operational Reference for WhatsApp Link Customization, Role Permissions, and Google Sheets Synchronization.

---

## 1. HOW TO CUSTOMIZE THE WHATSAPP MESSAGE IN NOTION

In Notion, the **1-Click WhatsApp Link** uses a Formula property that URL-encodes a message so when Dr. Prashant Singh clicks it, WhatsApp opens on mobile/desktop with a pre-filled, professional Hinglish message.

### Advanced Native Notion Formula 2.0 WhatsApp Formula (Zero JS Error):
Paste this exact formula into your Notion Formula property (Edit Property -> Edit Formula):

```javascript
if(empty(prop("Contact / WhatsApp Number")), "", if(empty(replaceAll(prop("Contact / WhatsApp Number"), "[^0-9]", "")), "", "https://wa.me/91" + replaceAll(prop("Contact / WhatsApp Number"), "[^0-9]", "") + "?text=Namaste%20" + replaceAll(if(empty(prop("Scholar Name")), "Scholar", prop("Scholar Name")), " ", "%20") + "%20Ji%2C%0A%0AGreetings%20from%20Vashishthya%20Research%20Education%20Foundation!%0A%0AYour%20academic%20order%20status%20is%20currently%3A%20" + replaceAll(if(empty(prop("Status")), "New%20Intake", prop("Status")), " ", "%20") + "%20(Balance%20Due%3A%20INR%20" + if(empty(prop("Balance Due (INR)")), "0", format(prop("Balance Due (INR)"))) + ")%0A%0AThank%20you%20for%20choosing%20Vashishthya%20Research!%0AWebsite%3A%20www.vashisthyaresearchedu.com%0AHelpline%3A%208319353139"))
```

### Simple Short Version:
```javascript
if(empty(prop("Contact / WhatsApp Number")), "", "https://wa.me/91" + replaceAll(prop("Contact / WhatsApp Number"), "[^0-9]", "") + "?text=Hello%20" + replaceAll(if(empty(prop("Scholar Name")), "Scholar", prop("Scholar Name")), " ", "%20") + "%2C%20your%20order%20status%20is%20" + replaceAll(if(empty(prop("Status")), "New%20Intake", prop("Status")), " ", "%20"))
```

### How to Modify the Text:
- The `if(empty(...))` wrappers prevent Notion from throwing errors when a new empty row is created!
- Change `"Namaste "` or `"Greetings from..."` to any custom greeting.
- To add a new line in WhatsApp messages, use `"\n"`.
- `encodeURIComponent(...)` automatically handles spaces and special characters so the link never breaks.

---

## 2. HOW TO ADD 1-CLICK WHATSAPP LINK TO ANY NEW NOTION TABLE

To add a 1-Click WhatsApp link to any future table or database in Notion:

1. Open your Notion Table -> Click `+` on the rightmost column header to add a property.
2. Select Property Type: **Formula**.
3. Name the property: `WhatsApp Link`.
4. Click **Edit Formula** and paste:
   ```javascript
   "https://wa.me/91" + replaceAll(prop("Phone Column Name"), "[^0-9]", "") + "?text=" + encodeURIComponent("Hello " + prop("Name Column Name") + ", your status is " + prop("Status"))
   ```
   *(Replace `"Phone Column Name"` and `"Name Column Name"` with your exact property names).*

---

## 3. HOW EMPLOYEES UPDATE STATUS WITHOUT GETTING FULL ACCESS (PERMISSIONS & LOCKS)

To prevent staff from modifying database schemas, changing financial formulas, or seeing private revenue columns:

### Method A: Notion Database View Lock (Zero Setup)
1. Open the **"My Work Queue"** view (Board view).
2. Click `...` in the top right corner of the database.
3. Turn ON **Lock Database View**.  
   *Result:* Staff can drag cards between status columns (`New Intake` -> `In Progress` -> `Completed`) and tick step checkboxes, but CANNOT add/delete columns or edit formulas.

### Method B: Notion Member Access Control ("Can Edit Content")
1. Click **Share** at the top right of the page.
2. Invite staff members using their email address.
3. Set permission level to **Can Edit Content** (NOT "Full Access").  
   *Result:* Staff can edit text, check off sub-tasks, and update statuses, but CANNOT alter database structure, delete database pages, or change sharing permissions.

---

## 4. HOW TO SYNC THESE FIELDS TO GOOGLE SHEETS AUTOMATICALLY

Our embedded Google Apps Script engine ([GoogleAppsScript_NotionSync.gs](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/02-notion-and-automation-specs/GoogleAppsScript_NotionSync.gs)) handles multi-column mapping automatically:

1. **How it Works:**  
   The script reads every column from Notion (Scholar Name, WhatsApp Number, Fee, Balance Due, Progress %, Status, 1-Click WhatsApp Link) and writes them to the matching columns in Google Sheets.
2. **Adding New Columns to Google Sheets:**  
   Because the script uses **Dynamic Header Mapping (`getHeaderMap`)**, whenever you add a new property in Notion, simply add a matching header name in Column 1 of your Google Sheet. The script automatically detects the position and syncs it without requiring any code updates!
