# DrayTek Vigor 2960

The DrayTek Vigor 2960 is a consumer Wireless Router.

Product Page: https://www.draytek.co.uk/support/downloads/vigor-2960


### Configuration chagnes
No configuration changes are required for this device, it should work right out of the box.


## Run the rehosting

Run your configuration under penguin. You can connect to the root shell using `telnet` as described in the output a few moments after the run begins. The device will take a few minutes to boot. You can view the `console.log` file in the results directory as it boots.

**NOTE**: When connecting to the web server use the `/mobile` endpoint. It's not clear why it doesn't resolve the `/` endpoint.

```
19:12:27 penguin.runner INFO Launching rehosting
19:14:14 plugins.VPN INFO          telnetd binds tcp [::]:23          reach it at 192.168.5.2:1023     23 is privileged and user cannot bind
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:80       reach it at 192.168.5.2:1080     80 is privileged and user cannot bind
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:443      reach it at 192.168.5.2:1443     443 is privileged and user cannot bind
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:44300    reach it at 192.168.5.2:44300    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59886    reach it at 192.168.5.2:59886    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59887    reach it at 192.168.5.2:59887    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59890    reach it at 192.168.5.2:59890    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59892    reach it at 192.168.5.2:59892    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59895    reach it at 192.168.5.2:59895    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59889    reach it at 192.168.5.2:59889    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59894    reach it at 192.168.5.2:59894    
19:15:08 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:59893    reach it at 192.168.5.2:59893    
19:16:10 plugins.VPN INFO        ntpclient binds udp 0.0.0.0:123      reach it at 192.168.5.2:1123     123 is privileged and user cannot bind
19:17:46 plugins.VPN INFO          dhrelay binds udp 0.0.0.0:67       reach it at 192.168.5.2:1067     67 is privileged and user cannot bind
19:18:42 plugins.VPN INFO          dnsmasq binds udp 0.0.0.0:53       reach it at 192.168.5.2:1053     53 is privileged and user cannot bind
19:18:42 plugins.VPN INFO          dnsmasq binds tcp 0.0.0.0:53       reach it at 192.168.5.2:1053     53 is privileged and user cannot bind
```

