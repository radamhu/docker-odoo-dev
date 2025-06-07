# Overview
This project template facilitates Odoo development using Docker, specifically configured for VSCode IDE. It includes setup instructions and tips for effective debugging using the Odoo IDE extension.

## Setup development environment
### Prerequisites

**Clone the Project**
```bash
git clone https://github.com/teguhteja/docker-odoo-dev.git -b 15
readme.excalidraw
readme.plantuml
.gitignore
.dockerignore
pyenv install 3.9.18
pyenv versions
pyenv local 3.9.18 # .python-version
# direnv, echo 'eval "$(direnv hook bash)"' >> ~/.zshrc
echo 'layout pyenv 3.9.18' > .envrc
direnv allow
source .direnv/python-3.9.18/bin/activate
# THIS doesnt need if .envrc/direnv is used
# python -m venv .venv 
# source .venv/bin/activate
pip install -r requirements.txt 
touch .env
GH action https://github.com/python-semantic-release/python-semantic-release
GH readme.md https://github.com/othneildrew/Best-README-Template

```

**VSCode with the following extensions**
   - Odoo IDE
   - Owl Vision
   - Odoo Shortcuts

**Odoo Framework Integration for Visual Studio Code**
```bash
https://github.com/odoo-ide/vscode-odoo
```

**Python static analysis tool : Odoo Stubs**
```bash
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

**Build Docker Image w/ pydevd-odoo debugger**
   ```bash
   https://github.com/odoo-ide/pydevd-odoo
   requirements.txt pydevd-odoo
   in Dockerfile
   - change image sourceand version based on which paltform you are developing
      arm macos -->FROM wbms/odoo-15.0
      arm macos -->FROM arm64v8/odoo:15.0
      x86 --> FROM odoo:15
   docker build --platform linux/arm64/v8,linux/amd64 -t odoodev:15 .
   ```

**Start Docker Compose**
   ```bash
   in docker-compose.yml
   - change version related parameters 
   --> platform: linux/amd64
   docker compose up -d
   ```

**Add Your Addons**
   - Create a directory for your custom addons:
     ```bash
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

## 📌 Overview

- **Total Duration:** ~15 hours
- **Learning Mode:** Self-paced (1–2 hours per day)
- **Start Date:** 2025-06-06
- **Goal:** Gain practical experience in Odoo development and understand how to build and customize ERP modules.

---

## 🧭 Syllabus Overview: Odoo 15 Development Tutorials

### **⏱️ Study Plan: 1–2 Hours Daily**
Assuming a daily commitment of 1–2 hours, here's an estimated schedule:

Week 1:
- Day 1: Module 1
- Day 2–3: Module 2
- Day 4–5: Module 3

Week 2:
- Day 6–7: Module 4
- Day 8: Module 5
- Day 9: Module 6
- Day 10–11: Module 7

This plan spans approximately 11 days, allowing for flexibility and review sessions.

### **Module 1: Introduction to Odoo Development**
- Setting up the Odoo development environment
- Creating a new module
- Understanding module structure
- Videos: 1–5
- ⏱️ **Estimated Time:** 1.5 hours

### **Module 2: Models and Fields**
- Defining models and adding field types
- Understanding field attributes
- Custom data structures in Odoo
- Videos: 6–15
- ⏱️ **Estimated Time:** 2 hours

### **Module 3: Views and User Interface**
- Creating form, tree, and kanban views
- Menu items, actions, and UI customization
- Working with XML views
- Videos: 16–25
- ⏱️ **Estimated Time:** 2 hours

### **Module 4: Business Logic and ORM**
- Writing business logic in Python
- Using Odoo ORM methods (`create`, `write`, `unlink`, `search`)
- Compute fields, decorators, and onchange methods
- Videos: 26–35
- ⏱️ **Estimated Time:** 2 hours

### **Module 5: Security and Access Control**
- Managing user roles and groups
- Access control lists and record rules
- Safeguarding business data
- Videos: 36–40
- ⏱️ **Estimated Time:** 1.5 hours

### **Module 6: Reporting and QWeb**
- Creating reports using QWeb
- Report templates and actions
- PDF report generation
- videos: 41–45
- ⏱️ **Estimated Time:** 1.5 hours

### **Module 7: Advanced Topics**
- Inheriting and extending core modules
- Working with APIs
- Deploying and maintaining custom modules
- videos: 46–60
- ⏱️ **Estimated Time:** 4.5 hours

---

## 🗓️ Study Plan

| Date       | Module                         | Status       |
|------------|--------------------------------|--------------|
| 2025-06-06 | Module 1: Intro to Odoo        | ✅ Completed |
| 2025-06-07 | Module 2: Models and Fields    | ✅ Completed |
| 2025-06-08 | Module 3: Views & UI           | ✅ Completed |
| 2025-06-09 | Module 4: Business Logic/ORM   | ✅ Completed |
| 2025-06-10 | Module 5: Security & Access    | ✅ Completed |
| 2025-06-11 | Module 6: Reporting & QWeb     | ✅ Completed |
| 2025-06-12 | Module 7: Advanced Topics      | ✅ Completed |

---

## 📝 Notes

- **Module 1:** Set up dev environment, created a basic Odoo module.
- **Module 2:** Defined fields and models using `fields.Char`, `fields.Many2one`, etc.
- **Module 3:** Created tree/form views and customized the UI.
- **Module 4:** Used `@api.depends`, `@api.onchange`, and ORM methods.
- **Module 5:** Explored security through `ir.model.access.csv` and record rules.
- **Module 6:** Created custom PDF reports and learned about QWeb templates.
- **Module 7:** Learned to override core modules and prepare for deployment.

---

## 📂 Resources

- 📺 [YouTube Playlist](https://www.youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU)
- 📖 [Odoo 15 Official Docs](https://www.odoo.com/documentation/15.0/)
- 🛠️ [Odoo Developer Reference](https://www.odoo.com/documentation/15.0/developer.html)

---

## ✅ Conclusion

This structured journey through the Odoo 15 framework provided hands-on development skills aligned with ERP customization, security, and deployment. As a DevOps Python developer, this knowledge bridges backend automation with ERP system architecture — enabling contributions to business operations at scale.

