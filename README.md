# Overview
This project template facilitates Odoo development using Docker, specifically configured for VSCode IDE. It includes setup instructions and tips for effective debugging using the Odoo IDE extension.

## Setup development environment
### Prerequisites

**Clone the Project**
```bash
git clone https://github.com/teguhteja/docker-odoo-dev.git -b 15
.gitignore
.dockerignore
pyenv local 3.9.18 # .python-version
# direnv, echo 'eval "$(direnv hook bash)"' >> ~/.zshrc
echo 'layout pyenv 3.9.18' > .envrc
direnv allow
source .direnv/python-3.9.18/bin/activate
GH action https://github.com/python-semantic-release/python-semantic-release
GH readme.md https://github.com/othneildrew/Best-README-Template

```

**VSCode with the following extensions**
   - [Odoo IDE](https://github.com/odoo-ide/vscode-odoo)
   - Owl Vision
   - Odoo Shortcuts


**Python static analysis tool : Odoo Stubs**
```bash
.gitignore odoo-stubs-15
git clone https://github.com/odoo-ide/odoo-stubs.git -b 15.0 odoo-stubs-15
```
pyrightconfig.json
```bash
{
    "stubPath": "./odoo-stubs15/",
    "extraPaths": [
        "./custom-addons/",
    ]
}
```

**Build Docker Image w/ [pydevd-odoo debugger](https://github.com/odoo-ide/pydevd-odoo)**
   ```bash
   add pydevd-odoo to requirements.txt 
   in Dockerfile
   - change image source and version based on which platform you are developing
      arm macos -->FROM wbms/odoo-15.0
      arm macos -->FROM arm64v8/odoo:15.0
      x86 --> FROM odoo:15
   docker build --platform linux/arm64/v8,linux/amd64 -t odoodev:15 .
   ```

** Odoo conf **
   ```bash
   # Session persistence configuration
   session_dir = /var/lib/odoo/sessions
   server_wide_modules = base,web,om_hospital
   ```

**Start Docker Compose**

in docker-compose.yml
   ```bash   
   - change version related parameters 
   --> platform: linux/amd64
   # update om_hospital module each time web service is restarted
   entrypoint: /usr/bin/python3 -m debugpy --listen 0.0.0.0:8888 /usr/bin/odoo -c /etc/odoo/odoo.conf -d odoo -i base -u om_hospital
   - o15-sessions:/var/lib/odoo/sessions
   
   docker compose up -d
   docker compose restart web
   docker logs -f --tail 50 o15 2>&1 | ccze -m ansi
   docker exec -e "TERM=xterm-256color" -it o15 odoo -c /etc/odoo/odoo.conf -d odoo -u om_hospital --stop-after-init
   ```

**Add Your Addons**
   - Create a directory for your custom addons:
     ```bash
     # touch .env
     mkdir custom-addons
     docker compose restart odoo-dev
     ```

**Debugging**
   - Set breakpoints in your source code within VSCode.
   - Ensure the debugger is configured to debug external code (`"justMyCode": false` in .vscode/launch.json).
   - Access the Odoo source code from the container:
     ```bash
     ./docker-cp-odoo.sh
     ```
   - Add breakpoints in the Odoo source code.
   - Run the debugger process to start debugging.


### Troubleshooting Tips

**Copying misc.py in odoodev**

   - If backup failures occur with Docker images, modify `misc.py` to resolve issues.

**Debugging Odoo Source Code**

   - Modify `"justMyCode": false` in `launch.json`, 
   -download the Odoo folder from the container using `docker-cp-odoo.sh`, uncomment this line in docker-compose.yml
   - ./odoo:/usr/lib/python3/dist-packages/odoo
   - restart stack or docker compose
   - add breakpoints, and start the debugger process .

---


# Odoo 15 Development Learning Journey

This repository documents my progress and learnings from the [Odoo 15 Development Tutorials YouTube Playlist](https://www.youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU).

# 📚 Odoo 15 Development Study Plan

Tick each video off as you progress.  

If you dedicate **~1 hour per day**, the full program will take roughly:

- **6 weeks (about 42 days)** total  
- Allowing for 1–2 review/catch-up days each week, expect **7–8 weeks** realistically  

This means that with just a small daily investment, you can cover the entire Odoo 15 development track in under **two months**, while still leaving breathing room for rewatching tough topics (ORM overrides, reporting, APIs).

---

### **Module 1: Introduction to Odoo Development**
- [ x] Setting up Odoo with PyCharm  
- [ x] Configure custom addons path  
- [ x] Create a new module  
- [ x] Add an icon for module  
- [ x] Define menus and actions basics  
- **Videos:** 1–6  
- ⏱️ **Estimated Time:** ~1.5 hours  

---

### **Module 2: Models & Security Basics**
- [x ] Define models and database tables  
- [x ] Link menus and actions  
- [x ] Set access rights and icons  
- **Videos:** 7–8  
- ⏱️ **Estimated Time:** ~1 hour  

---

### **Module 3: Views Essentials**
- [x ] Create form, tree, and search views  
- [x ] Add filters and group by options : male, female, etecera, gender
- [x ] Apply domains : female patients
- [x ] Archive / unarchive records  
- [x ] Use default values and context : female patients
- **Videos:** 9–16  
- ⏱️ **Estimated Time:** ~3 hours  

---

### **Module 4: Communication & Tracking**
- [x ] Add chatter to forms  
- [x ] Enable field tracking  
- [x ] Add search panel  
- **Videos:** 17–19  
- ⏱️ **Estimated Time:** ~1 hour  

---

### **Module 5: Fields Deep Dive**
- [x ] Add Many2one fields  
- [x ] Use date & datetime fields  
- [x ] Define related and computed fields  
- [x ] Handle onchange functions  
- [x ] Configure rec name  
- [x ] Add notebooks, HTML fields, and images  
- **Videos:** 20–28  
- ⏱️ **Estimated Time:** ~3.5 hours  

### **Module 6: Widgets & Decorations**
- [x ] Priority widget & statusbars  
- [x ] Buttons, help messages, confirmation dialogs  
- [x ] Rainbow effects, badges, colors, avatars  
- [x ] Dynamic tree views, resizable/collaborative HTML fields  
- [x ] Boolean toggles, color pickers, Many2many widget options  
- [x ] Advanced widgets (activity, radio, selection, handle, progress, calendar, etc.)  
- **Videos:** 29–43  
- ⏱️ **Estimated Time:** ~4 hours  

---

### **Module 7: Workflows & Wizards**
- [x ] Control statusbar using buttons  
- [x ] Enable hotkeys  
- [x ] Work with One2many and Many2many fields  
- [x ] Create and use transient models & wizards  
- [x ] Load data from XML & CSV  
- **Videos:** 44–66  
- ⏱️ **Estimated Time:** ~4.5 hours  

--- 

### **Module 8: Inheritance & ORM**
- [x ] Create module with scaffold command
```bash
docker exec -it o15 /usr/bin/odoo scaffold om_odoo_inheritance /mnt/custom-addons
this was suck, gave a sale.order model not found error
suggesting create new custom module and add the code there by manualy
```
- [x ] Inherit models, fields, functions (_inherit in py model , xpath in views) 
- [x ] Override create/write/unlink methods  
- [x ] Work with sequences, default get, name get  
- [x] Explore ORM methods (create, browse, search, etc.)  
   - [x ] How To Inherit Model In Odoo || Odoo Inheritance || Odoo 15 Tutorials || Odoo 15 Development	6:08	12. Inheritance & Method Overrides	70
   - [x ] How To Inherit And Add Field To A Model In Odoo || Odoo Inheritance || Odoo 15 Tutorials	21:05	12. Inheritance & Method Overrides	71
   - [x ] How To Inherit A Function In Odoo || Odoo Inheritance || Odoo 15 Tutorials || Odoo 15 Development	8:33	12. Inheritance & Method Overrides	72
   - [x ] How To Override Create Method In Odoo || Odoo 15 Tutorial || Odoo ORM Methods	8:57	12. Inheritance & Method Overrides	73
   - [x ] How To Override Write Method In Odoo || Inherit Write Function In Odoo || Odoo ORM Methods	9:13	12. Inheritance & Method Overrides	75
- **Videos:** 67–75  
- ⏱️ **Estimated Time:** ~5 hours  

---

WEEK
### **Module 9: Advanced Features**
- [x ] New Odoo playground model tutorials
   - [x ] 76. Menu And SubMenu Without Specifying Parent In Odoo || Odoo Tips and Tricks || Odoo Advanced
   - [x ] 77. Target Inline In Odoo || Inline Actions In Odoo || Target In Odoo Actions || Odoo Window Action
- [ ] Odoo Environment | Odoo Self | self.env in Odoo || Odoo
- [x ] Raise validation errors  
   - How To Raise Validation Error In Odoo || Odoo Validation || Validation Error In Odoo,6:25,"9. Validation, Constraints & Domains",89
- [x ] Apply domains on fields  
   - Apply Domain For Fields In Odoo || Odoo Domain Concept || Odoo Field Domain || Odoo 15 Tutorials,13:35,"9. Validation, Constraints & Domains",90
- [x ] Add SQL & Python constraints  
   - Sql Constraints In Odoo || Constrains In Odoo || Odoo 15 Field Validations,15:06,"9. Validation, Constraints & Domains",91
   - Python Constrains In Odoo || Constrains Decorator In Odoo || Model Constrains In Odoo,7:15,"9. Validation, Constraints & Domains",92
- [x ] Copy function overrides  
   - 84. Copy Function In Odoo ｜ Copy Attribute In Odoo ｜ Odoo Copy ORM Method
- [ ] Configure stored/unstored computed fields  
   - Stored Compute Field In Odoo And Its Dependency || Re computation Of Stored Compute Field,12:53,17. Misc & Unsorted,95
   - Searchable Non Stored Compute Field In Odoo | How To Define Search Function For Field In Odoo,14:22,6. Fields: Basics & Relational,109
- [ ] Set inverse functions  
   - How To Set Inverse Function For Computed Field In Odoo || Editable Compute Field In Odoo,12:26,6. Fields: Basics & Relational,108
- [ ] Use ondelete policies & conditional fields  
   - Ondelete Policy In Odoo | Ondelete Restrict and Ondelete Cascade In Odoo | Odoo Ondelete Policy,7:57,"9. Validation, Constraints & Domains",97
   - How To Hide Fields Based On Conditions In Odoo || Make Field Invisible Based On Other Fields,10:33,"9. Validation, Constraints & Domains",98
   - How To Make Field Readonly Based On Condition In Odoo || Conditional Readonly Fields In Odoo,5:48,"9. Validation, Constraints & Domains",99
   - How To Make Field Required Based On Conditions In Odoo || Conditional Required Fields In Odoo,8:01,"9. Validation, Constraints & Domains",100
   - Label Attribute In Odoo | Class oe_edit_only |  Label For Fields | Edit Only Class In Odoo,4:17,"9. Validation, Constraints & Domains",101
   - Ondelete Decorator In Odoo || Execute Codes On Deleting a Record In Odoo || Decorators in Odoo,5:27,"9. Validation, Constraints & Domains",104
- **Videos:** 76–83, 84–85, 86–96, 97, 98–100
- ⏱️ **Estimated Time:** ~4 hours  

---

### **Module 10: Reporting & Integrations**
- [ ] Generate QWeb, PDF, and Excel reports  
   - [ ] Customize  PDF Reports From User Interface In Odoo	16:25	13. Reporting (QWeb, PDF/Excel)	138
   - [ ] How To Add New Field To Sale Report Model In Odoo || Inherit Database View In Odoo	11:54	13. Reporting (QWeb, PDF/Excel)	174
   - [ ] Create PDF And Excel Reports In Odoo 15 || Odoo 15 Excel Reporting | Odoo 15 PDF Reports	21:20	13. Reporting (QWeb, PDF/Excel)	182
   - [ ] How To Add Line Number In Odoo Qweb Report | Line Number Inside For Loop	9:03	13. Reporting (QWeb, PDF/Excel)	184
   - [ ] How To Add Barcode And QR Code In Odoo PDF Reports	10:50	13. Reporting (QWeb, PDF/Excel)	185
- [ ] Add line numbers, barcodes, and QR codes  
- [ ] Work with external API & XMLRPC  
   - [ ] Odoo Whatsapp Integration || Odoo Whatsapp Connector || Redirect To Whatsapp From Odoo	17:11	14. External APIs & Integrations	137
   - [ ] How To Pass New Field Value From Sale Order To Invoice In Odoo	10:06	14. External APIs & Integrations	149
   - [ ] How To Get Code From Postman Application || Postman Code Generator	4:25	14. External APIs & Integrations	158
   - [ ] Odoo External API | Authentication From External Application | Odoo External API Logging in	11:19	14. External APIs & Integrations	175
   - [ ] Odoo External API: Search And Read From Odoo Database	14:02	14. External APIs & Integrations	176
   - [ ] Odoo XMLRPC: Search Read Method To Read From Database	5:06	14. External APIs & Integrations	177
   - [ ] Create Record In Odoo From External Applications | Odoo External API	5:47	14. External APIs & Integrations	178
   - [ ] Write Into Odoo Database From External Application || Odoo External API	6:45	14. External APIs & Integrations	179
   - [ ] How To Delete Records From Odoo Database Using External API	5:18	14. External APIs & Integrations	180

- [ ] Use Postman integration  
- [ ] Implement WhatsApp connector  
- **Videos:** 101–115  
- ⏱️ **Estimated Time:** ~5 hours  

---

DISMISSED

### **Module 11: Deployment & Debugging**
78 How To Run Odoo From Terminal | Odoo Command Line Options | Odoo CLI | How To Run Odoo Using Command
79 How To Generate Odoo Configuration File From Terminal || Odoo Command Line Interface || Odoo CLI
80 How To Install Module From Terminal In Odoo || Odoo Command Line Interface || Odoo CLI
81 Error no 98 Address Already In Use Error Odoo | Reason & Solution | Fix Address already In Use Error
82 How To Upgrade A Module From Odoo CLI || Upgrade Module From Terminal In Odoo || Odoo Command Line
83 How To Create Database From Terminal Odoo CLI || Odoo Command Line Interface || Odoo CLI Parameters
- [ ] Run Odoo from CLI  
- [ ] Configure Odoo server and workers  
- [ ] Upgrade modules from CLI  
- [ ] Handle common errors (compute fails, port in use, missing invoice values, etc.)  
- [ ] Debugging and troubleshooting tips  
- **Videos:** 116–end  
- ⏱️ **Estimated Time:** ~3 hours  

---

✅ By the end, you’ll have a **full-circle Odoo dev foundation**: from setup → models/views → widgets → workflows → reporting → APIs → deployment.

---

## 📂 Resources

- 📺 [YouTube Playlist](https://www.youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU)
- 📖 [Odoo 15 Official Docs](https://www.odoo.com/documentation/15.0/)
- 🛠️ [Odoo Developer Reference](https://www.odoo.com/documentation/15.0/developer.html)

---

## ✅ Conclusion

This structured journey through the Odoo 15 framework provided hands-on development skills aligned with ERP customization, security, and deployment. 

As a DevOps Python developer, this knowledge bridges backend automation with ERP system architecture — enabling contributions to business operations at scale.


## Playlist Comparison (15 → 16 → 17/18)

| Topic                                    | Odoo 15              | Odoo 16                                   | Odoo 17/18                      | Action                                             |
| ---------------------------------------- | -------------------- | ----------------------------------------- | ------------------------------- | -------------------------------------------------- |
| Environment setup (IDE, addons path, DB) | Covered              | Covered                                   | Covered                         | **Skip** – identical                               |
| Module creation & manifest               | Covered              | Covered                                   | Covered                         | **Skip**, just check new manifest keys per version |
| ORM: models & fields                     | Covered              | Covered                                   | Covered                         | **Skip** – same ORM core                           |
| Computed fields, `@api.depends`          | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Onchange methods                         | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Security (groups, rules, ACLs)           | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Views (form, tree, kanban)               | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| QWeb reports                             | Covered              | Covered                                   | Covered                         | **Skip**, small styling diffs only                 |
| Wizards                                  | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Scheduled actions / Cron                 | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Website basics (controllers, templates)  | Covered              | **Revamped website builder**              | Covered                         | **Focus** from 16 onward                           |
| Controllers (routes, JSON)               | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| JavaScript / assets                      | Covered (classic JS) | **OWL adoption**                          | **OWL 2, more frontend in JS**  | **Focus** in 16+, esp. 17/18                       |
| API integrations                         | Covered              | Covered                                   | Covered                         | **Skip**                                           |
| Accounting                               | Covered              | **Changed fields, reconciliation widget** | **Further improvements**        | **Focus** from 16 onward                           |
| MRP & Manufacturing                      | Minor                | **Revamped**                              | **Expanded again**              | **Focus** if you need MRP                          |
| New modules                              | N/A                  | Knowledge app introduced                  | Spreadsheets, Knowledge matured | **Focus if relevant**                              |

### 🔑 Key Differences Across Versions

- Odoo 16: Big performance revamp, new Knowledge app, website builder changes, OWL v1 in frontend. Accounting reworked.
- Odoo 17: UX polish (menus, search bar), website + eCommerce fully unified, OWL 2 in web client.
- Odoo 18 (early dev): Strengthening the OWL framework, refining accounting & inventory, more AI-assisted features.

### 🎯 Study Efficiency

Skip repeating basics: module creation, ORM, views, security, reports, wizards, cron. Same from 15 → 18.

Focus zones:

- Frontend evolution (classic JS → OWL v1 → OWL v2).
- Website/eCommerce (rebuilt in 16, unified in 17).
- Accounting/MRP (major differences each release).
- New modules (Knowledge, Spreadsheet, AI helpers).

## 🚀 Odoo Developer Fast-Track (15 → 16 → 17/18)

✅ Already Safe in Your Brain (Skip in 16/17/18)

- Environment setup (IDE, addons path, DB)
- Module creation & manifest basics (just glance at manifest changelog)
- ORM fundamentals (models, fields, computed, onchange)
- Security (groups, ACLs, rules)
- Views (form, tree, kanban)
- QWeb reports basics
- Wizards / TransientModels
- Cron jobs / scheduled actions
- Controllers & REST API basics

If you learned these in Odoo 15, they didn’t magically change in 16/17/18. Stop wasting time.

### 🎯 Must-Watch by Version

**From Odoo 16 tutorials**

Website builder overhaul (new asset bundling, drag-drop, integration with backend)
- Frontend: OWL v1 adoption, new JS patterns
- Accounting: reconciliation widget, field removals/renames
- Knowledge app intro (brand new module)
- Manufacturing (MRP) upgrades: subcontractor portal, order splitting/merging

**From Odoo 17 tutorials**

- UX changes: redesigned menu system, global search bar improvements
- Website + eCommerce unification (no more half-baked separation)
- Frontend: OWL v2 (more stable, bigger ecosystem)
- Spreadsheets module integration (important if you want reporting inside Odoo)

**From Odoo 18 tutorials (bleeding edge, but worth peeking)**

- AI-assisted features (suggestions, auto-completions, smart reconciliations)
- Refinements in Accounting & Inventory (incremental but dev-relevant)
- Continued OWL framework maturity (expect more frontend dev to shift here)

**📌 Fast-Track Watch Order**

1. Finish your Odoo 15 playlist → lock in fundamentals.
2. Jump straight to Odoo 16 → watch only:

   - Website builder
   - OWL frontend intro
   - Accounting changes
   - Knowledge app
   - MRP upgrades

3. From Odoo 17 playlist → skip repeats, watch:
   - UX redesign (menus/search)
   - Website/eCommerce merge
   - OWL v2 deep-dive
   - Spreadsheets integration

4. From Odoo 18 playlist → just cherry-pick:
   - AI helpers
   - Latest Accounting/Inventory tweaks
   - OWL refinements

### 🏁 End Result

- You keep your time: ~20–25% of the videos instead of 100%.
- You stay current on what actually changed.
- You avoid the soul-crushing repetition of "create a new module" tutorials.

---

## 🎯 Odoo Developer Interview Questions

Expected: with related solutions

### � Learning Path Mapping

This section maps interview questions to the learning modules above. Use this to prepare for interviews or assess candidates based on their practical knowledge.

| Experience Level | Study These Modules | Interview Focus |
|-----------------|---------------------|-----------------|
| 🟢 **Junior** (0-1 years) | Modules 1-3 | Setup, basic models, views, security |
| 🟡 **Mid-Level** (1-3 years) | Modules 4-8 | ORM, inheritance, widgets, workflows, wizards |
| 🔴 **Expert** (3+ years) | Modules 9-11 | Advanced features, constraints, reporting, APIs, deployment |

---

### 🟢 Junior Level (0-1 years experience)
*Foundation topics covered in Modules 1-3*

#### Module 1: Setup & Module Structure

1. **What is Odoo and what are its main modules?** *(Module 1)*
   
   ![Odoo Main Dashboard](docs/interview-questions/junior/q01-odoo-dashboard.png)
   <!-- TODO: Screenshot of Odoo main dashboard showing Apps menu with Sales, CRM, Inventory, Accounting modules -->
   
   **Expected Answer:** 
   - Odoo is an open-source ERP (Enterprise Resource Planning) system
   - Main modules include: Sales, CRM, Inventory, Accounting, Manufacturing, HR, Website, etc.
   - Each module handles specific business functions and can be installed/customized independently

---

2. **Explain the structure of an Odoo module.** *(Module 1)*
   
   ![Module Structure](docs/interview-questions/junior/q02-module-structure.png)
   <!-- TODO: Screenshot of VS Code showing om_hospital folder structure -->
   
   **Expected Answer:** `__manifest__.py`, models, views, security folders, data files
   
   **Actual `om_hospital` Module Structure:**
   ```
   om_hospital/
   ├── __init__.py                    # Python package initializer
   ├── __manifest__.py                # Module metadata and configuration
   ├── models/                        # Business logic (Python models)
   │   ├── __init__.py
   │   ├── patient.py
   │   ├── appointment.py
   │   └── patient_tag.py
   ├── views/                         # UI definitions (XML)
   │   ├── menu.xml
   │   ├── patient_view.xml
   │   ├── appointment_view.xml
   │   └── patient_tag_view.xml
   ├── security/                      # Access control
   │   └── ir.model.access.csv
   ├── data/                          # Initial/demo data
   │   ├── sequence.xml
   │   └── patient_tag_data.xml
   ├── wizard/                        # Transient models
   │   └── cancel_appointment.py
   └── static/                        # Assets (images, CSS, JS)
       └── description/
           └── icon.png
   ```

---

3. **What is the purpose of `__manifest__.py`?** *(Module 1)*
   
   ![Manifest File](docs/interview-questions/junior/q03-manifest-file.png)
   <!-- TODO: Screenshot of VS Code showing __manifest__.py content -->
   
   **Expected Answer:** Module metadata, dependencies, data files to load, version info
   
   **Code Example from `om_hospital/__manifest__.py`:**
   ```python
   {
       'name': 'Hospital Management',           # Module display name
       'version': '1.0.0',                      # Version number
       'category': 'Healthcare',                # App category
       'author': 'Adam informatika',            # Author
       'sequence': -100,                        # Menu order
       'summary': 'Manage hospital operations and patient records',
       'depends': [
           'mail',      # For Chatter functionality
           'product'    # For product management
       ],
       'data': [
           'security/ir.model.access.csv',      # Load security first
           'data/sequence.xml',                 # Then data files
           'wizard/cancel_appointment_view.xml',
           'views/menu.xml',                    # Then views
           'views/patient_view.xml',
           'views/appointment_view.xml',
       ],
       'application': True,                     # Standalone application
       'auto_install': False,                   # Manual installation
       'license': 'LGPL-3',
   }
   ```

---

4. **How do you add a menu item in Odoo?** *(Module 1)*
   
   ![Menu in Odoo UI](docs/interview-questions/junior/q04-menu-ui.png)
   <!-- TODO: Screenshot of Odoo showing Hospital menu with submenus -->
   
   **Expected Answer:** Define `<menuitem>` in XML with action, parent, sequence
   
   **Code Example from `om_hospital/views/menu.xml`:**
   ```xml
   <!-- Main Menu -->
   <menuitem id="menu_hospital_root"
             name="Hospital"
             web_icon="om_hospital,static/description/icon.png"
             sequence="0"/>

   <!-- Sub Menu (Parent) -->
   <menuitem id="menu_patient_master"
             name="Patient Details"
             parent="menu_hospital_root"
             sequence="0"/>

   <!-- Sub Menu with Action -->
   <menuitem id="menu_patient"
             name="Patients"
             action="action_hospital_patient"
             parent="menu_patient_master"
             sequence="0"/>
   ```
   
   **Key Attributes:**
   - `id`: Unique identifier
   - `name`: Display text
   - `parent`: Parent menu (for hierarchical structure)
   - `action`: Links to window action
   - `sequence`: Display order (lower = earlier)
   - `web_icon`: Custom icon path


---

#### Module 2: Models & Security

5. **How do you create a new field in an Odoo model?** *(Module 2)*
   
   ![Patient Form View with Fields](docs/interview-questions/junior/q05-patient-form.png)
   <!-- TODO: Screenshot of patient form showing name, age, gender, date_of_birth fields -->
   
   **Expected Answer:** Use Fields class (Char, Integer, Many2one, etc.) in models
   
   **Code Example from `om_hospital/models/patient.py`:**
   ```python
   from odoo import api, fields, models
   
   class HospitalPatient(models.Model):
       _name = "hospital.patient"
       _description = "Hospital Patient"
       
       # Different field types:
       name = fields.Char(string='Patient Name', tracking=True)
       date_of_birth = fields.Date(string='Date of Birth')
       ref = fields.Char(string='Reference')
       age = fields.Integer(string='Age', compute='_compute_age', 
                           tracking=True, store=True)
       gender = fields.Selection([
           ('male', 'Male'),
           ('female', 'Female'),
           ('other', 'Other'),
       ], string='Gender', required=True, tracking=True, default='female')
       active = fields.Boolean(string='Active', default=True, tracking=True)
       image = fields.Image(string="Patient Image")
   ```
   
   **Field Syntax:**
   - `field_name = fields.FieldType(parameters)`
   - Common parameters: `string`, `required`, `default`, `tracking`, `readonly`

---

6. **What are the basic field types in Odoo?** *(Module 2)*
   
   ![Field Types in Code](docs/interview-questions/junior/q06-field-types.png)
   <!-- TODO: Screenshot highlighting different field types in patient.py -->
   
   **Expected Answer:** Char, Text, Integer, Float, Boolean, Date, Datetime, Selection
   
   **Field Types Demonstrated in `patient.py`:**
   ```python
   # Basic Types
   name = fields.Char(string='Patient Name')              # Text (short)
   ref = fields.Char(string='Reference')                  # Text (short)
   age = fields.Integer(string='Age')                     # Whole number
   date_of_birth = fields.Date(string='Date of Birth')    # Date only
   active = fields.Boolean(string='Active', default=True) # True/False
   
   # Selection (Dropdown)
   gender = fields.Selection([
       ('male', 'Male'),
       ('female', 'Female'),
       ('other', 'Other'),
   ], string='Gender', required=True)
   
   # Binary/Image
   image = fields.Image(string="Patient Image")           # Image field
   
   # Relational Fields (covered in Module 5)
   appointment_id = fields.Many2one("hospital.appointment", string="Appointments")
   tag_ids = fields.Many2many("patient.tag", string="Tags")
   ```

---

7. **What is `ir.model.access.csv` used for?** *(Module 2)*
   
   ![Access Rights CSV](docs/interview-questions/junior/q07-access-rights.png)
   <!-- TODO: Screenshot of ir.model.access.csv file in VS Code -->
   
   **Expected Answer:** Access control list - defines which groups can read/write/create/delete records
   
   **Code Example from `om_hospital/security/ir.model.access.csv`:**
   ```csv
   id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
   access_hospital_patient,access_hospital_patient,om_hospital.model_hospital_patient,base.group_user,1,1,1,1
   access_hospital_appointment,access_hospital_appointment,om_hospital.model_hospital_appointment,base.group_user,1,1,1,1
   ```
   
   **Column Explanation:**
   - `id`: Unique identifier
   - `name`: Human-readable name
   - `model_id:id`: Model technical name (prefixed with module name)
   - `group_id:id`: User group with access (`base.group_user` = internal users)
   - `perm_read`: Can view records (1=yes, 0=no)
   - `perm_write`: Can edit records
   - `perm_create`: Can create records
   - `perm_unlink`: Can delete records

---

8. **Write a simple model with name, description, and date fields.** *(Module 2)*
   
   ![Simple Model Example](docs/interview-questions/junior/q08-simple-model.png)
   <!-- TODO: Screenshot of a simple model definition -->
   
   **Expected Answer:** Class inheriting `models.Model`, proper field definitions
   
   **Example - Simplified Patient Model:**
   ```python
   from odoo import models, fields
   
   class HospitalPatient(models.Model):
       _name = "hospital.patient"              # Technical model name (DB table)
       _description = "Hospital Patient"       # Human-readable description
       
       # Basic fields
       name = fields.Char(string='Name', required=True)
       description = fields.Text(string='Description')
       date_of_birth = fields.Date(string='Date of Birth')
   ```
   
   **Key Components:**
   - Inherit from `models.Model`
   - `_name`: Defines database table name (dots become underscores)
   - `_description`: Shows in logs and technical views
   - Field definitions with appropriate types


---

#### Module 3: Views & Basic Operations

9. **Explain the difference between `tree` and `form` views.** *(Module 3)*
   
   ![Tree View - Patient List](docs/interview-questions/junior/q09-tree-view.png)
   <!-- TODO: Screenshot of patient tree view showing list of multiple patients -->
   
   ![Form View - Patient Details](docs/interview-questions/junior/q09-form-view.png)
   <!-- TODO: Screenshot of patient form view showing single patient details -->
   
   **Expected Answer:** Tree = list view, Form = detailed single record view
   
   **Tree View (List) - `patient_view.xml`:**
   ```xml
   <record id="view_hospital_patient_tree" model="ir.ui.view">
       <field name="name">hospital.patient.tree</field>
       <field name="model">hospital.patient</field>
       <field name="arch" type="xml">
           <tree>
               <field name="name"/>
               <field name="age"/>
               <field name="gender"/>
               <field name="ref"/>
               <field name="tag_ids" widget="many2many_tags"/>
           </tree>
       </field>
   </record>
   ```
   
   **Form View (Detail) - `patient_view.xml`:**
   ```xml
   <record id="view_hospital_patient_form" model="ir.ui.view">
       <field name="name">hospital.patient.form</field>
       <field name="model">hospital.patient</field>
       <field name="arch" type="xml">
           <form>
               <sheet>
                   <group>
                       <group>
                           <field name="image" widget="image"/>
                           <field name="name"/>
                           <field name="date_of_birth"/>
                           <field name="age"/>
                       </group>
                       <group>
                           <field name="ref"/>
                           <field name="gender"/>
                           <field name="tag_ids" widget="many2many_tags"/>
                       </group>
                   </group>
               </sheet>
           </form>
       </field>
   </record>
   ```
   
   **Key Differences:**
   - **Tree**: Compact, shows multiple records, columns, sortable
   - **Form**: Detailed, shows single record, grouped fields, full editing

---

10. **What is the difference between `active=True` and `active=False` in records?** *(Module 3)*
    
    ![Archive Button in UI](docs/interview-questions/junior/q10-archive-button.png)
    <!-- TODO: Screenshot showing archive/unarchive action in patient form -->
    
    ![Archived Filter](docs/interview-questions/junior/q10-archived-filter.png)
    <!-- TODO: Screenshot of search view with "Archived" filter -->
    
    **Expected Answer:** Archiving mechanism - inactive records are hidden by default
    
    **Code Implementation in `patient.py`:**
    ```python
    active = fields.Boolean(string='Active', default=True, tracking=True)
    ```
    
    **Search View Filter in `patient_view.xml`:**
    ```xml
    <filter name="filter_archived" string="Archived" 
            domain="[('active', '=', False)]"/>
    ```
    
    **Behavior:**
    - `active=True`: Record is visible in default views
    - `active=False`: Record is archived (soft delete), hidden unless explicitly filtered
    - Odoo automatically adds Archive/Unarchive actions to form views
    - Useful for maintaining historical data without cluttering active lists

---

11. **How do you set a default value for a field?** *(Module 3)*
    
    ![Default Gender Field](docs/interview-questions/junior/q11-default-value.png)
    <!-- TODO: Screenshot of new patient form showing gender defaulting to "Female" -->
    
    **Expected Answer:** Use `default=` parameter or `default_get()` method
    
    **Method 1: Static Default in Field Definition:**
    ```python
    # From patient.py
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, default='female')  # Default value
    
    active = fields.Boolean(string='Active', default=True)
    ```
    
    **Method 2: Dynamic Default with `default_get()` method:**
    ```python
    @api.model
    def default_get(self, fields_list):
        res = super(HospitalPatient, self).default_get(fields_list)
        res['gender'] = 'female'  # Set dynamic default
        return res
    ```
    
    **Method 3: Context in Action (view level):**
    ```xml
    <field name="context">{'default_gender': 'female'}</field>
    ```

---

12. **What is a domain in Odoo? Give examples.** *(Module 3)*
    
    ![Domain Filter in Search View](docs/interview-questions/junior/q12-domain-filter.png)
    <!-- TODO: Screenshot showing Male/Female filter buttons in patient search -->
    
    **Expected Answer:** Filter criteria `[('field', 'operator', 'value')]`
    
    **Code Examples from `patient_view.xml`:**
    ```xml
    <!-- Filter for Male patients -->
    <filter name="filter_male" string="Male" 
            domain="[('gender', '=', 'male')]"/>
    
    <!-- Filter for Female patients -->
    <filter name="filter_female" string="Female" 
            domain="[('gender', '=', 'female')]"/>
    
    <!-- Filter for Archived records -->
    <filter name="filter_archived" string="Archived" 
            domain="[('active', '=', False)]"/>
    ```
    
    **Domain Syntax:**
    ```python
    # Basic operators
    [('field_name', '=', 'value')]        # Equal
    [('field_name', '!=', 'value')]       # Not equal
    [('field_name', '>', 10)]             # Greater than
    [('field_name', '<=', 18)]            # Less than or equal
    [('field_name', 'in', [1, 2, 3])]     # In list
    [('field_name', 'like', 'John')]      # Contains (case-sensitive)
    [('field_name', 'ilike', 'john')]     # Contains (case-insensitive)
    
    # Logical operators
    ['|', ('age', '<', 18), ('age', '>', 65)]  # OR (kids OR seniors)
    [('age', '>=', 18), ('age', '<=', 65)]     # AND (adults)
    ['!', ('active', '=', False)]              # NOT (active records)
    ```

---

13. **How would you make a field required?** *(Module 3)*
    
    ![Required Field Validation](docs/interview-questions/junior/q13-required-field.png)
    <!-- TODO: Screenshot showing validation error when trying to save without required field -->
    
    **Expected Answer:** `required=True` parameter
    
    **Code Example from `patient.py`:**
    ```python
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, tracking=True, default='female')
    ```
    
    **Behavior:**
    - Field shows with bold label and red asterisk (*) in UI
    - Form cannot be saved without filling the required field
    - Validation error appears if user tries to save empty required field
    
    **Conditional Required (in view):**
    ```xml
    <field name="email" attrs="{'required': [('has_email', '=', True)]}"/>
    ```

---

14. **How do you add filters and group by options in search views?** *(Module 3)*
    
    ![Search Filters and Group By](docs/interview-questions/junior/q14-filters-groupby.png)
    <!-- TODO: Screenshot of search view showing filters dropdown and Group By options -->
    
    **Expected Answer:** `<filter>` tags in search view with domain or context for grouping
    
    **Code Example from `patient_view.xml`:**
    ```xml
    <record id="view_hospital_patient_search" model="ir.ui.view">
        <field name="name">hospital.patient.search</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <search>
                <!-- Search by field -->
                <field name="name" filter_domain="['|', ('name', 'ilike', self), 
                                                   ('ref', 'ilike', self)]"/>
                <field name="age"/>
                <field name="gender"/>
                
                <!-- Filter buttons (uses domain) -->
                <filter name="filter_male" string="Male" 
                        domain="[('gender', '=', 'male')]"/>
                <filter name="filter_female" string="Female" 
                        domain="[('gender', '=', 'female')]"/>
                
                <separator/>
                <filter name="filter_archived" string="Archived" 
                        domain="[('active', '=', False)]"/>
                
                <!-- Group By options (uses context) -->
                <group expand="0" string="Group By">
                    <filter name="group_by_gender" string="Gender" 
                            context="{'group_by': 'gender'}"/>
                </group>
                
                <!-- Search Panel (left sidebar) -->
                <searchpanel>
                    <field name="gender" string="Gender" icon="fa-users" 
                           select="multi" enable_counters="1"/>
                </searchpanel>
            </search>
        </field>
    </record>
    ```
    
    **Key Elements:**
    - `<filter>`: Creates filter button with domain or group by
    - `domain`: Filters records based on criteria
    - `context={'group_by': 'field'}`: Groups records by field
    - `<searchpanel>`: Left sidebar for quick filtering

---

15. **What does context do when opening a view?** *(Module 3)*
    
    ![Context in Action](docs/interview-questions/junior/q15-context-action.png)
    <!-- TODO: Screenshot showing patient list with Male filter pre-activated -->
    
    **Expected Answer:** Pass default values, hide/show fields, activate filters
    
    **Code Example from `patient_view.xml`:**
    ```xml
    <record id="action_hospital_patient" model="ir.actions.act_window">
        <field name="name">Patients</field>
        <field name="res_model">hospital.patient</field>
        <field name="view_mode">tree,form</field>
        
        <!-- Context with default filters activated -->
        <field name="context">{
            'search_default_filter_male': 1,      # Activate Male filter
            'search_default_group_by_gender': 1   # Activate Group By Gender
        }</field>
    </record>
    ```
    
    **Common Context Uses:**
    ```python
    # Set default field values
    {'default_gender': 'female', 'default_active': True}
    
    # Activate search filters automatically
    {'search_default_filter_name': 1}
    
    # Hide/show fields dynamically
    {'hide_field_name': True}
    
    # Pass custom data
    {'from_patient_view': True, 'patient_id': 123}
    ```
    
    **Accessing Context in Python:**
    ```python
    def some_method(self):
        gender = self.env.context.get('default_gender')
        if self.env.context.get('from_patient_view'):
            # Custom logic
            pass
    ```

---

---

### 🟡 Mid Level (1-3 years experience)
*Advanced topics covered in Modules 4-8*

#### Module 4: Communication & Tracking

16. **How do you add tracking to a field (chatter)?** *(Module 4)*
    
    ![Field Tracking in Chatter](docs/interview-questions/mid/q16-field-tracking.png)
    <!-- TODO: Screenshot of chatter showing "Gender changed from Male to Female" message -->
    
    **Expected Answer:** Inherit `mail.thread`, add `tracking=True` to field
    
    **Code Example from `patient.py`:**
    ```python
    from odoo import api, fields, models
    
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        _description = "Hospital Patient"
        _inherit = ['mail.thread', 'mail.activity.mixin']  # Enable chatter
        
        # Fields with tracking
        name = fields.Char(string='Patient Name', tracking=True)
        age = fields.Integer(string='Age', tracking=True)
        gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ], string='Gender', required=True, tracking=True)
        active = fields.Boolean(string='Active', default=True, tracking=True)
    ```
    
    **Chatter in Form View (`patient_view.xml`):**
    ```xml
    <form>
        <sheet>
            <!-- Form content -->
        </sheet>
        
        <!-- Chatter widget at bottom -->
        <div class="oe_chatter">
            <field name="message_follower_ids"/>
            <field name="activity_ids"/>
            <field name="message_ids"/>
        </div>
    </form>
    ```
    
    **Benefits:**
    - Automatic audit trail for field changes
    - Displays who changed what and when
    - Users can follow records and receive notifications
    - Adds activities (tasks, calls, meetings)

---

17. **What is the purpose of the search panel?** *(Module 4)*
    
    ![Search Panel in Patient View](docs/interview-questions/mid/q17-search-panel.png)
    <!-- TODO: Screenshot showing left sidebar with Gender filter (Male/Female/Other) -->
    
    **Expected Answer:** Quick filtering sidebar for categories/tags, improves UX
    
    **Code Example from `patient_view.xml`:**
    ```xml
    <record id="view_hospital_patient_search" model="ir.ui.view">
        <field name="name">hospital.patient.search</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="age"/>
                <field name="gender"/>
                
                <!-- Search Panel (Left Sidebar) -->
                <searchpanel>
                    <field name="gender" 
                           string="Gender" 
                           icon="fa-users" 
                           select="multi" 
                           enable_counters="1"/>
                </searchpanel>
            </search>
        </field>
    </record>
    ```
    
    **Key Features:**
    - **`select="multi"`**: Allows multiple selection (checkboxes)
    - **`select="one"`**: Radio buttons (single selection)
    - **`enable_counters="1"`**: Shows record count per category
    - **`icon`**: FontAwesome icon for visual appeal
    
    **Use Cases:**
    - Filter products by category
    - Filter patients by gender/age group
    - Filter tickets by priority/stage
    - Better UX than traditional filter dropdowns

---

18. **How do you enable chatter (mail thread) in a model?** *(Module 4)*
    
    ![Full Chatter Implementation](docs/interview-questions/mid/q18-chatter-full.png)
    <!-- TODO: Screenshot showing chatter with messages, followers, and activities -->
    
    **Expected Answer:** Inherit `mail.thread`, `mail.activity.mixin`, add to view
    
    **Complete Implementation:**
    
    **Step 1: Model Inheritance (`patient.py`):**
    ```python
    from odoo import api, fields, models
    
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        _description = "Hospital Patient"
        
        # Inherit mail mixins for full chatter functionality
        _inherit = ['mail.thread', 'mail.activity.mixin']
        
        name = fields.Char(string='Patient Name', tracking=True)
        gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], string='Gender', tracking=True)
    ```
    
    **Step 2: Add to Manifest (`__manifest__.py`):**
    ```python
    {
        'name': 'Hospital Management',
        'depends': [
            'mail',      # Required for chatter
        ],
        # ... rest of manifest
    }
    ```
    
    **Step 3: Add Chatter to Form View (`patient_view.xml`):**
    ```xml
    <record id="view_hospital_patient_form" model="ir.ui.view">
        <field name="name">hospital.patient.form</field>
        <field name="model">hospital.patient</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="gender"/>
                    </group>
                </sheet>
                
                <!-- Chatter Section -->
                <div class="oe_chatter">
                    <!-- Followers widget -->
                    <field name="message_follower_ids" 
                           widget="mail_followers"/>
                    
                    <!-- Activities (tasks, calls, meetings) -->
                    <field name="activity_ids" 
                           widget="mail_activity"/>
                    
                    <!-- Message thread -->
                    <field name="message_ids" 
                           widget="mail_thread"/>
                </div>
            </form>
        </field>
    </record>
    ```
    
    **What Each Widget Provides:**
    - **`message_follower_ids`**: Follow/unfollow button, follower list
    - **`activity_ids`**: Schedule activities, activity timeline
    - **`message_ids`**: Message thread, internal notes, send messages

---

#### Module 5: Fields Deep Dive

19. **Explain Many2one, One2many, and Many2many relationships.** *(Module 5)*
    
    ![Relational Fields Diagram](docs/interview-questions/mid/q19-relational-fields.png)
    <!-- TODO: Screenshot showing patient form with doctor (Many2one), appointments (One2many), tags (Many2many) -->
    
    **Expected Answer:** Foreign key, reverse relation, junction table concepts
    
    **Many2one (Foreign Key - N:1):**
    ```python
    # patient.py - Many patients can have one doctor
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        # Many2one: Foreign key to res.partner
        doctor_id = fields.Many2one(
            'res.partner',                    # Related model
            string="Doctor",
            domain=[('is_doctor', '=', True)] # Filter only doctors
        )
    ```
    
    **One2many (Reverse Relation - 1:N):**
    ```python
    # patient.py - One patient can have many appointments
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        # One2many: Reverse of Many2one
        appointment_ids = fields.One2many(
            'hospital.appointment',  # Related model
            'patient_id',           # Foreign key field in that model
            string="Appointments"
        )
    
    # appointment.py
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        
        # The Many2one that One2many references
        patient_id = fields.Many2one('hospital.patient', string="Patient")
    ```
    
    **Many2many (Junction Table - N:N):**
    ```python
    # patient.py - Many patients can have many tags
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        # Many2many: Creates junction table automatically
        tag_ids = fields.Many2many(
            'patient.tag',                    # Related model
            'patient_tag_rel',                # Junction table name (optional)
            'patient_id',                     # Column 1 in junction table
            'tag_id',                         # Column 2 in junction table
            string="Tags"
        )
    ```
    
    **Database Structure:**
    - **Many2one**: `doctor_id` column in `hospital_patient` table
    - **One2many**: No column (virtual field from reverse Many2one)
    - **Many2many**: Junction table `patient_tag_rel` with two foreign keys
    
    **View Usage:**
    ```xml
    <!-- Many2one: Dropdown -->
    <field name="doctor_id"/>
    
    <!-- One2many: Embedded list/tree -->
    <field name="appointment_ids">
        <tree>
            <field name="name"/>
            <field name="appointment_date"/>
        </tree>
    </field>
    
    <!-- Many2many: Tags widget -->
    <field name="tag_ids" widget="many2many_tags"/>
    ```

---

20. **What are computed fields? How do you create one?** *(Module 5)*
    
    ![Computed Age Field](docs/interview-questions/mid/q20-computed-field.png)
    <!-- TODO: Screenshot showing age field auto-calculated from date_of_birth -->
    
    **Expected Answer:** Fields calculated from other fields, use `@api.depends` decorator
    
    **Code Example from `patient.py`:**
    ```python
    from odoo import api, fields, models
    from datetime import date
    
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        date_of_birth = fields.Date(string='Date of Birth')
        
        # Computed field with dependencies
        age = fields.Integer(
            string='Age',
            compute='_compute_age',  # Method to compute value
            store=True,              # Store in database (optional)
            tracking=True
        )
        
        @api.depends('date_of_birth')  # Recompute when date_of_birth changes
        def _compute_age(self):
            for rec in self:
                if rec.date_of_birth:
                    today = date.today()
                    dob = rec.date_of_birth
                    rec.age = today.year - dob.year - (
                        (today.month, today.day) < (dob.month, dob.day)
                    )
                else:
                    rec.age = 0
    ```
    
    **Key Concepts:**
    - **`compute='method_name'`**: Method that calculates the value
    - **`@api.depends('field1', 'field2')`**: Triggers recomputation when dependencies change
    - **`store=True`**: Stores value in database (improves performance but uses space)
    - **`store=False`** (default): Computes on-the-fly (saves space but slower)
    - **Loop through `self`**: Always iterate records in computed methods
    
    **Advanced Example with Related Field Dependency:**
    ```python
    @api.depends('appointment_ids.state')  # Depends on related field
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = len(rec.appointment_ids.filtered(
                lambda x: x.state == 'confirmed'
            ))
    ```

---

21. **Explain the `@api.onchange` decorator.** *(Module 5)*
    
    ![Onchange in Action](docs/interview-questions/mid/q21-onchange.png)
    <!-- TODO: Screenshot showing gender changing and auto-updating related fields -->
    
    **Expected Answer:** Triggers when field changes in UI, updates other fields dynamically
    
    **Code Example from `appointment.py`:**
    ```python
    from odoo import api, fields, models
    
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        
        patient_id = fields.Many2one('hospital.patient', string="Patient")
        patient_age = fields.Integer(string="Patient Age", readonly=True)
        patient_gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], string="Gender", readonly=True)
        
        @api.onchange('patient_id')  # Triggers when patient_id changes
        def _onchange_patient_id(self):
            if self.patient_id:
                # Auto-fill patient details
                self.patient_age = self.patient_id.age
                self.patient_gender = self.patient_id.gender
            else:
                # Clear fields when patient is removed
                self.patient_age = 0
                self.patient_gender = False
    ```
    
    **Key Differences: `@api.onchange` vs `@api.depends`**
    
    | Feature | `@api.onchange` | `@api.depends` (Computed) |
    |---------|-----------------|---------------------------|
    | **When** | User changes field in UI | Any time dependency changes |
    | **Where** | Client-side only | Server-side |
    | **Saves?** | No (until form saved) | Yes (if `store=True`) |
    | **Use Case** | Auto-fill related fields | Calculate values |
    | **Performance** | Instant in UI | May require DB query |
    
    **Advanced Onchange with Warning:**
    ```python
    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        if self.date_of_birth and self.date_of_birth > fields.Date.today():
            return {
                'warning': {
                    'title': 'Invalid Date',
                    'message': 'Date of birth cannot be in the future!'
                }
            }
    ```
    
    **Onchange with Domain Update:**
    ```python
    @api.onchange('doctor_id')
    def _onchange_doctor_id(self):
        # Update domain for available appointment slots
        if self.doctor_id:
            return {
                'domain': {
                    'appointment_slot_id': [('doctor_id', '=', self.doctor_id.id)]
                }
            }
    ```

---

22. **What does `_rec_name` do in a model?** *(Module 5)*
    
    ![Rec Name in Many2one](docs/interview-questions/mid/q22-rec-name.png)
    <!-- TODO: Screenshot showing patient reference (REF0001) displayed in Many2one dropdown -->
    
    **Expected Answer:** Specifies which field to use as display name in Many2one relations
    
    **Default Behavior (using `name` field):**
    ```python
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        name = fields.Char(string='Patient Name')  # Default display field
    ```
    
    **Custom `_rec_name` Implementation:**
    ```python
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        _rec_name = 'ref'  # Use 'ref' field instead of 'name'
        
        name = fields.Char(string='Patient Name')
        ref = fields.Char(string='Reference')  # REF0001, REF0002, etc.
    ```
    
    **Advanced: Custom Display with `name_get()`:**
    ```python
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        name = fields.Char(string='Patient Name')
        ref = fields.Char(string='Reference')
        age = fields.Integer(string='Age')
        
        def name_get(self):
            """Custom display format for Many2one fields"""
            result = []
            for rec in self:
                # Format: "[REF0001] John Doe (45)"
                display_name = f"[{rec.ref}] {rec.name}"
                if rec.age:
                    display_name += f" ({rec.age})"
                result.append((rec.id, display_name))
            return result
    ```
    
    **When to Use:**
    - `_rec_name`: Simple field swap (e.g., use code instead of name)
    - `name_get()`: Complex formatting (combine multiple fields)

---

23. **What is a related field and when would you use it?** *(Module 5)*
    
    ![Related Field Example](docs/interview-questions/mid/q23-related-field.png)
    <!-- TODO: Screenshot showing appointment form with patient_phone auto-filled from patient -->
    
    **Expected Answer:** Shortcut to access related record's field, use `related=` parameter
    
    **Code Example from `appointment.py`:**
    ```python
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        
        patient_id = fields.Many2one('hospital.patient', string="Patient")
        
        # Related field: Shortcut to patient_id.phone
        patient_phone = fields.Char(
            string="Patient Phone",
            related='patient_id.phone',  # Dot notation for related path
            store=True,                  # Optional: store in DB
            readonly=True                # Usually readonly
        )
        
        # Related field from nested relation
        patient_doctor_name = fields.Char(
            string="Patient's Doctor",
            related='patient_id.doctor_id.name',  # Multi-level relation
            readonly=True
        )
    ```
    
    **Benefits:**
    - **Convenience**: Access related fields without writing code
    - **Searchable**: Can search/filter on related fields
    - **Performance**: If `store=True`, avoids JOIN queries
    
    **Use Cases:**
    ```python
    # Get customer country from sale order
    country_id = fields.Many2one(
        'res.country',
        related='partner_id.country_id',
        string="Customer Country",
        store=True
    )
    
    # Get product category from order line
    product_category_id = fields.Many2one(
        'product.category',
        related='product_id.categ_id',
        string="Product Category",
        readonly=True
    )
    ```
    
    **When to Use:**
    - Display related data without custom computed field
    - Make related fields searchable in views
    - Simplify reports and filters
    
    **When NOT to Use:**
    - Complex calculations (use computed fields instead)
    - Writable fields (use computed with inverse function)

---

24. **How do you add an image field to a model?** *(Module 5)*
    
    ![Image Field in Form](docs/interview-questions/mid/q24-image-field.png)
    <!-- TODO: Screenshot showing patient image in form view -->
    
    **Expected Answer:** Use `fields.Image` or `fields.Binary`, display with image widget
    
    **Code Example from `patient.py`:**
    ```python
    from odoo import fields, models
    
    class HospitalPatient(models.Model):
        _name = "hospital.patient"
        
        # Image field (Odoo 13+)
        image = fields.Image(string="Patient Image")
        
        # Alternative: Binary field (older Odoo versions)
        # image = fields.Binary(string="Patient Image")
    ```
    
    **Display in Form View (`patient_view.xml`):**
    ```xml
    <form>
        <sheet>
            <field name="image" widget="image" class="oe_avatar"/>
            
            <!-- Or with explicit size -->
            <field name="image" 
                   widget="image" 
                   options="{'size': [200, 200]}"/>
            
            <group>
                <field name="name"/>
                <field name="age"/>
            </group>
        </sheet>
    </form>
    ```
    
    **Image Field Features (Odoo 13+):**
    - Automatically creates resized variants (1920, 1024, 512, 256, 128)
    - Optimized storage and performance
    - Built-in image processing
    
    **Access Resized Variants:**
    ```python
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
    ```
    
    **Avatar Style (Top-Right Corner):**
    ```xml
    <sheet>
        <field name="image" widget="image" class="oe_avatar"/>
        <div class="oe_title">
            <h1><field name="name"/></h1>
        </div>
    </sheet>
    ```

---

#### Module 6: Widgets & Decorations

25. **Explain widgets in Odoo. Name at least 5.** *(Module 6)*
    
    ![Common Widgets in Action](docs/interview-questions/mid/q25-widgets.png)
    <!-- TODO: Screenshot showing multiple widgets: statusbar, priority stars, tags, image, badge -->
    
    **Expected Answer:** statusbar, priority, badge, image, many2many_tags, handle, color, etc.
    
    **Common Widgets with Examples:**
    
    **1. Statusbar Widget:**
    ```xml
    <field name="state" widget="statusbar" 
           statusbar_visible="draft,confirmed,done"/>
    ```
    
    **2. Priority Widget (Stars):**
    ```xml
    <field name="priority" widget="priority"/>
    ```
    ```python
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Priority', default='0')
    ```
    
    **3. Many2many Tags:**
    ```xml
    <field name="tag_ids" widget="many2many_tags" 
           options="{'color_field': 'color'}"/>
    ```
    
    **4. Badge Widget:**
    ```xml
    <field name="state" widget="badge" 
           decoration-success="state == 'done'"
           decoration-info="state == 'draft'"/>
    ```
    
    **5. Image Widget:**
    ```xml
    <field name="image" widget="image" class="oe_avatar"/>
    ```
    
    **6. Handle Widget (Drag/Drop Reordering):**
    ```xml
    <tree>
        <field name="sequence" widget="handle"/>
        <field name="name"/>
    </tree>
    ```
    
    **7. Color Picker:**
    ```xml
    <field name="color" widget="color"/>
    ```
    
    **8. Boolean Toggle:**
    ```xml
    <field name="active" widget="boolean_toggle"/>
    ```
    
    **9. Progressbar:**
    ```xml
    <field name="progress" widget="progressbar"/>
    ```
    ```python
    progress = fields.Float(string='Progress', default=0.0)
    ```
    
    **10. Monetary Widget:**
    ```xml
    <field name="total_amount" widget="monetary" 
           options="{'currency_field': 'currency_id'}"/>
    ```

---

26. **How do you add a button in a form view that triggers a Python method?** *(Module 6)*
    
    ![Action Buttons in Form](docs/interview-questions/mid/q26-action-buttons.png)
    <!-- TODO: Screenshot showing Confirm, Done, Cancel buttons in appointment form -->
    
    **Expected Answer:** `<button>` tag with `type="object"` and `name="method_name"`
    
    **Code Example from `appointment_view.xml`:**
    ```xml
    <form>
        <header>
            <!-- Object button: Calls Python method -->
            <button name="action_confirm" 
                    type="object" 
                    string="Confirm" 
                    class="btn-primary"
                    states="draft"/>
            
            <!-- With confirmation dialog -->
            <button name="action_done" 
                    type="object" 
                    string="Mark as Done" 
                    class="btn-success"
                    confirm="Are you sure you want to mark this as done?"
                    states="confirmed"/>
            
            <!-- With icon -->
            <button name="action_cancel" 
                    type="object" 
                    string="Cancel" 
                    class="btn-danger"
                    icon="fa-times"
                    states="draft,confirmed"/>
            
            <field name="state" widget="statusbar"/>
        </header>
        <sheet>
            <!-- Form content -->
        </sheet>
    </form>
    ```
    
    **Python Methods in `appointment.py`:**
    ```python
    from odoo import api, fields, models
    from odoo.exceptions import ValidationError
    
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        
        state = fields.Selection([
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ], string='Status', default='draft', required=True, tracking=True)
        
        def action_confirm(self):
            """Button method: Confirm appointment"""
            for rec in self:
                if rec.state != 'draft':
                    raise ValidationError('Only draft appointments can be confirmed!')
                rec.state = 'confirmed'
        
        def action_done(self):
            """Button method: Mark as done"""
            self.write({'state': 'done'})
        
        def action_cancel(self):
            """Button method: Cancel appointment"""
            return {
                'type': 'ir.actions.act_window',
                'name': 'Cancel Appointment',
                'res_model': 'cancel.appointment.wizard',
                'view_mode': 'form',
                'target': 'new',  # Open as popup
                'context': {'default_appointment_id': self.id}
            }
    ```
    
    **Button Attributes:**
    - **`type="object"`**: Calls Python method
    - **`type="action"`**: Calls window action
    - **`name`**: Method/action name
    - **`string`**: Button label
    - **`class`**: Bootstrap CSS class (btn-primary, btn-success, btn-danger)
    - **`states`**: Show button only in specific states
    - **`confirm`**: Confirmation dialog message
    - **`icon`**: FontAwesome icon
    - **`invisible`**: Hide button based on condition

---

27. **What is the purpose of `attrs` in view definitions?** *(Module 6)*
    
    ![Dynamic Attrs Behavior](docs/interview-questions/mid/q27-attrs.png)
    <!-- TODO: Screenshot showing field becoming readonly when state changes -->
    
    **Expected Answer:** Dynamic visibility/readonly/required based on conditions
    
    **Code Example from `appointment_view.xml`:**
    ```xml
    <form>
        <sheet>
            <group>
                <!-- Invisible when state is draft -->
                <field name="confirmation_date" 
                       attrs="{'invisible': [('state', '=', 'draft')]}"/>
                
                <!-- Readonly when state is not draft -->
                <field name="patient_id" 
                       attrs="{'readonly': [('state', '!=', 'draft')]}"/>
                
                <!-- Required when appointment type is 'consultation' -->
                <field name="doctor_id" 
                       attrs="{'required': [('appointment_type', '=', 'consultation')]}"/>
                
                <!-- Multiple conditions with OR -->
                <field name="notes" 
                       attrs="{
                           'invisible': ['|', 
                               ('state', '=', 'cancelled'), 
                               ('state', '=', 'done')
                           ]
                       }"/>
                
                <!-- Multiple conditions with AND -->
                <field name="follow_up_date" 
                       attrs="{
                           'required': [
                               ('state', '=', 'done'),
                               ('requires_followup', '=', True)
                           ]
                       }"/>
                
                <!-- Multiple attributes at once -->
                <field name="cancellation_reason" 
                       attrs="{
                           'invisible': [('state', '!=', 'cancelled')],
                           'required': [('state', '=', 'cancelled')]
                       }"/>
            </group>
        </sheet>
    </form>
    ```
    
    **Domain Syntax in `attrs`:**
    ```python
    # Single condition
    [('field_name', 'operator', 'value')]
    
    # AND conditions (default when multiple conditions)
    [('field1', '=', 'value1'), ('field2', '>', 10)]
    
    # OR conditions (use '|' prefix)
    ['|', ('field1', '=', 'value1'), ('field2', '=', 'value2')]
    
    # NOT condition (use '!' prefix)
    ['!', ('field', '=', 'value')]
    
    # Complex: (field1 = 'A' AND field2 > 10) OR (field3 = 'B')
    ['|', 
        ('field1', '=', 'A'), ('field2', '>', 10),
        ('field3', '=', 'B')
    ]
    ```
    
    **Common Use Cases:**
    - Hide fields in certain states
    - Make fields readonly after submission
    - Conditional required fields
    - Dynamic form layout based on user input

---

28. **How do you implement a statusbar widget?** *(Module 6)*
    
    ![Statusbar Widget](docs/interview-questions/mid/q28-statusbar.png)
    <!-- TODO: Screenshot showing statusbar with Draft, Confirmed, Done states -->
    
    **Expected Answer:** Selection field with `statusbar` widget, define clickable states
    
    **Complete Implementation:**
    
    **Step 1: Define State Field (`appointment.py`):**
    ```python
    from odoo import api, fields, models
    
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        
        state = fields.Selection([
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ], string='Status', default='draft', required=True, tracking=True)
    ```
    
    **Step 2: Add Statusbar to View (`appointment_view.xml`):**
    ```xml
    <form>
        <header>
            <!-- Statusbar widget -->
            <field name="state" 
                   widget="statusbar" 
                   statusbar_visible="draft,confirmed,done"
                   options="{'clickable': '1'}"/>
        </header>
        <sheet>
            <!-- Form content -->
        </sheet>
    </form>
    ```
    
    **Step 3: Add State Transition Methods:**
    ```python
    def action_confirm(self):
        """Transition from draft to confirmed"""
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'confirmed'
    
    def action_done(self):
        """Transition from confirmed to done"""
        for rec in self:
            if rec.state == 'confirmed':
                rec.state = 'done'
    
    def action_cancel(self):
        """Cancel appointment from any state"""
        self.write({'state': 'cancelled'})
    
    def action_draft(self):
        """Reset to draft"""
        self.write({'state': 'draft'})
    ```
    
    **Statusbar Attributes:**
    - **`statusbar_visible`**: Show only these states in bar (hides cancelled)
    - **`options="{'clickable': '1'}"`**: Make states clickable (direct transition)
    - **`options="{'clickable': '0'}"`**: Non-clickable (use buttons instead)
    
    **With Action Buttons:**
    ```xml
    <header>
        <button name="action_confirm" string="Confirm" 
                type="object" states="draft" class="btn-primary"/>
        <button name="action_done" string="Done" 
                type="object" states="confirmed" class="btn-success"/>
        <button name="action_cancel" string="Cancel" 
                type="object" states="draft,confirmed" class="btn-danger"/>
        
        <field name="state" widget="statusbar" 
               statusbar_visible="draft,confirmed,done"/>
    </header>
    ```

---

29. **What are decorations in tree views?** *(Module 6)*
    
    ![Tree View Decorations](docs/interview-questions/mid/q29-decorations.png)
    <!-- TODO: Screenshot showing colored rows based on state (green=done, red=cancelled) -->
    
    **Expected Answer:** Apply colors/styles based on conditions (decoration-success, decoration-danger)
    
    **Code Example from `appointment_view.xml`:**
    ```xml
    <record id="view_hospital_appointment_tree" model="ir.ui.view">
        <field name="name">hospital.appointment.tree</field>
        <field name="model">hospital.appointment</field>
        <field name="arch" type="xml">
            <tree decoration-success="state == 'done'"
                  decoration-danger="state == 'cancelled'"
                  decoration-info="state == 'draft'"
                  decoration-warning="state == 'confirmed'"
                  decoration-muted="active == False"
                  decoration-bf="priority == '3'">
                
                <field name="name"/>
                <field name="patient_id"/>
                <field name="appointment_date"/>
                <field name="state" widget="badge"/>
                <field name="priority" widget="priority"/>
                <field name="active" invisible="1"/>  <!-- Hidden but used in decoration -->
            </tree>
        </field>
    </record>
    ```
    
    **Available Decorations:**
    
    | Decoration | Color | Use Case |
    |------------|-------|----------|
    | `decoration-success` | Green | Completed, Done, Success |
    | `decoration-danger` | Red | Cancelled, Error, Critical |
    | `decoration-warning` | Orange | Warning, Pending Action |
    | `decoration-info` | Blue | Draft, Info, New |
    | `decoration-muted` | Gray | Archived, Inactive |
    | `decoration-primary` | Primary color | Important records |
    | `decoration-bf` | Bold font | High priority |
    | `decoration-it` | Italic | Special notation |
    
    **Complex Conditions:**
    ```xml
    <!-- Multiple conditions with AND -->
    <tree decoration-danger="state == 'cancelled' and priority == '3'">
    
    <!-- OR condition -->
    <tree decoration-warning="state == 'confirmed' or priority &gt;= '2'">
    
    <!-- Date comparisons -->
    <tree decoration-danger="appointment_date &lt; current_date and state != 'done'">
    
    <!-- Combine multiple decorations -->
    <tree decoration-success="state == 'done'"
          decoration-danger="state == 'cancelled'"
          decoration-bf="priority == '3'">
    ```
    
    **Note:** In XML, use `&lt;` for `<` and `&gt;` for `>` in conditions.

---

30. **How do you add a confirmation dialog to a button?** *(Module 6)*
    
    ![Confirmation Dialog](docs/interview-questions/mid/q30-confirm-dialog.png)
    <!-- TODO: Screenshot showing "Are you sure you want to delete?" dialog -->
    
    **Expected Answer:** Use `confirm="message"` attribute in button tag
    
    **Simple Confirmation:**
    ```xml
    <button name="action_delete" 
            type="object" 
            string="Delete" 
            class="btn-danger"
            confirm="Are you sure you want to delete this record?"/>
    ```
    
    **State-Specific Confirmation:**
    ```xml
    <header>
        <button name="action_done" 
                type="object" 
                string="Mark as Done" 
                class="btn-success"
                states="confirmed"
                confirm="Are you sure you want to mark this appointment as done?"/>
        
        <button name="action_cancel" 
                type="object" 
                string="Cancel Appointment" 
                class="btn-danger"
                states="draft,confirmed"
                confirm="This will cancel the appointment. Do you want to proceed?"/>
    </header>
    ```
    
    **Advanced: Custom Confirmation with Wizard:**
    ```python
    # appointment.py
    def action_cancel_with_reason(self):
        """Open wizard for cancellation with reason"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cancel Appointment',
            'res_model': 'cancel.appointment.wizard',
            'view_mode': 'form',
            'target': 'new',  # Opens as popup dialog
            'context': {
                'default_appointment_id': self.id,
                'default_date': self.appointment_date,
            }
        }
    ```
    
    ```xml
    <!-- No confirm attribute - opens custom wizard instead -->
    <button name="action_cancel_with_reason" 
            type="object" 
            string="Cancel with Reason" 
            class="btn-warning"
            states="draft,confirmed"/>
    ```
    
    **Wizard View (`cancel_appointment_view.xml`):**
    ```xml
    <record id="view_cancel_appointment_wizard_form" model="ir.ui.view">
        <field name="name">cancel.appointment.wizard.form</field>
        <field name="model">cancel.appointment.wizard</field>
        <field name="arch" type="xml">
            <form>
                <group>
                    <field name="appointment_id" readonly="1"/>
                    <field name="reason" required="1"/>
                </group>
                <footer>
                    <button string="Confirm Cancellation" 
                            type="object" 
                            name="action_cancel" 
                            class="btn-primary"/>
                    <button string="Discard" 
                            class="btn-secondary" 
                            special="cancel"/>
                </footer>
            </form>
        </field>
    </record>
    ```

---

#### Module 7: Workflows & Wizards
31. **How do you create a wizard (TransientModel)?** *(Module 7)*
    - Expected: Inherit `models.TransientModel`, create view, link with action

32. **How do you control statusbar states with buttons?** *(Module 7)*
    - Expected: Methods that update state field, buttons with `states` attribute

33. **Explain One2many fields and when to use them.** *(Module 7)*
    - Expected: Reverse of Many2one, display related records (e.g., order lines)

34. **How do you load initial data into Odoo?** *(Module 7)*
    - Expected: XML/CSV files in `data/` folder, referenced in manifest

35. **What is `noupdate="1"` in data files?** *(Module 7)*
    - Expected: Prevents Odoo from updating the record on module upgrade

36. **How do you enable hotkeys for buttons?** *(Module 7)*
    - Expected: Add `accesskey` attribute or use Odoo shortcuts

#### Module 8: Inheritance & ORM
37. **Explain the difference between `_name`, `_inherit`, and `_inherits`.** *(Module 8)*
    - Expected: `_name` = new model, `_inherit` = extend existing, `_inherits` = delegation inheritance

38. **How do you override the `create()` method? Give an example.** *(Module 8)*
    - Expected: Call `super().create()`, add custom logic before/after

39. **How do you override the `write()` method?** *(Module 8)*
    - Expected: Call `super().write()`, add validation or side effects

40. **What ORM methods would you use to:**
    - Create a record?
    - Search for records?
    - Update a record?
    - Delete a record?
    - Expected: `create()`, `search()`, `write()`, `unlink()` *(Module 8)*

41. **What is the difference between `search()` and `search_read()`?** *(Module 8)*
    - Expected: `search()` returns recordset, `search_read()` returns list of dicts

42. **How do you use sequences for auto-generated reference numbers?** *(Module 8)*
    - Expected: Define sequence in XML, call `env['ir.sequence'].next_by_code()`

43. **Explain `name_get()` and when to override it.** *(Module 8)*
    - Expected: Customizes display name format, returns list of (id, name) tuples

#### Security & Advanced Features
44. **Explain the difference between access rights and record rules.** *(Modules 2, 7)*
    - Expected: Access = model-level CRUD, Record rules = row-level filters

45. **What is the purpose of `groups_id` in field definitions?** *(Module 7)*
    - Expected: Field-level security - show only to specific user groups

46. **How do you handle translations in Odoo?** *(Modules 7-8)*
    - Expected: `_()` function for strings, PO files, translate=True for fields

#### Practical Scenarios
47. **Create a computed field that calculates total from line items.** *(Module 5)*
48. **Write a domain that shows only active records created this year.** *(Module 3)*
49. **How would you prevent deletion of records in certain states?** *(Module 8)*
    - Expected: Override `unlink()` method, raise ValidationError
50. **Create an onchange that auto-fills city based on zip code.** *(Module 5)*

---

### 🔴 Expert Level (3+ years experience)
*Advanced topics covered in Modules 9-11*

#### Module 9: Advanced Features & Constraints
51. **How do you raise validation errors in Odoo?** *(Module 9)*
    - Expected: Use `raise ValidationError(_("Message"))` from `odoo.exceptions`

52. **What are SQL constraints vs Python constraints?** *(Module 9)*
    - Expected: SQL = DB-level (UNIQUE, CHECK), Python = `@api.constrains` decorator

53. **Implement a Python constraint that ensures email is unique.** *(Module 9)*
    - Expected: `@api.constrains` decorator, check uniqueness, raise error

54. **How do you apply a domain to a Many2one field dynamically?** *(Module 9)*
    - Expected: Use `domain=` attribute in field or view with dynamic expressions

55. **What is `store=True` for computed fields?** *(Module 9)*
    - Expected: Stores value in DB, improves performance, triggers on dependencies

56. **How do you make a computed field searchable?** *(Module 9)*
    - Expected: Add `search=` parameter with custom search method

57. **Explain inverse functions for computed fields.** *(Module 9)*
    - Expected: Makes computed field editable, `inverse=` method to update source fields

58. **What are ondelete policies (CASCADE vs RESTRICT)?** *(Module 9)*
    - Expected: CASCADE deletes related records, RESTRICT prevents deletion

59. **How do you make fields conditionally invisible/readonly/required?** *(Module 9)*
    - Expected: Use `attrs` in view or `states`, `invisible`, `readonly`, `required` attributes

60. **What is the `@api.ondelete` decorator?** *(Module 9)*
    - Expected: Execute custom code when deleting records, use `at_uninstall` flag

#### Advanced ORM & Environment
61. **Explain the Odoo environment (`self.env`). What can you access through it?** *(Module 9)*
    - Expected: `env.user`, `env.company`, `env.cr` (cursor), `env.context`, `env.ref()`

62. **What is the difference between `self.env.cr.execute()` and ORM methods?** *(Module 9)*
    - Expected: Raw SQL vs ORM (security, caching, access rights differences)

63. **When and why would you use `sudo()`?** *(Module 9)*
    - Expected: Bypass access rights, admin-level operations, security implications

64. **Explain `with_context()` and `with_company()`.** *(Module 9)*
    - Expected: Temporary context modification, multi-company scenarios

65. **How does Odoo handle multi-company architecture?** *(Module 9)*
    - Expected: `company_id` field, record rules, security models

66. **What are the performance implications of stored vs non-stored computed fields?** *(Module 9)*
    - Expected: DB space vs computation time, cache, dependencies, recomputation triggers

67. **Explain the `@api.model` decorator.** *(Module 8)*
    - Expected: Class-level method, no recordset (similar to classmethod)

68. **How do you handle circular dependencies in computed fields?** *(Module 9)*
    - Expected: Careful `@api.depends` design, inverse functions, avoid recursion

69. **What is the purpose of `_sql_constraints`?** *(Module 9)*
    - Expected: Database-level constraints (UNIQUE, CHECK), faster than Python

70. **Explain method resolution order (MRO) in Odoo inheritance.** *(Module 8)*
    - Expected: Multiple inheritance chain, how Odoo resolves conflicts

#### Module 10: Reporting & Integrations
71. **How do you create a custom PDF report with dynamic content?** *(Module 10)*
    - Expected: QWeb template, report action, Python report class

72. **Explain QWeb and its use cases.** *(Module 10)*
    - Expected: Templating engine for reports, website, views

73. **How do you generate Excel reports from Odoo?** *(Module 10)*
    - Expected: `xlsxwriter` library, AbstractModel inheritance, download action

74. **How do you add barcodes and QR codes to PDF reports?** *(Module 10)*
    - Expected: QWeb expressions with barcode/QR code helpers

75. **How do you create a custom REST API endpoint in Odoo?** *(Module 10)*
    - Expected: Controller class, `@http.route`, JSON responses, authentication

76. **Explain XMLRPC vs JSONRPC in Odoo.** *(Module 10)*
    - Expected: External API protocols, use cases, authentication methods

77. **How would you integrate Odoo with an external service (e.g., payment gateway)?** *(Module 10)*
    - Expected: API calls, webhooks, scheduled actions, error handling

78. **What are the security considerations for external API integration?** *(Module 10)*
    - Expected: API keys, CORS, rate limiting, input validation

79. **How do you use Postman to test Odoo APIs?** *(Module 10)*
    - Expected: Authentication setup, request configuration, code generation

#### Module 11: Deployment & DevOps
80. **Explain the Odoo module upgrade process.** *(Module 11)*
    - Expected: `-u module_name`, migration scripts, version in manifest

81. **How do you handle database migrations in Odoo?** *(Module 11)*
    - Expected: `pre.py` and `post.py` migration scripts in `migrations/` folder

82. **How do you debug Odoo in a Docker container?** *(Module 11)*
    - Expected: Remote debugging, pydevd-odoo, port mapping, attach to process

83. **Explain the purpose of `--workers`, `--max-cron-threads`, and `--limit-time-cpu`.** *(Module 11)*
    - Expected: Concurrency control, resource limits, production configuration

84. **What are workers in Odoo? When do you need them?** *(Module 11)*
    - Expected: Multiprocessing, concurrent requests, long-running tasks

85. **How do you run Odoo from command line?** *(Module 11)*
    - Expected: `odoo -c config.conf -d database -u module`

#### Advanced Views & Frontend
86. **How do you create a custom widget in Odoo?** *(Module 6, advanced)*
    - Expected: JavaScript widget registration, template, CSS (mention OWL for 16+)

87. **How do you pass data from Python to JavaScript?** *(Module 6)*
    - Expected: Context, widget props, JSON endpoints

88. **What is the difference between OWL v1 and v2?** *(Odoo 16-17)*
    - Expected: Component lifecycle, reactivity, hooks (Odoo 16 vs 17+)

89. **How do you debug JavaScript issues in Odoo?** *(Module 11)*
    - Expected: Browser console, asset debug mode, source maps

90. **Explain how asset bundles work in Odoo.** *(Module 10)*
    - Expected: Asset XML declarations, JS/CSS compilation, lazy loading

#### Performance & Optimization
91. **How do you optimize a slow Odoo query?** *(Module 9)*
    - Expected: Indexes, reduce computed fields, prefetch, `read_group()`, SQL explain

92. **Explain prefetching in Odoo ORM.** *(Module 8)*
    - Expected: Batch loading of related records to reduce queries

93. **How do you profile Odoo performance issues?** *(Module 11)*
    - Expected: `--log-level=debug`, Python profilers, query logs, Odoo profiler

94. **What is `@api.depends_context` and when would you use it?** *(Module 9)*
    - Expected: Computed field depends on context values (company, lang, etc.)

95. **Explain how to add a pivot/graph view to a model.** *(Module 10)*
    - Expected: `<graph>` and `<pivot>` view types, measure fields, grouping

96. **What is the purpose of `search_default_` in context?** *(Module 3)*
    - Expected: Auto-activate search filters when view opens

#### Real-World Expert Scenarios
97. **Design a multi-step approval workflow for purchase orders.** *(Modules 7, 8, 9)*
    - Expected: State field, buttons, groups, email notifications, constraints

98. **How would you implement a custom pricing rule engine?** *(Modules 5, 8)*
    - Expected: Pricelist inheritance, computed fields, onchange logic

99. **Design a system to sync Odoo inventory with an external warehouse.** *(Modules 10, 11)*
    - Expected: Scheduled actions, API integration, error handling, logging

100. **How do you handle large data imports (100k+ records)?** *(Modules 7, 11)*
     - Expected: Batch processing, `load()` method, disable tracking, SQL bulk insert

101. **Implement a custom field that behaves differently for different user groups.** *(Modules 2, 5, 9)*
     - Expected: Computed fields with `env.user` checks, attrs in views

102. **Design a reporting dashboard with real-time data.** *(Modules 10, 11)*
     - Expected: Custom controllers, JS widgets, websockets (advanced), caching

103. **What are the best practices for Odoo module development?** *(All Modules)*
     - Expected: Small commits, testing, linting, documentation, version control, proper inheritance

---

### 💡 Behavioral & Situational Questions (All Levels)

104. **Describe a challenging Odoo customization you implemented.** *(All Modules)*
105. **How do you approach debugging a production issue in Odoo?** *(Module 11)*
106. **What's your experience with Odoo upgrades (e.g., 13 → 15 → 17)?** *(Module 11)*
107. **How do you stay updated with Odoo developments?** *(Professional Development)*
108. **Explain a situation where you had to optimize slow Odoo performance.** *(Modules 9, 11)*
109. **How do you handle conflicting requirements from business users?** *(Project Management)*
110. **What's your testing strategy for Odoo modules?** *(Module 11)*
111. **Describe your experience with Odoo community vs Enterprise.** *(General Knowledge)*
112. **How do you document your Odoo customizations?** *(Best Practices)*
113. **What would you do if a module upgrade breaks existing functionality?** *(Module 11)*

---

### 📝 Coding Challenges by Experience Level

#### 🟢 Junior Level Challenges
**Challenge 1: Library Management Module** *(Modules 1-3)*
- Create models: Book (title, author, ISBN, published_date), Member (name, email, phone)
- Implement basic views (tree, form, search)
- Add proper access rights
- Use domains to filter available books

**Challenge 2: Appointment Cancellation Wizard** *(Module 7)*
- Create a wizard to cancel appointments
- Add a reason field (required)
- Update appointment state on confirmation
- Show appropriate success message

---

#### 🟡 Mid-Level Challenges
**Challenge 3: Discount Calculation System** *(Modules 5, 8)*
- Implement multiple discount rules (percentage, fixed amount, tiered)
- Use computed fields for automatic calculation
- Apply onchange methods for dynamic updates
- Override create/write to validate discount limits

**Challenge 4: Sales Report by Category** *(Modules 7, 10)*
- Create a custom report showing monthly sales grouped by product category
- Include filters for date range and salesperson
- Use QWeb template for PDF generation
- Add graph/pivot views for data visualization

**Challenge 5: Three-State Workflow** *(Modules 7, 8)*
- Implement a workflow: Draft → Confirmed → Done
- Add buttons with proper state transitions
- Implement access controls (only managers can confirm)
- Add field tracking for audit trail

---

#### 🔴 Expert Level Challenges
**Challenge 6: Multi-Tenant System** *(Modules 9, 11)*
- Design data isolation using record rules
- Implement company-specific configurations
- Handle shared vs company-specific data
- Optimize queries with proper indexing

**Challenge 7: Inventory Reservation System** *(Modules 8, 9, 10)*
- Create custom reservation logic with expiration
- Implement SQL constraints for stock availability
- Add scheduled actions for auto-release
- Build API endpoints for external warehouse integration

**Challenge 8: Real-Time Stock Alert System** *(Modules 9, 10, 11)*
- Monitor stock levels with computed fields
- Send notifications when below threshold
- Create dashboard with live updates
- Implement webhook integration for external systems

**Challenge 9: Custom Dashboard with KPIs** *(Modules 6, 10)*
- Build interactive dashboard using JS widgets
- Include charts (sales trends, top products, revenue)
- Add filters and date range selectors
- Optimize for performance with caching

---

### 🎓 Assessment & Interview Tips

#### 🟢 For Junior Candidates (Modules 1-3):
**Focus Areas:**
- Understanding of Odoo basics: models, views, fields
- Ability to navigate Odoo UI and studio
- Can they create simple modules independently?
- Do they understand MVC pattern in Odoo context?
- Basic debugging skills

**Red Flags:**
- Cannot explain `__manifest__.py` structure
- Doesn't understand difference between tree and form views
- No knowledge of access rights (`ir.model.access.csv`)
- Cannot write basic domains

**Green Flags:**
- Has completed om_hospital module or similar tutorial
- Can explain field types and when to use each
- Understands basic security (groups, access rights)
- Knows how to use Odoo developer mode

---

#### 🟡 For Mid-Level Candidates (Modules 4-8):
**Focus Areas:**
- Deep ORM knowledge (inheritance, computed fields, relationships)
- Can they solve real business logic problems?
- Understanding of performance implications
- Independent feature development capability
- Wizard and workflow implementation

**Red Flags:**
- Cannot explain `_inherit` vs `_inherits`
- Doesn't understand when to use `@api.depends` vs `@api.onchange`
- No experience with method overriding (create, write, unlink)
- Cannot implement One2many/Many2many correctly

**Green Flags:**
- Has built complete modules with workflows
- Can override ORM methods properly
- Understands computed field dependencies
- Experience with transient models (wizards)
- Knows how to use sequences and data files

---

#### 🔴 For Expert Candidates (Modules 9-11):
**Focus Areas:**
- Architecture and design patterns
- Performance optimization experience
- Integration and API expertise
- Can they lead module design and mentor others?
- Production debugging and troubleshooting skills
- Understanding of deployment and DevOps

**Red Flags:**
- Cannot explain `self.env` and its components
- No experience with constraints or validations
- Doesn't understand security implications of `sudo()`
- Cannot optimize slow queries
- No API integration experience

**Green Flags:**
- Has deployed Odoo to production environments
- Experience with module upgrades and migrations
- Can debug complex issues using logs and profilers
- Built custom APIs and external integrations
- Understands multi-company architecture
- Has contributed to Odoo community or built reusable modules

---

### 📊 Quick Reference: Module to Skills Mapping

| Module | Key Skills | Interview Weight |
|--------|-----------|------------------|
| **Module 1** | Setup, structure, menus | Junior 30% |
| **Module 2** | Models, security basics | Junior 30% |
| **Module 3** | Views, domains, filters | Junior 40% |
| **Module 4** | Tracking, chatter | Mid 10% |
| **Module 5** | Fields, computed, onchange | Mid 25% |
| **Module 6** | Widgets, UI/UX | Mid 15% |
| **Module 7** | Workflows, wizards, data | Mid 25% |
| **Module 8** | Inheritance, ORM methods | Mid 25% |
| **Module 9** | Constraints, environment, advanced | Expert 35% |
| **Module 10** | Reporting, APIs, integration | Expert 35% |
| **Module 11** | Deployment, debugging, optimization | Expert 30% |

---

### 🎯 Interview Process Recommendations

**For Junior Positions:**
1. 15 min: Basic concepts (10-15 questions from Modules 1-3)
2. 30 min: Live coding - Create simple model with view
3. 15 min: Q&A and culture fit

**For Mid-Level Positions:**
1. 20 min: ORM and workflow questions (15-20 questions from Modules 4-8)
2. 45 min: Live coding - Implement wizard or computed field challenge
3. 15 min: Behavioral questions and team fit

**For Expert Positions:**
1. 30 min: Architecture and advanced topics (15-20 questions from Modules 9-11)
2. 60 min: System design - Real-world scenario (e.g., design approval workflow)
3. 30 min: Code review of their previous work or whiteboard API integration
4. 20 min: Leadership and mentoring discussion

---