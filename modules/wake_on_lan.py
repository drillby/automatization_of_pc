from wakeonlan import send_magic_packet

send_magic_packet("DC-41-A9-E2-FE-0F", ip_address="192.168.132.102",
                  port=80, interface="192.168.132.1")
