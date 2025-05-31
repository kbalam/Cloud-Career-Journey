# Week 2 – Linux Progress

## ✅ Topics Covered
- Using `sudo`, `apt`, and basic Linux administration
- File and directory permissions (`chmod`, `chown`, `chgrp`)
- User and group management: `useradd`, `usermod`, `userdel`, groups
- Login monitoring tools: `whoami`, `who`, `id`, `w`, `uptime`, `last`
- Special permissions: SUID, SGID, Sticky Bit
- Umask and permission defaults
- File attributes: `lsattr`, `chattr`
- Cron jobs and scheduling scripts
- Bash scripting: `#!/bin/bash`, variables, `echo`

## 🧪 Hands-On
- Created users and groups using `useradd` and `groupadd`
- Modified and deleted users with `usermod` and `userdel`
- Tested file permissions with `chmod`, octal notation, directory restrictions
- Used `find` to locate and change permissions recursively
- Explored `passwd` and `shadow` files for account control
- Wrote and executed a shell script to print system info (date, uptime, user)
- Scheduled the script with `crontab` to run every 5 minutes

## 📸 Screenshots
- [Bash Script](./screenshots/Terminal%20Screenshots/script.png)
- [Crontab](./screenshots/Terminal%20Screenshots/crontab.png)
- [Script running via cron](./screenshots/Terminal%20Screenshots/cron-job-running.png)

## 🧠 Reflections
- Learned how Linux uses layered security via file permissions and special bits
- Understood how automation through cron simplifies monitoring
- SUID and Sticky Bit were tricky at first but make sense with hands-on testing
- `lsattr` and `chattr` were new but useful for locking important files

## 🔗 Resources
- [Linux File Permissions Explained](https://www.redhat.com/sysadmin/linux-file-permissions)
- [Cron Syntax Guide](https://crontab.guru/)
- [Bash Scripting Basics](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
- [User Management in Linux](https://www.geeksforgeeks.org/user-management-in-linux/)
