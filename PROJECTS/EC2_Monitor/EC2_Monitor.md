# EC2Monitor – EC2 Health Monitoring & Alerting Pipeline

## 📄 Project Overview

`EC2Monitor` is a real-time EC2 system health monitoring project that uses **both custom Bash scripts and CloudWatch Agent** to demonstrate a complete and layered monitoring solution. It simulates how real-world production monitoring pipelines work, showcasing:
- **Script-based custom metric collection and push** using AWS CLI
- **CloudWatch Agent-based system metric collection**
- **Log streaming to CloudWatch Logs** via CloudWatch Agent

This hybrid method highlights practical knowledge of AWS monitoring, metric pipelines, log analytics, and alerting — all while remaining within AWS Free Tier limits.

---

## 📊 Features
- Real-time metric collection via Bash script (`ec2_monitor.sh`)
- Metric validation and custom push to CloudWatch using AWS CLI (`send_extract_metric.sh`)
- CloudWatch Agent pushes system-level metrics (e.g., cpu idle percent)
- CloudWatch Agent streams `metrics_output_log.txt` (push logs) to CloudWatch Logs
- CloudWatch Log Group and Log Insights setup for analysis
- CloudWatch Alarms with SNS alerts for threshold breaches
- Fully Free Tier compliant (4 out of 10 custom metrics used)

---

## 🖼️ Architecture Diagram

![Diagram](./EC2%20Diagram.png)

``` bash 
EC2_Instance
├── ec2_monitor.sh (cron: every 5 min)
│   ├── Collects CPU, memory, process count, etc.
│   └── Logs to monitor_log.txt
│
├── send_extract_metric.sh (cron: every 5–6 min)
│   ├── Reads from monitor_log.txt
│   ├── Validates + pushes Process_Count to CloudWatch
│   └── Logs status to metrics_output_log.txt
│
└── CloudWatch Agent
    ├── Pushes system metrics (e.g., mem_used_percent)
    └── Streams metrics_output_log.txt to CloudWatch Logs
```
---

## 🗂️ Project Structure
``` bash
Projects/
└── EC2Monitor/
├── scripts/
│ ├── ec2_monitor.sh
│ └── send_extract_metric.sh
├── output/
│ ├── monitor_log.txt
│ ├── metrics_output_log.txt
├── screenshots/...
└── README.md
```
---
## 🛠️ Scripts Description

### `ec2_monitor.sh`
- Runs every 5 minutes via cron
- Collects:
  - CPU usage
  - Memory statistics
  - Disk usage
  - System uptime
  - Logged-in users
  - Total process count
  - Top CPU and memory consuming processes
- Logs everything to `monitor_log.txt`

### `send_extract_metric.sh`
- Runs 30–60 seconds after the monitor script
- Extracts latest `Process_Count` from `monitor_log.txt`
- Validates value (ensures numeric)
- Pushes metric to CloudWatch via `aws cloudwatch put-metric-data`
- Logs status/output to `metrics_output_log.txt`

---

## 🧠 CloudWatch Agent Role
- Streams log file: `metrics_output_log.txt` to CloudWatch Logs
- Pushes internal system metrics like:
  - `cpu_usage_idle`
  - Disk I/O
  - CPU stats
- All logs go to: `EC2MonitorLogs` log group (or your chosen group)

---

## 🚨 CloudWatch Alarms

| Metric Name       | Source             | Threshold | Alarm Action   |
|-------------------|--------------------|-----------|----------------|
| `Process_Count`    | send_extract_metric.sh | > 109     | SNS email       |
| `cpu_usage_idle` | CloudWatch Agent   | < 80%     | SNS email       |

---

## 🔍 Log Insights Query (Example)

```sql
fields @timestamp, @message
| parse @message "Pushed process count '*'" as processCount
| stats avg(processCount) as AvgProcessCount, max(processCount) as MaxProcessCount, min(processCount) as MinProcessCount by bin(5m)
| sort @timestamp desc

---

## 📈 Metrics Used

| Metric Name       | Source               | Description                             |
|-------------------|----------------------|-----------------------------------------|
| `Process_Count`   | Bash Script          | Custom number of running processes      |
| `mem_used_percent`| CloudWatch Agent     | Memory usage percent (system-level)     |
| `CPU_usage_idle`  | CloudWatch Agent     | Real-time CPU tracking                  |
| `LoggedIn_Users`  | Optional via script  | Logged-in user count                    |

---

## 🔐 IAM Role Required

Your EC2 instance must use an IAM Role with the following policy:

- `CloudWatchAgentServerPolicy`

**(Optional)** Add the following if using **SSM Session Manager**:

- `AmazonSSMManagedInstanceCore`

---

## 🧰 Technologies Used

- **Amazon EC2** (Amazon Linux 2)
- **Amazon CloudWatch** (Metrics, Logs, Alarms, Insights)
- **Amazon SNS** (for alerts)
- **AWS CLI**
- **CloudWatch Agent**
- **Bash Scripting**
- **Crontab** (automation)

---

## ✅ Why This Project Stands Out

- Combines both agent-based and script-based monitoring
- Validates and pushes custom metrics not available by default
- Demonstrates log streaming, filtering, and alarm automation
- Reflects practical DevOps and Cloud Support workflows
- Entire setup runs within **AWS Free Tier** limits

---

## 📂 Scripts

[Monitor.sh](./Scripts/ec2_monitor.sh) – Collects system metrics every 5 minutes

[Send_Extract_Metric](./Scripts/send_extract_metric.sh) – Extracts and pushes metric to CloudWatch


## 📁 Output Logs

[Monitor_log.txt](./Outputs/monitor_log.txt) – Full system metric logs from monitor script

[Metrics_output_log.txt](./Outputs/metrics_output_log.txt) – Push result logs (used by agent)


## 🖼️ Screenshots - Visual Proof

[Metric Creation](./Screenshots/Metric%20Namespaces.png)
[CPU Metric Graph](./Screenshots/CPU%20Metric%20Graph.png)
[Process Count Graph](./Screenshots/Process%20Count%20Graph.png)
[Alarm Creation](./Screenshots/Alarm.png)
[Log Groups](./Screenshots/Log%20Groups.png)
[Agent Log Files](./Screenshots/Agent%20Logs.png)
[Script Log Files](./Screenshots/Script_Logs.png)
[Log Insights](./Screenshots/Log%20Insights.png)
[CPU SNS Notifcation](./Screenshots/CPU%20Notification.png)
[Process Count SNS](./Screenshots/Process%20Notification.png)

---

## 🧾 Conclusion

This **EC2Monitor** project is a showcase of **hybrid monitoring**, combining **CloudWatch Agent** with manual **AWS CLI scripts** to achieve a full EC2 health pipeline. It reflects solid hands-on skills in:

- EC2 operations  
- AWS monitoring  
- CLI automation  
- Logging and alerting

✅ Exactly the kind of solution used in **real production environments**.
