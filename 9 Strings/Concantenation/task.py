def create_ip_address(first_octet, second_octet, third_octet, fourth_octet):
    # Convert each octet to a string, then join with dots
    ip_parts = ".".join([str(first_octet), str(second_octet), str(third_octet), str(fourth_octet)])
    return ip_parts
