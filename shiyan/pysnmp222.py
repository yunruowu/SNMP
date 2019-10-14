from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.hlapi import *

host = input("host:")
host="192.168.43.180"
oid = input("OID:")
oid = "1.3.6.1.2.1.2.2.1.2.4"
print (oid[0])
if oid[0]=='.'or oid[0]=='1':
    g = getCmd(SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
        # ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
        )
else:
    g = getCmd(SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget((host, 161)),
        ContextData(),
        # ObjectType(ObjectIdentity(oid))
        ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
        )
errorIndication, errorStatus, errorIndex, varBinds  = next(g)
if errorIndication:
        print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
            # 推导式
        for varBind in varBinds:
            print("查询的对象：",varBind[0])
                                   
            print("查询的对象的值：",varBind[1])
            
            print(' = '.join([x.prettyPrint() for x in varBind]))


lasttag = 0;
tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
if tag != "1" and tag!="3":
    last = 0
    if oid[0]=='.'or oid[0]=='1':
        g = nextCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
            # ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
            )
    else:
        g = nextCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((host, 161)),
            ContextData(),
            # ObjectType(ObjectIdentity(oid))
            ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
            )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    if errorIndication:
            print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        # print(varBinds)
        for varBind in varBinds:
            print("查询的对象：",varBind[0])
                                   
            print("查询的对象的值：",varBind[1])
            
            print(' = '.join([x.prettyPrint() for x in varBind]))
    print();
    tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
    print();
else:
   
    if tag == "3":
        lasttag = 3
        host = input("host:")
        host="192.168.43.180"
        oid = input("OID:")
        oid = "1.3.6.1.2.1.2.1.0"
        if oid[0]=='.'or oid[0]=='1':
            g = getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
                # ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
                )
        else:
            g = getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((host, 161)),
                ContextData(),
                # ObjectType(ObjectIdentity(oid))
                ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
                )
        errorIndication, errorStatus, errorIndex, varBinds = next(g)
        if errorIndication:
                print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            # print(varBinds)
            for varBind in varBinds:
                print("查询的对象：",varBind[0])
                                    
                print("查询的对象的值：",varBind[1])
                
                print(' = '.join([x.prettyPrint() for x in varBind]))
        print();
        tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
        print();


while tag != "1":
    if tag !="3" and lasttag!=3:
        lasttag = 0
        errorIndication, errorStatus, errorIndex, varBinds = next(g)
        if errorIndication:
                print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print("查询的对象：",varBind[0])
                                    
                print("查询的对象的值：",varBind[1])
                
                print(' = '.join([x.prettyPrint() for x in varBind]))
        print();
        tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
        print();
    if tag !="3"and lasttag==3:
        lasttag = 0
        if oid[0]=='.'or oid[0]=='1':
            g = nextCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
            # ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
            )
        else:
            g = nextCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((host, 161)),
                ContextData(),
                # ObjectType(ObjectIdentity(oid))
                ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
                )
        errorIndication, errorStatus, errorIndex, varBinds = next(g)
        if errorIndication:
                print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            # print(varBinds)
            for varBind in varBinds:
                print("查询的对象：",varBind[0])
                                    
                print("查询的对象的值：",varBind[1])
                
                print(' = '.join([x.prettyPrint() for x in varBind]))
        print();
        tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
        print();
    elif tag=="3":
        lasttag = 3
        host = input("host:")
        host="192.168.43.180"
        oid = input("OID:")
        oid = "1.3.6.1.2.1.2.1.0"
        if oid[0]=='.'or oid[0]=='1':
            g = getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
                # ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
                )
        else:
            g = getCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((host, 161)),
                ContextData(),
                # ObjectType(ObjectIdentity(oid))
                ObjectType(ObjectIdentity('SNMPv2-MIB', oid, 0))
                )
        errorIndication, errorStatus, errorIndex, varBinds = next(g)
        if errorIndication:
                print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            # print(varBinds)
            for varBind in varBinds:
                print("查询的对象：",varBind[0])
                                    
                print("查询的对象的值：",varBind[1])
                
                print(' = '.join([x.prettyPrint() for x in varBind]))
        print();
        tag = input("是否查询next的值？   0：是     1：否      3:重新输入"      ) 
        print();