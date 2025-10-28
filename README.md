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
   - Expected: Understanding of ERP, mention of Sales, CRM, Inventory, Accounting
   
2. **Explain the structure of an Odoo module.** *(Module 1)*
   - Expected: `__manifest__.py`, models, views, security folders, data files

3. **What is the purpose of `__manifest__.py`?** *(Module 1)*
   - Expected: Module metadata, dependencies, data files to load, version info

4. **How do you add a menu item in Odoo?** *(Module 1)*
   - Expected: Define `<menuitem>` in XML with action, parent, sequence

#### Module 2: Models & Security
5. **How do you create a new field in an Odoo model?** *(Module 2)*
   - Expected: Use Fields class (Char, Integer, Many2one, etc.) in models

6. **What are the basic field types in Odoo?** *(Module 2)*
   - Expected: Char, Text, Integer, Float, Boolean, Date, Datetime, Selection

7. **What is `ir.model.access.csv` used for?** *(Module 2)*
   - Expected: Access control list - defines which groups can read/write/create/delete records

8. **Write a simple model with name, description, and date fields.** *(Module 2)*
   - Expected: Class inheriting `models.Model`, proper field definitions

#### Module 3: Views & Basic Operations
9. **Explain the difference between `tree` and `form` views.** *(Module 3)*
   - Expected: Tree = list view, Form = detailed single record view

10. **What is the difference between `active=True` and `active=False` in records?** *(Module 3)*
    - Expected: Archiving mechanism - inactive records are hidden by default

11. **How do you set a default value for a field?** *(Module 3)*
    - Expected: Use `default=` parameter or `default_get()` method

12. **What is a domain in Odoo? Give examples.** *(Module 3)*
    - Expected: Filter criteria `[('field', 'operator', 'value')]`

13. **How would you make a field required?** *(Module 3)*
    - Expected: `required=True` parameter

14. **How do you add filters and group by options in search views?** *(Module 3)*
    - Expected: `<filter>` tags in search view with domain or context for grouping

15. **What does context do when opening a view?** *(Module 3)*
    - Expected: Pass default values, hide/show fields, activate filters

---

### 🟡 Mid Level (1-3 years experience)
*Advanced topics covered in Modules 4-8*

#### Module 4: Communication & Tracking
16. **How do you add tracking to a field (chatter)?** *(Module 4)*
    - Expected: Inherit `mail.thread`, add `tracking=True` to field

17. **What is the purpose of the search panel?** *(Module 4)*
    - Expected: Quick filtering sidebar for categories/tags, improves UX

18. **How do you enable chatter (mail thread) in a model?** *(Module 4)*
    - Expected: Inherit `mail.thread`, `mail.activity.mixin`, add to view

#### Module 5: Fields Deep Dive
19. **Explain Many2one, One2many, and Many2many relationships.** *(Module 5)*
    - Expected: Foreign key, reverse relation, junction table concepts

20. **What are computed fields? How do you create one?** *(Module 5)*
    - Expected: Fields calculated from other fields, use `@api.depends` decorator

21. **Explain the `@api.onchange` decorator.** *(Module 5)*
    - Expected: Triggers when field changes in UI, updates other fields dynamically

22. **What does `_rec_name` do in a model?** *(Module 5)*
    - Expected: Specifies which field to use as display name in Many2one relations

23. **What is a related field and when would you use it?** *(Module 5)*
    - Expected: Shortcut to access related record's field, use `related=` parameter

24. **How do you add an image field to a model?** *(Module 5)*
    - Expected: Use `fields.Image` or `fields.Binary`, display with image widget

#### Module 6: Widgets & Decorations
25. **Explain widgets in Odoo. Name at least 5.** *(Module 6)*
    - Expected: statusbar, priority, badge, image, many2many_tags, handle, color, etc.

26. **How do you add a button in a form view that triggers a Python method?** *(Module 6)*
    - Expected: `<button>` tag with `type="object"` and `name="method_name"`

27. **What is the purpose of `attrs` in view definitions?** *(Module 6)*
    - Expected: Dynamic visibility/readonly/required based on conditions

28. **How do you implement a statusbar widget?** *(Module 6)*
    - Expected: Selection field with `statusbar` widget, define clickable states

29. **What are decorations in tree views?** *(Module 6)*
    - Expected: Apply colors/styles based on conditions (decoration-success, decoration-danger)

30. **How do you add a confirmation dialog to a button?** *(Module 6)*
    - Expected: Use `confirm="message"` attribute in button tag

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