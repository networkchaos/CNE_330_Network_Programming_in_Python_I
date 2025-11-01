def check_in(ip_address, octet):
    # Split the IP address into its parts
    ip_parts = ip_address.split('.')
    # Return True if the octet (as string) is inside the IP
    return str(octet) in ip_parts


def check_not_in(ip_address, octet):
    # Split the IP address into its parts
    ip_parts = ip_address.split('.')
    # Return True if the octet (as string) is NOT inside the IP
    return str(octet) not in ip_parts
