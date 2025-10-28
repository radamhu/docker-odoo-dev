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
- [ ] Add SQL & Python constraints  
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

### 🟢 Junior Level (0-1 years experience)

#### Basic Concepts
1. **What is Odoo and what are its main modules?**
   - Expected: Understanding of ERP, mention of Sales, CRM, Inventory, Accounting
   
2. **Explain the structure of an Odoo module.**
   - Expected: `__manifest__.py`, models, views, security folders, data files

3. **What is the purpose of `__manifest__.py`?**
   - Expected: Module metadata, dependencies, data files to load, version info

4. **How do you create a new field in an Odoo model?**
   - Expected: Use Fields class (Char, Integer, Many2one, etc.) in models

5. **What are the basic field types in Odoo?**
   - Expected: Char, Text, Integer, Float, Boolean, Date, Datetime, Selection

6. **Explain the difference between `tree` and `form` views.**
   - Expected: Tree = list view, Form = detailed single record view

7. **What is `ir.model.access.csv` used for?**
   - Expected: Access control list - defines which groups can read/write/create/delete records

8. **How do you add a menu item in Odoo?**
   - Expected: Define `<menuitem>` in XML with action, parent, sequence

9. **What is the difference between `active=True` and `active=False` in records?**
   - Expected: Archiving mechanism - inactive records are hidden by default

10. **How do you set a default value for a field?**
    - Expected: Use `default=` parameter or `default_get()` method

#### Practical Questions
11. **Write a simple model with name, description, and date fields.**
12. **How would you make a field required?**
    - Expected: `required=True` parameter
    
13. **What does `_rec_name` do in a model?**
    - Expected: Specifies which field to use as display name in Many2one relations

14. **How do you add tracking to a field (chatter)?**
    - Expected: Inherit `mail.thread`, add `tracking=True` to field

15. **What is the purpose of `sequence.xml`?**
    - Expected: Auto-generate unique sequential numbers for records

---

### 🟡 Mid Level (1-3 years experience)

#### ORM & Models
16. **Explain the difference between `_name`, `_inherit`, and `_inherits`.**
    - Expected: `_name` = new model, `_inherit` = extend existing, `_inherits` = delegation inheritance

17. **What are computed fields? How do you create one?**
    - Expected: Fields calculated from other fields, use `@api.depends` decorator

18. **Explain the `@api.onchange` decorator.**
    - Expected: Triggers when field changes in UI, updates other fields dynamically

19. **What ORM methods would you use to:**
    - Create a record?
    - Search for records?
    - Update a record?
    - Delete a record?
    - Expected: `create()`, `search()`, `write()`, `unlink()`

20. **How do you override the `create()` method? Give an example.**
    - Expected: Call `super().create()`, add custom logic before/after

21. **What is the difference between `search()` and `search_read()`?**
    - Expected: `search()` returns recordset, `search_read()` returns list of dicts

22. **Explain Many2one, One2many, and Many2many relationships.**
    - Expected: Foreign key, reverse relation, junction table concepts

23. **What is a domain in Odoo? Give examples.**
    - Expected: Filter criteria `[('field', 'operator', 'value')]`

24. **How do you make a computed field searchable?**
    - Expected: Add `search=` parameter with custom search method

25. **What is `store=True` for computed fields?**
    - Expected: Stores value in DB instead of computing on-the-fly

#### Views & UI
26. **How do you apply a domain to a Many2one field?**
    - Expected: Use `domain=` attribute in field or view

27. **Explain widgets in Odoo. Name at least 5.**
    - Expected: statusbar, priority, badge, image, many2many_tags, handle, color, etc.

28. **How do you add a button in a form view that triggers a Python method?**
    - Expected: `<button>` tag with `type="object"` and `name="method_name"`

29. **What is the purpose of `attrs` in view definitions?**
    - Expected: Dynamic visibility/readonly/required based on conditions

30. **How do you create a wizard (TransientModel)?**
    - Expected: Inherit `models.TransientModel`, create view, link with action

