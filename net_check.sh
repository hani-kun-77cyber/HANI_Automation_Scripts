#!/data/data/com.termux/files/usr/bin/bash

# --- Automated Network Stability Monitor ---

# Define the target IP address (Google's reliable DNS server)
TARGET="8.8.8.8"
# Define the file where failures will be recorded
LOG_FILE="network_failures.log"

echo "=========================================="
echo "  🌐 Network Monitor: Pinging $TARGET   "
echo "  Failures will be logged to $LOG_FILE  "
echo "  Press Ctrl + C to stop the monitor.  "
echo "=========================================="

# Start an infinite loop that runs until manually stopped (Ctrl+C)
while true
do
    # 1. Run ping: Send only 1 packet and discard normal output (>/dev/null)
    ping -c 1 $TARGET > /dev/null

    # 2. Check the exit status ($?) of the last command (ping)
    # $? returns 0 for SUCCESS and a non-zero number (usually 1 or 2) for FAILURE.
    if [ $? -ne 0 ]; then
        # Condition: if the status is NOT equal to 0 (ping failed)
        
        # Capture the current date and time
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        
        # Print the alert and append it to the log file (tee -a saves the output)
        echo "🚨 FAILURE detected at: $TIMESTAMP" | tee -a $LOG_FILE
    else
        # Condition: if the status IS 0 (ping succeeded)
        
        # Print a dot to show the script is still running successfully
        echo -n "."
    fi

    # Wait for 5 seconds before repeating the process
    sleep 5

done
