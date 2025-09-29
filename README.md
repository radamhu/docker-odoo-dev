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
- [ ] Explore ORM methods (create, browse, search, etc.)  
- **Videos:** 67–75, 84–85, 98–100  
- ⏱️ **Estimated Time:** ~5 hours  

---

WEEK

### **Module 9: Advanced Features**
- [ ] Apply domains on fields  
- [ ] Raise validation errors  
- [ ] Add SQL & Python constraints  
- [ ] Configure stored/unstored computed fields  
- [ ] Set inverse functions  
- [ ] Use ondelete policies & conditional fields  
- **Videos:** 76–83, 86–96  
- ⏱️ **Estimated Time:** ~4 hours  

---

### **Module 10: Reporting & Integrations**
- [ ] Generate QWeb, PDF, and Excel reports  
- [ ] Add line numbers, barcodes, and QR codes  
- [ ] Work with external API & XMLRPC  
- [ ] Use Postman integration  
- [ ] Implement WhatsApp connector  
- **Videos:** 97, 101–115  
- ⏱️ **Estimated Time:** ~5 hours  

---

DISMISSED

### **Module 11: Deployment & Debugging**
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
- You avoid the soul-crushing repetition of “create a new module” tutorials.