#### Security & Data
31. **Explain the difference between access rights and record rules.**
    - Expected: Access = model-level CRUD, Record rules = row-level filters

32. **How do you load initial data into Odoo?**
    - Expected: XML/CSV files in `data/` folder, referenced in manifest

33. **What is `noupdate="1"` in data files?**
    - Expected: Prevents Odoo from updating the record on module upgrade

34. **How do you handle translations in Odoo?**
    - Expected: `_()` function for strings, PO files, translate=True for fields

35. **What is the purpose of `groups_id` in field definitions?**
    - Expected: Field-level security - show only to specific user groups

#### Practical Scenarios
36. **Create a computed field that calculates total from line items.**
37. **Write a domain that shows only active records created this year.**
38. **How would you prevent deletion of records in certain states?**
    - Expected: Override `unlink()` method, raise ValidationError

39. **Implement a Python constraint that ensures email is unique.**
40. **Create an onchange that auto-fills city based on zip code.**

---

### 🔴 Expert Level (3+ years experience)

#### Advanced ORM & Architecture
41. **Explain the Odoo environment (`self.env`). What can you access through it?**
    - Expected: `env.user`, `env.company`, `env.cr` (cursor), `env.context`, `env.ref()`

42. **What is the difference between `self.env.cr.execute()` and ORM methods?**
    - Expected: Raw SQL vs ORM (security, caching, access rights differences)

43. **When and why would you use `sudo()`?**
    - Expected: Bypass access rights, admin-level operations, security implications

44. **Explain `with_context()` and `with_company()`.**
    - Expected: Temporary context modification, multi-company scenarios

45. **How does Odoo handle multi-company architecture?**
    - Expected: `company_id` field, record rules, security models

46. **What are the performance implications of stored vs non-stored computed fields?**
    - Expected: DB space vs computation time, cache, dependencies

47. **Explain the `@api.model` decorator.**
    - Expected: Class-level method, no recordset (similar to classmethod)

48. **How do you handle circular dependencies in computed fields?**
    - Expected: Careful `@api.depends` design, inverse functions, avoid recursion

49. **What is the purpose of `_sql_constraints`?**
    - Expected: Database-level constraints (UNIQUE, CHECK), faster than Python

50. **Explain method resolution order (MRO) in Odoo inheritance.**
    - Expected: Multiple inheritance chain, how Odoo resolves conflicts

#### Advanced Views & Frontend
51. **How do you create a custom widget in Odoo?**
    - Expected: JavaScript widget registration, template, CSS (mention OWL for 16+)

52. **Explain QWeb and its use cases.**
    - Expected: Templating engine for reports, website, views

53. **How do you pass data from Python to JavaScript?**
    - Expected: Context, widget props, JSON endpoints

54. **What is the difference between OWL v1 and v2?**
    - Expected: Component lifecycle, reactivity, hooks (Odoo 16 vs 17+)

55. **How do you debug JavaScript issues in Odoo?**
    - Expected: Browser console, asset debug mode, source maps

56. **Explain how asset bundles work in Odoo.**
    - Expected: Asset XML declarations, JS/CSS compilation, lazy loading

#### Integration & APIs
57. **How do you create a custom REST API endpoint in Odoo?**
    - Expected: Controller class, `@http.route`, JSON responses, authentication

58. **Explain XMLRPC vs JSONRPC in Odoo.**
    - Expected: External API protocols, use cases, authentication methods

59. **How would you integrate Odoo with an external service (e.g., payment gateway)?**
    - Expected: API calls, webhooks, scheduled actions, error handling

60. **What are the security considerations for external API integration?**
    - Expected: API keys, CORS, rate limiting, input validation

#### Reporting & Advanced Features
61. **How do you create a custom PDF report with dynamic content?**
    - Expected: QWeb template, report action, Python report class

62. **Explain how to add a pivot/graph view to a model.**
    - Expected: `<graph>` and `<pivot>` view types, measure fields, grouping

63. **How do you generate Excel reports from Odoo?**
    - Expected: `xlsxwriter` library, AbstractModel inheritance, download action

