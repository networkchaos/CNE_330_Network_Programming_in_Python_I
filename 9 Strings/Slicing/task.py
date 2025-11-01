def get_first_octet(ip_address):
    # TODO - Write your code here. Make sure to edit the return line
    ip_parts = ip_address.split('.')
    # Return the first part converted to integer
    return int(ip_parts[0])

def get_third_octet(ip_address):
    # TODO - Write your code here. Make sure to edit the return line

    ip_parts = ip_address.split('.')
    # Return the third part converted to integer
    return int(ip_parts[2])
