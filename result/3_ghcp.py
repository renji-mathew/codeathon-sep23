def is_valid_ip_address(ip):
    # Split the IP address into its components
    components = ip.split('.')
    
    # Check that there are exactly 4 components
    if len(components) != 4:
        return False
    
    # Check that each component is an integer between 0 and 255
    for c in components:
        try:
            if int(c) < 0 or int(c) > 255:
                return False
        except ValueError:
            return False
    
    return True

assert is_valid_ip_address('255.255.0.0') == True
assert is_valid_ip_address('555.555.555.555') == False
assert is_valid_ip_address('256.255.0.0') == False
assert is_valid_ip_address('0.0.0.0') == True
assert is_valid_ip_address('192.168.1.1') == True