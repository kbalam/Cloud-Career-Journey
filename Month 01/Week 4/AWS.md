# Week 4 – AWS Progress

## ✅ Topics Covered
- CloudWatch Logs: log groups, log streams, retention
- Using `put-log-events` to send test logs via CLI
- Installing and configuring CloudWatch Agent on EC2
- Creating and testing CloudWatch Alarms on custom metrics
- Automating metric push from EC2 using Bash + cron
- Querying log data using CloudWatch Log Insights

---

## 🧪 Hands-On

- Created CloudWatch log group via Console + CLI
- Sent manual log events using `put-log-events`
- Installed and configured CloudWatch Agent on EC2
- Created custom metrics using `put-metric-data`
- Triggered alarms on thresholds like `CPU > 70`
- Wrote `metric.sh` and scheduled it with cron
- Ran Log Insights queries for filtering logs and extracting fields

---

## 📁 Outputs
- [Log events](./output/Log%20events.png)
- [Log Group](./output/Log%20group.png)
- [Metric creation](./output/Metrics%20creation.png)
- [Metrics Graph](./output/Metrics.png)

---

## Scripts
- [CloudWatch Agent Config file](./script/config.json)
- [Manual Logs from CLI](./script/manualLogs.txt)
- [Uploading metrics using metric.sh](./script/shell%20script.png)
- [Automation using cron](./script/cron%20setup.png)

---

## 📸 Screenshots
- [Creating Log Group](./screenshots/CLI/Creating%20Log%20group.png)
- [Logging Events](./screenshots/CLI/Log%20events.png)
- [Cloudwatch Agent Installation](./screenshots/CLI/Cloudwatch%20Agent.png)
- [Cloudwatch Agent Activation](./screenshots/CLI/Cloudwatch%20Agent.png)
- [Pushing Metrics](./screenshots/CLI/Uploading%20custom%20metrics.png)
- [Alarm Dashboard](./screenshots/Alarm%20creation.png)
- [Alarm Graph](./screenshots/Alarm.png)
- [Cloudwatch Insights](./screenshots/Cloudwatch%20Insights.png)
- [Running Query](./screenshots/Running%20%20query.png)

---

## 🧠 Reflections
- Learned how to build a lightweight monitoring pipeline
- Understood how logs and metrics flow inside AWS
- Gained hands-on experience with both CLI and agent-based monitoring
- First exposure to writing metric-driven automation scripts from EC2
- Log Insights gave deeper visibility into raw logs and patterns

---

## 🔗 Resources
- [CloudWatch Logs CLI](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html)
- [CloudWatch Agent Setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent.html)
- [Put Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [Log Insights Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
