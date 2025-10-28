# 📸 Screenshot Guide for Odoo Interview Questions

This guide helps you take screenshots to populate the placeholders in the README.md file.

## 🚀 Quick Start

1. **Start Odoo:**
   ```bash
   cd /home/ferko/Documents/docker-odoo-dev
   docker compose restart web
   ```

2. **Access Odoo:**
   - URL: `http://localhost:8069`
   - Email: `49i3s92fy@mozmail.com`
   - Password: `admin`

3. **Enable Developer Mode:**
   - Settings → Activate Developer Mode
   - Or append `?debug=1` to URL

---

## 🟢 Junior Level Screenshots (15 screenshots needed)

### Module 1: Setup & Module Structure

#### Q01: Odoo Main Dashboard
**File:** `junior/q01-odoo-dashboard.png`
**Steps:**
1. Login to Odoo
2. Click on "Apps" menu (top-left grid icon)
3. Screenshot showing the apps list (Sales, CRM, Inventory, Accounting, etc.)
**What to capture:** Full screen showing multiple Odoo modules/apps

---

#### Q02: Module Structure
**File:** `junior/q02-module-structure.png`
**Steps:**
1. Open VS Code
2. Navigate to `custom-addons/om_hospital/`
3. Expand all folders to show structure
**What to capture:** VS Code file explorer showing:
```
om_hospital/
├── __init__.py
├── __manifest__.py
├── models/
├── views/
├── security/
├── data/
├── wizard/
└── static/
```

---

#### Q03: Manifest File
**File:** `junior/q03-manifest-file.png`
**Steps:**
1. Open `custom-addons/om_hospital/__manifest__.py` in VS Code
2. Show the full content
**What to capture:** Code editor showing manifest file content (lines 1-35)

---

#### Q04: Menu in Odoo UI
**File:** `junior/q04-menu-ui.png`
**Steps:**
1. Login to Odoo
2. Click on "Hospital" menu
3. Show the dropdown with submenus (Patient Details, Appointments, Configuration)
**What to capture:** Menu hierarchy showing Hospital → Patient Details → Patients

---

### Module 2: Models & Security

#### Q05: Patient Form with Fields
**File:** `junior/q05-patient-form.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Open any patient record or create new
3. Show form view with fields
**What to capture:** Patient form showing Name, Date of Birth, Age, Gender, Reference fields

---

#### Q06: Field Types in Code
**File:** `junior/q06-field-types.png`
**Steps:**
1. Open `custom-addons/om_hospital/models/patient.py` in VS Code
2. Scroll to field definitions (lines 10-35)
**What to capture:** Code showing different field types (Char, Integer, Date, Boolean, Selection, Image, Many2one, Many2many)

---

#### Q07: Access Rights CSV
**File:** `junior/q07-access-rights.png`
**Steps:**
1. Open `custom-addons/om_hospital/security/ir.model.access.csv` in VS Code
**What to capture:** CSV file showing access control entries

---

#### Q08: Simple Model Example
**File:** `junior/q08-simple-model.png`
**Steps:**
1. Open `custom-addons/om_hospital/models/patient.py` in VS Code
2. Show lines 1-20 (class definition with basic fields)
**What to capture:** Code showing class HospitalPatient with _name, _description, and basic fields

---

### Module 3: Views & Basic Operations

#### Q09: Tree View - Patient List
**File:** `junior/q09-tree-view.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Make sure you're in List view (tree view)
3. Show multiple patient records
**What to capture:** List/tree view showing columns: Name, Age, Gender, Reference, Tags

---

#### Q09: Form View - Patient Details
**File:** `junior/q09-form-view.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Click on any patient to open form view
**What to capture:** Form view showing grouped fields, image, and detailed information

---

#### Q10: Archive Button in UI
**File:** `junior/q10-archive-button.png`
**Steps:**
1. Open a patient form
2. Show the Action menu → Archive option
**What to capture:** Dropdown menu showing "Archive" action

---

#### Q10: Archived Filter
**File:** `junior/q10-archived-filter.png`
**Steps:**
1. In patient list view
2. Click Filters → Show "Archived" filter option
**What to capture:** Search panel with "Archived" filter visible

---

#### Q11: Default Gender Field
**File:** `junior/q11-default-value.png`
**Steps:**
1. Hospital → Patient Details → Patients → Create
2. Show new patient form with Gender field defaulting to "Female"
**What to capture:** New patient form showing Gender = "Female" by default

---

#### Q12: Domain Filter in Search View
**File:** `junior/q12-domain-filter.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Click Filters dropdown
3. Show Male/Female filter buttons
**What to capture:** Filter dropdown showing "Male" and "Female" filter options

---

#### Q13: Required Field Validation
**File:** `junior/q13-required-field.png`
**Steps:**
1. Create new patient
2. Leave Gender field empty (if possible, or highlight the red asterisk)
3. Try to save → show validation error
**What to capture:** Either the red asterisk on Gender field label OR validation error message

---

#### Q14: Search Filters and Group By
**File:** `junior/q14-filters-groupby.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Open Filters and Group By menus
**What to capture:** Full search panel showing:
- Search field
- Filter options (Male, Female, Archived)
- Group By → Gender option
- Search panel on left (if visible)

---

#### Q15: Context in Action
**File:** `junior/q15-context-action.png`
**Steps:**
1. Hospital → Patient Details → Patients
2. Notice that "Male" filter is pre-activated (from context in action)
3. Records are grouped by Gender
**What to capture:** Patient list with Male filter badge active and records grouped by gender

---

## 💡 Screenshot Tips

### Best Practices:
- **Resolution:** Take high-quality screenshots (at least 1280px width)
- **Clean UI:** Close unnecessary browser tabs/windows
- **Focus:** Crop to relevant area (no need for entire desktop)
- **File Format:** PNG preferred (better quality for UI screenshots)
- **File Size:** Keep under 500KB per screenshot (compress if needed)

### Tools:
- **Linux:** `gnome-screenshot` or `flameshot`
- **Command:**
  ```bash
  # Full screen
  gnome-screenshot -f junior/q01-odoo-dashboard.png
  
  # Interactive selection
  gnome-screenshot -a -f junior/q02-module-structure.png
  ```

### Naming Convention:
- Format: `q[NUMBER]-[description].png`
- Example: `q05-patient-form.png`
- Keep names lowercase with hyphens

---

## ✅ Progress Tracker

Mark completed screenshots:

- [ ] q01-odoo-dashboard.png
- [ ] q02-module-structure.png
- [ ] q03-manifest-file.png
- [ ] q04-menu-ui.png
- [ ] q05-patient-form.png
- [ ] q06-field-types.png
- [ ] q07-access-rights.png
- [ ] q08-simple-model.png
- [ ] q09-tree-view.png
- [ ] q09-form-view.png
- [ ] q10-archive-button.png
- [ ] q10-archived-filter.png
- [ ] q11-default-value.png
- [ ] q12-domain-filter.png
- [ ] q13-required-field.png
- [ ] q14-filters-groupby.png
- [ ] q15-context-action.png

---

## 🎯 After Screenshots

1. Save all images to `docs/interview-questions/junior/`
2. Verify filenames match the placeholders in README.md
3. Check image quality and readability
4. Commit to git:
   ```bash
   git add docs/
   git commit -m "Add Junior level interview question screenshots"
   ```

---

## 🔄 Next Steps

After completing Junior screenshots:
- Review the README to ensure images display correctly
- Proceed to Mid-level questions (16-50) following same pattern
- Then Expert-level questions (51-113)
