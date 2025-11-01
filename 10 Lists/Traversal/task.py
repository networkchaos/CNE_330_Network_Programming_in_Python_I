def return_all_192_168(ip_address_list):
    # Return all IPs that start with "192.168"
    if ip_address_list is None:
        return []

    result = []
    for ip in ip_address_list:
        if ip.startswith("192.168"):
            result.append(ip)

    return result
