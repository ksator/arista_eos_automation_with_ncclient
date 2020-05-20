from ncclient import manager

eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

domain_name='''
<system>
    <config>
        <domain-name>
        </domain-name>
    </config>
</system>
'''

domain_name_conf = eos.get_config(source="running", filter=("subtree", domain_name))
print (domain_name_conf)

Interface_Ethernet3='''
<interfaces>
    <interface>
        <name>Ethernet3</name>
    </interface>
</interfaces>
'''

Interface_Ethernet3_conf = eos.get_config(source="running", filter=("subtree", Interface_Ethernet3))
print(Interface_Ethernet3_conf)

eos.close_session()