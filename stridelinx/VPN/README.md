# StrideLinx Industrial VPN

The StrideLinx Industrial VPN is a remote access VPN solution

Product Page: https://www.automationdirect.com/adc/overview/catalog/communications/secure_remote_access_-_vpn


## Configuration changes

The system must have an environmental value `sxid` set to reflect a model.

The device must have the `/dev/dsa` device and it must return 0 on the ioctls.


## Run the rehosting

```
16:22:06 penguin.runner INFO Loading plugins
16:22:06 plugins.core INFO Root shell will be available at: 192.168.4.2:23
16:22:06 plugins.core INFO Connect with: telnet 192.168.4.2
16:22:06 penguin.runner INFO Launching rehosting
16:22:58 plugins.VPN INFO            inetd binds tcp 0.0.0.0:7        reach it at 192.168.4.2:1007     7 is privileged and user cannot bind
16:22:58 plugins.VPN INFO            inetd binds udp 0.0.0.0:7        reach it at 192.168.4.2:2007     7 is privileged and user cannot bind
16:22:58 plugins.VPN INFO            inetd binds tcp 0.0.0.0:9        reach it at 192.168.4.2:1009     9 is privileged and user cannot bind
16:22:58 plugins.VPN INFO            inetd binds udp 0.0.0.0:9        reach it at 192.168.4.2:2009     9 is privileged and user cannot bind
16:22:58 plugins.VPN INFO            inetd binds tcp 0.0.0.0:23       reach it at 192.168.4.2:1023     23 is privileged and user cannot bind
16:23:34 plugins.VPN INFO            snmpd binds udp 0.0.0.0:161      reach it at 192.168.4.2:1161     161 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            inetd binds udp 127.0.0.1:9      reach it at 192.168.4.2:2009     9 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            inetd binds tcp 127.0.0.1:23     reach it at 192.168.4.2:2023     23 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            inetd binds tcp 127.0.0.1:7      reach it at 192.168.4.2:2007     7 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            inetd binds udp 127.0.0.1:7      reach it at 192.168.4.2:3007     7 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            inetd binds tcp 127.0.0.1:9      reach it at 192.168.4.2:2009     9 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            snmpd binds udp 127.0.0.1:161    reach it at 192.168.4.2:1161     161 is privileged and user cannot bind
16:23:42 plugins.VPN INFO            zebra binds udp 127.0.0.1:2601   reach it at 192.168.4.2:2601     
16:23:44 plugins.VPN INFO             ripd binds udp 0.0.0.0:520      reach it at 192.168.4.2:1520     520 is privileged and user cannot bind
16:23:44 plugins.VPN INFO             ripd binds udp 127.0.0.1:520    reach it at 192.168.4.2:1520     520 is privileged and user cannot bind
16:23:44 plugins.VPN INFO             ripd binds tcp 127.0.0.1:2602   reach it at 192.168.4.2:2602     
16:23:46 plugins.VPN INFO           ripngd binds udp [::]:521         reach it at 192.168.4.2:1521     521 is privileged and user cannot bind
16:23:46 plugins.VPN INFO           ripngd binds tcp 127.0.0.1:2603   reach it at 192.168.4.2:2603     
16:24:27 plugins.VPN INFO         lighttpd binds tcp [::]:80          reach it at 192.168.4.2:1080     80 is privileged and user cannot bind
16:24:27 plugins.VPN INFO         lighttpd binds tcp [::]:443         reach it at 192.168.4.2:1443     443 is privileged and user cannot bind
```