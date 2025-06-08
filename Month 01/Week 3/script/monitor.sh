#!/bin/bash
  2 
  3 echo "=========================================$(date)=====================================================" >> Documents/monitor_log.txt
  4 uname >> Documents/monitor_log.txt
  5 echo "==============================================================================================" >> Documents/monitor_log.txt
  6 who >> Documents/monitor_log.txt
  7 echo "==============================================================================================" >> Documents/monitor_log.txt
  8 df -h >> Documents/monitor_log.txt
  9 echo "==============================================================================================" >> Documents/monitor_log.txt
 10 lscpu >> Documents/monitor_log.txt
 11 echo "==============================================================================================" >> Documents/monitor_log.txt
 12 uptime >> Documents/monitor_log.txt
 13 echo "==============================================================================================" >> Documents/monitor_log.txt
 14 free -m >> Documents/monitor_log.txt
 15 echo "==============================================================================================" >> Documents/monitor_log.txt
 16 
