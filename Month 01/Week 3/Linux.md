# Week 3 – Linux Progress

## ✅ Topics Covered
- Writing bash scripts to monitor system health
- Commands: `uptime`, `df -h`, `free -m`, `who`
- Automating script execution using `cron`
- Output redirection and log file maintenance

## 🧪 Hands-On
- Created `monitor.sh` script to collect system metrics
- Scheduled it with `crontab` to run every 10 minutes
- Used `>>` to append logs to a file with timestamps

## 📸 Screenshots
- [Cron schedule](./screenshots/cron-monitor-setup.png)
- [Script output in terminal](./screenshots/monitor-script-output.png)

## Scripts
- [Shell Script](./script/monitor.sh)

## 📄 Output
- [Log Ouput](./output/monitor_log.txt)

## 🧠 Reflections
- Writing shell scripts felt more real on EC2
- Learned how cron automates periodic jobs without manual intervention
- Log growth needs to be managed (consider `logrotate` in future)

## 🔗 Resources
- [Linux `cron` Basics](https://opensource.com/article/19/7/introduction-cron)
- [Bash Scripting Tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
