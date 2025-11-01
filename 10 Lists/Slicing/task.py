def slice_ips(ip_address_list):
    # TODO - Write your code here. Make sure to edit the return line
    if ip_address_list is None:
        return []
    else:
        sliced_ip = ip_address_list[1:3]
    return sliced_ip