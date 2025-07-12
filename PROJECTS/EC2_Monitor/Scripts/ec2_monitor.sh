#!/bin/bash

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo ==========TIME: $TIMESTAMP ============
echo =================================LOGGEDIN_USERS========================================================
who
echo =================================SYSTEM_UPTIME=========================================================
uptime -p
echo =================================CPU==================================================================
CPU_Usage=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8 "%"}')
echo CPU_Usage = $CPU_Usage
echo =================================MEMORY===============================================================
Memory_Usage=$(free -m | awk '/^Mem:/ {print "Used: " $3 "MB", "Free:" $4 "MB", "Available: " $7 "MB"}')
echo Memory_Usage = $Memory_Usage
echo =================================DISK=================================================================
df -h /
echo =================================LOAD_AVERAGE=========================================================
uptime
echo =================================RUNNING_PROCESS======================================================
echo "> Top 5 CPU-using processes:"
ps aux --sort=-%cpu | head -n 6

echo "> Top 5 Memory-using processes:"
ps aux --sort=-%mem | head -n 6

process=$(ps aux | wc -l)
echo "> Total number of processes:" $process
echo ======================================================================================================
