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

# 📚 Odoo 15 Development Study Plan (11 Days)

This plan spans **11 days**, with built-in flexibility for rewatches and reviews.  
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

WEEK

### **Module 5: Fields Deep Dive**
- [x ] Add Many2one fields  
- [x ] Use date & datetime fields  
- [x ] Define related and computed fields  
- [x ] Handle onchange functions  
- [x ] Configure rec name  
- [x ] Add notebooks, HTML fields, and images  
- **Videos:** 20–28  
- ⏱️ **Estimated Time:** ~3.5 hours  

---

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

WEEK

### **Module 7: Workflows & Wizards**
- [ ] Control statusbar using buttons  
- [ ] Enable hotkeys  
- [ ] Work with One2many and Many2many fields  
- [ ] Create and use transient models & wizards  
- [ ] Load data from XML & CSV  
- **Videos:** 44–66  
- ⏱️ **Estimated Time:** ~4.5 hours  

---

### **Module 8: Inheritance & ORM**
- [ ] Inherit models, fields, functions  
- [ ] Override create/write/unlink methods  
- [ ] Work with sequences, default get, name get  
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

