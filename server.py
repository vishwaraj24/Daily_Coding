# Web Server Configuration System

# Tuple - cannot be changed
server_ip = ("192.168.1.10",)

# List - can be changed
allowed_ips = ["192.168.1.2", "192.168.1.3"]


# Function to update allowed IPs
def update_allowed_ips():
    ip = input("Enter new IP address to allow: ")
    allowed_ips.append(ip)
    print("IP added successfully!")


# Display configuration
def display_config():
    print("\n----- Server Configuration -----")
    print("Server IP:", server_ip[0])
    print("Allowed IPs:", allowed_ips)


# Main program
print("Current Configuration:")
display_config()

update_allowed_ips()

print("\nUpdated Configuration:")
display_config()
