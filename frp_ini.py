def frp_ini():
    ip= []
    data = ""
    with open('ip.txt','r',encoding='utf-8') as f:
        ips = f.readlines()
        for i in ips:
            ip.append(i.strip())
    for x in ip:
        #print(type(x))
        port = x.split(':')
        iplist = port[:1]
        portlist = port[1:2]
        ipok = "".join(iplist)
        portok = "".join(portlist)
        for a in range(1,134):#多少行ip:端口,根据数量修改range数值
            data = '[mysql{}]\ntype = tcp\nlocal_ip = {}\nlocal_port = {}\nremote_port = 6{}\n'.format(a, ipok, portok, a)
            with open('frp_data.txt','a+') as fs:
                fs.writelines(data+'\n')
frp_ini()