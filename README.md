### Project Template README: Debug Odoo with Docker in VSCode

#### Overview
This project template facilitates Odoo development using Docker, specifically configured for VSCode IDE. It includes setup instructions and tips for effective debugging using the Odoo IDE extension.

#### VSCode with the following extensions:
   - Odoo IDE
   - Owl Vision
   - Odoo Shortcuts

#### Setup Steps

**Clone the Project**
```bash
git clone https://github.com/teguhteja/docker-odoo-dev.git -b 18
```

**Odoo Framework Integration for Visual Studio Code**
```bash
https://github.com/odoo-ide/vscode-odoo

```

**Python static analysis tool : Odoo Stubs**
```bash
# odoo-stubs18 .gitignore
git clone -b 18.0 https://github.com/odoo-ide/odoo-stubs.git odoo-stubs18
```
pyrightconfig.json
```bash
{
    "stubPath": "./odoo-stubs18/",
    "extraPaths": [
        "./custom-addons/",
    ]
}
```

**Build Docker Image w/ pydevd-odoo debugger**
   ```bash
   https://github.com/odoo-ide/pydevd-odoo
   requirements.txt pydevd-odoo
   docker build -t odoodev:15 .
   ```

**Start Docker Compose**
   ```bash
   docker compose up -d
   ```

**Add Your Addons**
   `custom-addons`
   `docker compose restart odoo-dev`

**Debugging**
   - Set breakpoints in your source code within VSCode.
   - Ensure the debugger is configured to debug external code (`"justMyCode": false` in .vscode/launch.json).
   - Access the Odoo source code from the container:
     ```bash
     ./docker-cp-odoo.sh
     ```
   - Add breakpoints in the Odoo source code.
   - Run the debugger process to start debugging.

#### Troubleshooting Tips

**Copying misc.py in odoodev**
   If backup failures occur with Docker images, modify `misc.py` to resolve issues.

**Debugging Odoo Source Code**
   Modify `"justMyCode": false` in `launch.json`, 
   download the Odoo folder from the container using `docker-cp-odoo.sh`,
   uncomment this line in docker-compose.yml
   `- ./odoo:/usr/lib/python3/dist-packages/odoo` 
   restart stack or docker compose
   add breakpoints, and start the debugger process .

#### Conclusion
This README provides detailed steps to set up an Odoo development environment using Docker and VSCode, enabling efficient debugging of Odoo applications. For further details, refer to the full documentation and scripts available in the project repository.

---

For detailed scripts and further instructions, visit [docker-odoo-dev](https://github.com/teguhteja/docker-odoo-dev.git).