from ncclient import manager
from ncclient.xml_ import to_ele
import logging
import time
import threading

logging.basicConfig(level=logging.DEBUG)

rpc2 = """
<cli xmlns="http://cisco.com/ns/yang/cisco-nx-os-device"><mode>EXEC</mode><cmdline>run bash timeout 2 ls /bootflash </cmdline></cli>
"""

def initial_call():
    with manager.connect(host="ip-address", port="830", timeout=180, username="username", password="password", hostkey_verify=False, device_params={"name":"nexus"}) as conn:
        xmlagentreply = conn.exec_command(["copy http://tftp-ip-address/nxos64-cs.10.3.3q.F.bin bootflash:nxos64-cs.10.3.3.F.bin vrf default use-kstack"])
        return(xmlagentreply)

def check_for_file():
    with manager.connect(host="ip-address", port="830", timeout=180, username="username", password="password", hostkey_verify=False, device_params={"name": "nexus"}) as conn2:
        rpcreply2 = conn2.dispatch(to_ele(rpc2))
        return(rpcreply2)

if __name__ == '__main__':
    first = threading.Thread(target=initial_call)
    second = threading.Thread(target=check_for_file)
    first.start()
    second.start()
