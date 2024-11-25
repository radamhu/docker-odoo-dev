FROM odoo:18

# Switch to root for installing system dependencies
USER root

# Install dependencies
RUN apt update && \ 
    apt install -y --no-install-recommends \
    python3-dev \
    build-essential \
    libffi-dev \
    libssl-dev \
    cargo \
    zip \
    wget \
    python3-debugpy \
    python3-pydevd \
 && rm -rf /var/lib/apt/lists/*  # Clean up APT cache to reduce image size

# Optional: Modify Odoo source files (uncomment if needed)
# COPY ./misc.py /usr/lib/python3/dist-packages/odoo/tools/misc.py

# Switch back to the odoo user
USER odoo
