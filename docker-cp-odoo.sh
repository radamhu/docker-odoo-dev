docker exec o14 sh -c 'zip -r odoo.zip /usr/lib/python3/dist-packages/odoo'
docker cp o14:/odoo.zip ./odoo.zip
unzip odoo.zip
mv usr/lib/python3/dist-packages/odoo/ .
rm -r usr
rm -r odoo.zip