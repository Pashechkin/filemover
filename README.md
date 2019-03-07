**Filemover**

Async filemover for Linux.
Sorts files to dirs and works like a daemon.

**Add to ```/etc/systemd```**

````
sudo nano /etc/systemd/system/filemover.service
````
**Add to ```/etc/systemd/system/{filename}.service```**:
```
[Unit]

Description=FileMover

After=syslog.target

After=dir.target

[Service]

Type=simple

User=pavel

ExecStart=/usr/bin/python /home/{user}/todaemon/filemover.py

Restart=always

[Install]

WantedBy=multi-user.target
```

**Enable and run**
````
sudo systemctl enable filemover.service

sudo systemctl start filemover.service
````

Done!