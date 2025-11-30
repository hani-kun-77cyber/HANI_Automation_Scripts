# Import the external library we just installed
import requests 

# --- Website Health Checker ---

print("===================================")
print("🩺 Website Health Checker (HTTP) 🩺")
print("===================================")

# Get the website URL from the user
target_url = input("Enter the full URL (e.g., https://google.com): ")

try:
    # Use the requests library to send an HTTP GET request
    # timeout=5 means the script will give up if it doesn't hear back in 5 seconds
    response = requests.get(target_url, timeout=5)

    # Calculate the time it took to get a response (in seconds)
    response_time = response.elapsed.total_seconds()

    print("\n--- Diagnostic Report ---")
    print(f"Target URL: {target_url}")
    print(f"Status Code: {response.status_code}") # e.g., 200 (Success), 404 (Not Found)
    print(f"Response Time: {response_time:.2f} seconds")

    # Conditional Logic to assess health
    if response.status_code == 200 and response_time < 1.0:
        print("✅ Status: Site is ONLINE and FAST.")
    elif response.status_code == 200:
        print("🟡 Status: Site is ONLINE but SLOW (Time > 1.0s).")
    else:
        print(f"❌ Status: Site is OFFLINE or has an error code ({response.status_code}).")

except requests.exceptions.RequestException as e:
    # This block runs if there's a connection error (e.g., wrong URL format, no internet)
    print(f"\n❌ ERROR: Could not connect to {target_url}.")
    print(f"Reason: {e}")

print("===================================")
