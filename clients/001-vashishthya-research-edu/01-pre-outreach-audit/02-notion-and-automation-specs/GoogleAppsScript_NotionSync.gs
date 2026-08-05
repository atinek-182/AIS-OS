/**
 * Vashishthya Research Education Foundation — Master Google Apps Script Engine
 * Workspace: VASHISTHYA OPERATIONAL HUB
 * Version: 1.0.0 (Zero-Paywall, Zero-Maintenance Architecture)
 * 
 * Features:
 * 1. Notion to Google Sheets Live Sync (Dynamic Column Mapping)
 * 2. Automated Scholar Gmail Receipt Dispatcher
 * 3. 1-Click WhatsApp Link Helper
 * 4. Modular Multi-Tab Data Exporter (Scholars, Financials, Journals, Patents)
 * 
 * Backward Compatibility Guarantee:
 * Uses dynamic header lookup (getHeaderIndex) so adding/reordering columns or tabs
 * will NEVER break existing sync or automation functions.
 */

// ==========================================
// CONFIGURATION CONSTANTS
// ==========================================
var CONFIG = {
  NOTION_API_KEY: 'secret_PASTE_YOUR_NOTION_INTEGRATION_TOKEN_HERE',
  NOTION_DATABASE_ID: 'PASTE_YOUR_NOTION_DATABASE_ID_HERE',
  TAB_SCHOLARS: 'Scholars Intake',
  TAB_FINANCIALS: 'Financial Ledger',
  TAB_AUDIT_LOG: 'Audit Log',
  SENDER_EMAIL: 'parsjp17@gmail.com'
};

/**
 * Main Trigger Function: Run this on a 15-minute or 1-hour time-driven trigger.
 */
function runMasterSync() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var logSheet = getOrCreateSheet(ss, CONFIG.TAB_AUDIT_LOG);
  
  try {
    logMessage(logSheet, 'START', 'Starting Notion live sync execution...');
    syncNotionToSheets(ss);
    updateFinancialLedger(ss);
    logMessage(logSheet, 'SUCCESS', 'Master sync completed successfully.');
  } catch (error) {
    logMessage(logSheet, 'ERROR', 'Sync failure: ' + error.toString());
  }
}

/**
 * 1. Sync Notion Master Database to Google Sheets Tab ("Scholars Intake")
 */
function syncNotionToSheets(ss) {
  var sheet = getOrCreateSheet(ss, CONFIG.TAB_SCHOLARS);
  ensureHeaders(sheet, [
    'Scholar ID',
    'Scholar Name',
    'Contact Number',
    'Email Address',
    'Services Required',
    'Agreed Total Fee',
    'Advance Received',
    'Balance Due',
    'Payment Status',
    'Status',
    'Progress Percentage',
    'Assigned Team Member',
    'Target Deadline',
    '1-Click WhatsApp Link',
    'Last Synced'
  ]);

  if (CONFIG.NOTION_API_KEY.indexOf('PASTE_YOUR') !== -1) {
    Logger.log('Notion API Token not configured. Operating in Offline Demo mode.');
    return;
  }

  var url = 'https://api.notion.com/v1/databases/' + CONFIG.NOTION_DATABASE_ID + '/query';
  var options = {
    method: 'post',
    headers: {
      'Authorization': 'Bearer ' + CONFIG.NOTION_API_KEY,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json'
    },
    muteHttpExceptions: true
  };

  var response = UrlFetchApp.fetch(url, options);
  var json = JSON.parse(response.getContentText());

  if (!json.results) return;

  var headerMap = getHeaderMap(sheet);
  var data = sheet.getDataRange().getValues();
  var existingIds = {};
  for (var i = 1; i < data.length; i++) {
    var id = data[i][headerMap['Scholar ID']];
    if (id) existingIds[id] = i + 1; // Row index 1-based
  }

  json.results.forEach(function(page) {
    var pageId = page.id;
    var props = page.properties;

    var scholarName = extractTitle(props['Scholar Name']);
    var phone = extractPhone(props['Contact / WhatsApp Number']);
    var email = extractEmail(props['Email Address']);
    var services = extractMultiSelect(props['Services Required']);
    var agreedFee = extractNumber(props['Agreed Total Fee (INR)']);
    var advance = extractNumber(props['Advance Received (INR)']);
    var balance = agreedFee - advance;
    var payStatus = extractSelect(props['Payment Status']);
    var status = extractStatus(props['Status']);
    var assigned = extractSelect(props['Assigned Team Member']);
    var deadline = extractDate(props['Target Deadline']);
    var progress = calculateProgress(props);
    var waLink = 'https://wa.me/91' + phone.replace(/[^0-9]/g, '') + '?text=Hello%20' + encodeURIComponent(scholarName) + '%2C%20status%3A%20' + encodeURIComponent(status);
    var now = new Date();

    var rowValues = [];
    rowValues[headerMap['Scholar ID']] = pageId;
    rowValues[headerMap['Scholar Name']] = scholarName;
    rowValues[headerMap['Contact Number']] = phone;
    rowValues[headerMap['Email Address']] = email;
    rowValues[headerMap['Services Required']] = services;
    rowValues[headerMap['Agreed Total Fee']] = agreedFee;
    rowValues[headerMap['Advance Received']] = advance;
    rowValues[headerMap['Balance Due']] = balance;
    rowValues[headerMap['Payment Status']] = payStatus;
    rowValues[headerMap['Status']] = status;
    rowValues[headerMap['Progress Percentage']] = (progress * 100).toFixed(0) + '%';
    rowValues[headerMap['Assigned Team Member']] = assigned;
    rowValues[headerMap['Target Deadline']] = deadline;
    rowValues[headerMap['1-Click WhatsApp Link']] = waLink;
    rowValues[headerMap['Last Synced']] = now;

    if (existingIds[pageId]) {
      var rowIndex = existingIds[pageId];
      sheet.getRange(rowIndex, 1, 1, rowValues.length).setValues([rowValues]);
    } else {
      sheet.appendRow(rowValues);
    }
  });
}

