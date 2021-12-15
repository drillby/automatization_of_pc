from wakeonlan import send_magic_packet


def wol(mac: str, broadcast_ip: str) -> None:
    if type(mac) is not str:
        raise TypeError("mac must be a string")
    if type(broadcast_ip) is not str:
        raise TypeError("broadcast_ip must be a string")
    send_magic_packet(mac, ip_address=broadcast_ip)
    return
