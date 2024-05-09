from ncclient import manager
from ncclient.xml_ import to_ele
import logging
import time
import threading

logging.basicConfig(level=logging.DEBUG)

#CONSIDERATIONS:
#Idle-Timeout Config: defaults to 5 minutes for idle sessions to be disconnected, this can be disabled
#Limit Config: max client sessions is 10 (default to 5) so if you don't close out sessions and remove idle timeouts, you could run into this limitation

rpc1 = """
<cli xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
  <mode>EXEC</mode>
    <cmdline> run bash timeout 2 ls /bootflash</cmdline>
 </cli>
"""

rpc2 = """
<cli xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
  <mode>EXEC</mode>
    <cmdline> show version</cmdline>
 </cli>
"""

manager_object = manager.connect(host="ip-address", port="830", timeout=75, username="username", password="password", hostkey_verify=False, device_params={"name":"nexus"})
rpcreply1 = manager_object.dispatch(to_ele(rpc1))
print(rpcreply1)
rpcreply2 = manager_object.dispatch(to_ele(rpc2))
print(rpcreply2)
manager_object.close_session()
