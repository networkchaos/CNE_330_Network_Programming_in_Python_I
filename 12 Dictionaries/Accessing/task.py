def dns_resolve(hostname):
    """
    Return the IP for a given hostname. Accepts a few common variants and
    is robust to case, surrounding whitespace, quotes, and simple punctuation.
    Returns None when hostname is None or not found.
    """
    # canonical mapping (lowercase keys)
    dic = {
        "linux": "192.168.1.101",
        "windows": "192.168.1.102",
        "router": "192.168.1.1",
        "gateway": "192.168.1.1",   # common synonym
        "gw": "192.168.1.1"         # short form
    }

    if hostname is None:
        return None

    # Normalize the input to a comparable form
    try:
        h = str(hostname).strip()          # convert to str and trim whitespace
    except Exception:
        return None

    # Remove surrounding quotes if any, take the first token (in case extra text),
    # remove trailing punctuation, then lowercase for lookup.
    h = h.strip('\'"')            # strip surrounding single/double quotes
    h = h.split()[0] if h else "" # keep only first token if multiple words
    h = h.rstrip(',:.')           # remove trailing punctuation like ':' ',' '.'
    h = h.lower()

    return dic.get(h, None)
