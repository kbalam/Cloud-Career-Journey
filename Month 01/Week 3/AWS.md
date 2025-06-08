# Week 3 – AWS Progress

## ✅ Topics Covered
- Real-time EC2 usage for automation tasks
- SSH access and terminal-based scripting
- Creating and managing Linux monitoring scripts on EC2
- Scheduling background tasks using `cron` in an EC2 environment

## 🧪 Hands-On
- Launched EC2 instance (Amazon Linux / Ubuntu)
- Connected via SSH using `.pem` key and terminal
- Created `monitor.sh` inside EC2 to capture:
  - `uptime`, `df -h`, `free -m`, `who`
- Used `chmod +x` to make the script executable
- Verified script functionality by executing manually
- Set up a crontab job to run the script every 10 minutes
- Stored output logs in `~/monitor_log.txt` on the EC2 instance
- Transferred logs and script back to local system for GitHub versioning

## 📸 Screenshots
- [EC2 Creation](./screenshots/terminal/EC2.png)
- [EC2 instance monitoring in terminal](./screenshots/terminal/EC2%20Instance.png)
- [EC2 Shell script](./screenshots/terminal/EC2%20Shell%20Script.png)
- [EC2 Log File](./screenshots/terminal/EC2_output_Log.png)
- [Cron job setup inside EC2](./screenshots/terminal/CRON.png)

## 📄 Output
- [EC2 Monitor Log](./output/EC2_monitor_log.txt)

## 🧠 Reflections
- Practicing inside EC2 felt exactly like what cloud engineers do daily
- Using `cron` in a cloud environment shows how background jobs work in real-world apps
- Got more comfortable navigating EC2, SSH, file permissions, and automation workflows
- Plan to explore CloudWatch Agent next to push these logs to AWS for alerting

## 🔗 Resources
- [EC2 Connect & SSH Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html)
- [Linux on EC2 – AWS Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html)
- [Cron on EC2](https://crontab.guru/)