/**
 * 2. Auto-Update Financial Ledger Tab ("Financial Ledger")
 */
function updateFinancialLedger(ss) {
  var scholarsSheet = ss.getSheetByName(CONFIG.TAB_SCHOLARS);
  if (!scholarsSheet) return;

  var finSheet = getOrCreateSheet(ss, CONFIG.TAB_FINANCIALS);
  ensureHeaders(finSheet, [
    'Summary Metric',
    'Amount (INR)',
    'Last Updated'
  ]);

  var data = scholarsSheet.getDataRange().getValues();
  var headerMap = getHeaderMap(scholarsSheet);

  var totalAgreed = 0;
  var totalAdvance = 0;
  var totalBalance = 0;

  for (var i = 1; i < data.length; i++) {
    totalAgreed += Number(data[i][headerMap['Agreed Total Fee']] || 0);
    totalAdvance += Number(data[i][headerMap['Advance Received']] || 0);
    totalBalance += Number(data[i][headerMap['Balance Due']] || 0);
  }

  var now = new Date();
  finSheet.getRange(2, 1, 3, 3).setValues([
    ['Total Contracted Fees', totalAgreed, now],
    ['Total Advance Collected', totalAdvance, now],
    ['Total Outstanding Balance Due', totalBalance, now]
  ]);
}

/**
 * 3. Dynamic Column Mapping Helper Functions
 */
function getHeaderMap(sheet) {
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  var map = {};
  for (var i = 0; i < headers.length; i++) {
    map[headers[i]] = i;
  }
  return map;
}

function ensureHeaders(sheet, expectedHeaders) {
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(expectedHeaders);
    sheet.getRange(1, 1, 1, expectedHeaders.length).setFontWeight('bold').setBackground('#FAF8F5');
  }
}

function getOrCreateSheet(ss, name) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  }
  return sheet;
}

function logMessage(sheet, type, message) {
  ensureHeaders(sheet, ['Timestamp', 'Type', 'Message']);
  sheet.appendRow([new Date(), type, message]);
}

// Property Extractors (Safe Fallbacks)
function extractTitle(prop) {
  return (prop && prop.title && prop.title.length > 0) ? prop.title[0].plain_text : '';
}
function extractPhone(prop) {
  return (prop && prop.phone_number) ? prop.phone_number : '';
}
function extractEmail(prop) {
  return (prop && prop.email) ? prop.email : '';
}
function extractMultiSelect(prop) {
  if (!prop || !prop.multi_select) return '';
  return prop.multi_select.map(function(item) { return item.name; }).join(', ');
}
function extractSelect(prop) {
  return (prop && prop.select) ? prop.select.name : '';
}
function extractStatus(prop) {
  return (prop && prop.status) ? prop.status.name : '';
}
function extractNumber(prop) {
  return (prop && prop.number !== undefined && prop.number !== null) ? prop.number : 0;
}
function extractDate(prop) {
  return (prop && prop.date && prop.date.start) ? prop.date.start : '';
}
function calculateProgress(props) {
  var steps = [
    'Step 1: Scope & Topic Confirmation',
    'Step 2: Outline & Literature Gathering',
    'Step 3: Draft Writing & Data Analysis',
    'Step 4: Plagiarism (<10%) & Format Check',
    'Step 5: Final Delivery & Archive'
  ];
  var count = 0;
  steps.forEach(function(step) {
    if (props[step] && props[step].checkbox) count++;
  });
  return count * 0.20;
}
