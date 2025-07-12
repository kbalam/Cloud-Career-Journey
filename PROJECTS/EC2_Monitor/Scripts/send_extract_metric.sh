#!/bin/bash

log_file="/home/ec2-user/EC2_project/metrics_output_log.txt"


# == Getting the value
process_count=$(grep "processes" /home/ec2-user/EC2_project/monitor_log.txt | tail -n 1 | awk '{print $6}')


# Validate value before pushing
if [[ -z "$process_count" || ! "$process_count" =~ ^[0-9]+$ ]]; then
    echo "[$(date)] ERROR: Invalid or missing process count: '$process_count'" >> "$log_file"
    exit 1
fi

# == Pushing to CloudWatch and capturing stderr
error_output=$(aws cloudwatch put-metric-data \
  --namespace "EC2Monitor" \
  --metric-name "Process_Count" \
  --value "$process_count" \
  --unit Count \
  --region ap-south-1 2>&1)

exit_code=$?

# == Logging

if [ $exit_code -eq 0 ]; then
    echo "[$(date)] SUCCESS: Pushed process count '$process_count' to CloudWatch." >> "$log_file"
else
    echo "[$(date)] ERROR: Failed to push process count '$process_count' to CloudWatch." >> "$log_file"
    echo "[$(date)] STDERR: $error_output" >> "$log_file"
fi

