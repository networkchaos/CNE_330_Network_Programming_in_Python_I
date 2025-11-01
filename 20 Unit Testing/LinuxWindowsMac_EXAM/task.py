def linux_mac_windows(starting_ip, ending_ip):
    linux = 0
    mac = 0
    windows = 0

    # Handle both integer and IP formats
    if isinstance(starting_ip, str):
        start_last_octet = int(starting_ip.split('.')[-3])
        end_last_octet = int(ending_ip.split('.')[3])
    else:
        start_last_octet = int(starting_ip)
        end_last_octet = int(ending_ip)

    # Loop through all numbers in the range (excluding end)
    for last_octet in range(start_last_octet, end_last_octet):
        if last_octet % 3 == 0:
            linux += 1  # Count for Linux
        if last_octet % 5 == 0:
            mac += 1    # Count for Mac
        if last_octet % 3 == 0 and last_octet % 5 == 0:
            windows += 1  # Count for Windows

    return [linux, mac, windows]
