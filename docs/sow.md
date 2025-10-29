# Statement of Work (SoW)

**Project:** Development of om_hospital Odoo 15 Module  
**Prepared for:** [Client Name]  
**Prepared by:** [Your Company / Name]  
**Date:** [Insert Date]

---

## 1. Project Overview

The purpose of this project is to design and develop a custom Odoo 15 module (`om_hospital`) to support hospital operations, including patient management, doctors, departments, and appointment workflows. The module will follow Odoo best practices, with appropriate models, views, security rules, and reporting.

---

## 2. Scope of Work

### 2.1 In-Scope Features (MVP)

#### Module Setup & Configuration
- Scaffold module, configure manifests, establish repository structure
- Sequences for key records

#### Core Models
- Patient, Doctor, Department, Appointment

#### Menus & Security
- Menu hierarchy, window actions, access rights, and groups

#### Views & User Interface
- Form, Tree, and Search views with filters, group by, and domains
- Context defaults, list customizations

#### Chatter & Tracking
- Add chatter and activity tracking for core models

#### Validations & Constraints
- SQL and Python constraints for data integrity

#### Wizards
- Appointment cancellation/rescheduling

#### Reports
- QWeb patient card and appointment list

#### Email
- Basic templates and notifications

#### Demo Data & Packaging
- XML/CSV demo data for testing, CLI setup, deployment scripts

#### Documentation
- README, usage notes, screenshots

### 2.2 Optional Features (Extras, Subject to Client Approval)

- External API (token authentication, CRUD endpoints)
- Calendar view for appointments
- Smart/stat buttons and small dashboards
- Barcode/QR integration in reports
- WhatsApp or external messaging integration
- Fine-grained permissions and advanced security rules

### 2.3 Out of Scope

- Integration with accounting, stock, or HR modules
- Multi-company or multi-language setup
- High-availability or Kubernetes deployment

---

## 3. Deliverables

1. `om_hospital` Odoo 15 custom module (source code)
2. Demo dataset for functional review
3. At least two sample QWeb reports
4. User documentation and installation guide
5. Technical documentation (model and method summary)

---

## 4. Project Timeline

### 4.1 Estimated Effort

- **MVP Scope:** ~95 hours
- **MVP + Extras:** ~134 hours

### 4.2 Suggested Schedule (assuming full-time development)

- **Milestone 1 – Core Models & Security (2 weeks):** CRUD entities, sequences, menus, ACLs
- **Milestone 2 – Views & Workflows (2 weeks):** Form/tree/search, chatter, constraints, wizards
- **Milestone 3 – Reports & Emails (1 week):** QWeb, templates, validation
- **Milestone 4 – QA, Packaging, Documentation (1 week)**
- **Milestone 5 – Optional Features (2 weeks, if approved)**

**Total:** 6 weeks for MVP, up to 8 weeks with extras

---

## 5. Pricing & Payment Terms

### 5.1 Estimated Project Cost

**MVP (95 hours):**
- €3,800 (≈1.52M HUF) at €40/hour mid-rate

**MVP + Extras (134 hours):**
- €5,360 (≈2.14M HUF)

**Range:** €35–€60/hour depending on negotiated rate

### 5.2 Payment Schedule

1. **30%** upfront upon contract signing
2. **40%** after completion of Milestone 2 (functional prototype)
3. **30%** upon delivery of final module, documentation, and acceptance

---

## 6. Acceptance Criteria

- Module installs cleanly in Odoo 15 CE
- Core models, views, security rules, and workflows function as described
- Reports generate correctly with sample data
- Documentation delivered in English
- Client sign-off on milestone deliverables

---

## 7. Assumptions

- Single Odoo 15 CE instance
- English language only
- Standard hosting (Ubuntu + Nginx + PostgreSQL)
- Client provides timely feedback within 3 business days per milestone

---

## 8. Confidentiality & IP

- All code delivered under client's ownership upon final payment
- Developer may reuse generic technical know-how, but no client-specific IP

---

## 9. Signatures

**Client Representative:** ___________________________  
**Date:** __________________

**Developer Representative:** ________________________  
**Date:** __________________