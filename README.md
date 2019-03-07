**Filemover**

Async filemover for Linux.
Sorts files to dirs and works like a daemon.

**Open file**

````
sudo nano /etc/systemd/system/filemover.service
````
**Add this**
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