64. **What is the purpose of `search_default_` in context?**
    - Expected: Auto-activate search filters when view opens

#### Performance & Optimization
65. **How do you optimize a slow Odoo query?**
    - Expected: Indexes, reduce computed fields, prefetch, `read_group()`, SQL explain

66. **Explain prefetching in Odoo ORM.**
    - Expected: Batch loading of related records to reduce queries

67. **What are workers in Odoo? When do you need them?**
    - Expected: Multiprocessing, concurrent requests, long-running tasks

68. **How do you profile Odoo performance issues?**
    - Expected: `--log-level=debug`, Python profilers, query logs, Odoo profiler

69. **What is `@api.depends_context` and when would you use it?**
    - Expected: Computed field depends on context values (company, lang, etc.)

#### Deployment & DevOps
70. **Explain the Odoo module upgrade process.**
    - Expected: `-u module_name`, migration scripts, version in manifest

71. **How do you handle database migrations in Odoo?**
    - Expected: `pre.py` and `post.py` migration scripts in `migrations/` folder

72. **What are the best practices for Odoo module development?**
    - Expected: Small commits, testing, linting, documentation, version control

73. **How do you debug Odoo in a Docker container?**
    - Expected: Remote debugging, pydevd-odoo, port mapping, attach to process

74. **Explain the purpose of `--workers`, `--max-cron-threads`, and `--limit-time-cpu`.**
    - Expected: Concurrency control, resource limits, production configuration

#### Real-World Scenarios
75. **Design a multi-step approval workflow for purchase orders.**
    - Expected: State field, buttons, groups, email notifications

76. **How would you implement a custom pricing rule engine?**
    - Expected: Pricelist inheritance, computed fields, onchange logic

77. **Design a system to sync Odoo inventory with an external warehouse.**
    - Expected: Scheduled actions, API integration, error handling, logging

78. **How do you handle large data imports (100k+ records)?**
    - Expected: Batch processing, `load()` method, disable tracking, SQL bulk insert

79. **Implement a custom field that behaves differently for different user groups.**
    - Expected: Computed fields with `env.user` checks, attrs in views

80. **Design a reporting dashboard with real-time data.**
    - Expected: Custom controllers, JS widgets, websockets (advanced), caching

---

### 💡 Behavioral & Situational Questions (All Levels)

81. **Describe a challenging Odoo customization you implemented.**
82. **How do you approach debugging a production issue in Odoo?**
83. **What's your experience with Odoo upgrades (e.g., 13 → 15 → 17)?**
84. **How do you stay updated with Odoo developments?**
85. **Explain a situation where you had to optimize slow Odoo performance.**
86. **How do you handle conflicting requirements from business users?**
87. **What's your testing strategy for Odoo modules?**
88. **Describe your experience with Odoo community vs Enterprise.**
89. **How do you document your Odoo customizations?**
90. **What would you do if a module upgrade breaks existing functionality?**

---

### 📝 Coding Challenges

#### Junior
- Create a simple library management module (books, authors, members)
- Add a wizard to cancel appointments with a reason

#### Mid
- Implement a discount calculation system with multiple rules
- Create a custom report showing monthly sales by product category
- Build a workflow with 3 states and proper transitions

#### Expert
- Design a multi-tenant Odoo system with data isolation
- Implement a custom inventory reservation system
- Create a real-time notification system for stock alerts
- Build a custom dashboard with charts and KPIs

---

### 🎓 Assessment Tips

**For Junior candidates:**
- Focus on understanding basics: models, views, fields
- Can they navigate Odoo UI and create simple modules?
- Do they understand the MVC pattern in Odoo context?

**For Mid-level candidates:**
- Test ORM knowledge deeply
- Can they solve real business logic problems?
- Do they understand performance implications?
- Can they work independently on feature development?

**For Expert candidates:**
- Architecture and design patterns
- Performance optimization experience
- Integration and API expertise
- Can they lead module design and mentor others?
- Production debugging and troubleshooting skills

---