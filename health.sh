#!/data/data/com.termux/files/usr/bin/bash

# --- Automated System Health Report ---

echo "=========================================="
echo "          📱 SYSTEM HEALTH REPORT          "
echo "=========================================="
echo ""

# 1. CPU and Load (Basic Check)
echo "--- 📊 CPU & MEMORY LOAD (via htop data) ---"
# Check Load Average
echo "Load Average: (Requires htop to view interactively)"
echo "Tasks: $(ps | wc -l) running processes."
echo ""

# 2. Memory Availability (Most Critical Metric)
echo "--- 🧠 MEMORY AVAILABILITY ---"
# Grab the MemAvailable line and format it
MEM_AVAIL=$(cat /proc/meminfo | grep MemAvailable | awk '{print $2/1024/1024 " GB"}')
echo "Memory Available (for new apps): $MEM_AVAIL"
echo "------------------------------------------"

# 3. Storage Health
echo "--- 💾 STORAGE USAGE (Internal Storage) ---"
# Find the line corresponding to your main storage (/storage/emulated) and display relevant columns
df -h | grep /storage/emulated | awk '{print "Size: " $2 "\nUsed: " $3 " (" $5 ")\nFree: " $4}'
echo "=========================================="
