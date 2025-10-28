# 📋 Junior Level Screenshot Checklist

Quick reference for taking screenshots. Check off as you complete each one.

## 🎯 Module 1: Setup & Module Structure (4 screenshots)

- [ ] **q01-odoo-dashboard.png**
  - What: Odoo Apps menu showing available modules
  - Where: Apps menu after login
  
- [ ] **q02-module-structure.png**
  - What: VS Code file tree of om_hospital module
  - Where: VS Code Explorer panel
  
- [ ] **q03-manifest-file.png**
  - What: __manifest__.py file content
  - Where: VS Code editor (custom-addons/om_hospital/__manifest__.py)
  
- [ ] **q04-menu-ui.png**
  - What: Hospital menu with submenus expanded
  - Where: Odoo UI top menu bar

---

## 🎯 Module 2: Models & Security (4 screenshots)

- [ ] **q05-patient-form.png**
  - What: Patient form showing fields (name, age, gender, etc.)
  - Where: Hospital → Patient Details → Patients → Open any patient
  
- [ ] **q06-field-types.png**
  - What: patient.py code showing different field types
  - Where: VS Code (custom-addons/om_hospital/models/patient.py lines 10-35)
  
- [ ] **q07-access-rights.png**
  - What: ir.model.access.csv content
  - Where: VS Code (custom-addons/om_hospital/security/ir.model.access.csv)
  
- [ ] **q08-simple-model.png**
  - What: HospitalPatient class definition
  - Where: VS Code (custom-addons/om_hospital/models/patient.py lines 1-20)

---

## 🎯 Module 3: Views & Basic Operations (9 screenshots)

- [ ] **q09-tree-view.png**
  - What: Patient list view (multiple records)
  - Where: Hospital → Patient Details → Patients (list view)
  
- [ ] **q09-form-view.png**
  - What: Single patient detail form
  - Where: Hospital → Patient Details → Patients → Open record
  
- [ ] **q10-archive-button.png**
  - What: Action menu showing Archive option
  - Where: Patient form → Action dropdown
  
- [ ] **q10-archived-filter.png**
  - What: Search view with Archived filter
  - Where: Patient list → Filters dropdown
  
- [ ] **q11-default-value.png**
  - What: New patient form with Gender defaulting to Female
  - Where: Hospital → Patients → Create (new record)
  
- [ ] **q12-domain-filter.png**
  - What: Filter buttons (Male/Female)
  - Where: Patient list → Filters dropdown
  
- [ ] **q13-required-field.png**
  - What: Required field indicator (red asterisk) or validation error
  - Where: Patient form (Gender field is required)
  
- [ ] **q14-filters-groupby.png**
  - What: Search panel with filters and Group By options
  - Where: Patient list → Filters + Group By menus
  
- [ ] **q15-context-action.png**
  - What: Patient list with pre-activated Male filter and grouping
  - Where: Hospital → Patients (notice filter badge and grouping)

---

## 📊 Progress: 0/17 Complete

**Total Screenshots Needed:** 17 (2 for Q09, 2 for Q10)

Save all to: `docs/interview-questions/junior/`
