# D-Link DNS-320

The D-Link DNS-320 is a network attached storage device.

Product Page: https://www.dlink.com/uk/en/products/dns-320-2-bay-sharecenter-network-storage-enclosure

### Configuration changes

This device needs the `egiga0` interface to run.

Unfortunately, something in the system keeps trying to tell the system to turn off. This could be a watchdog or a broken push button. We get around this by replacing a shutdown script and `/bin/killall` with an `exit0.sh` script.

## Run the rehosting

Run your configuration under penguin. You can connect to the root shell using `telnet` as described in the output a few moments after the run begins. The device will take about 30 seconds to boot. You can view the `console.log` file in the results directory as it boots.

```
13:26:27 penguin.runner INFO Loading plugins
13:26:27 plugins.core INFO Root shell will be available at: 192.168.1.2:23
13:26:27 plugins.core INFO Connect with: telnet 192.168.1.2
13:26:27 penguin.runner INFO Launching rehosting
13:27:36 plugins.VPN INFO          mserver binds udp 0.0.0.0:24629    reach it at 192.168.1.2:24629    
13:27:39 plugins.VPN INFO          mserver binds udp 224.0.0.1:24629  reach it at 192.168.1.2:25629    24629 is already in use
13:27:39 plugins.VPN INFO        op_server binds udp 224.0.0.1:13579  reach it at 192.168.1.2:13579    
13:28:23 plugins.VPN INFO         lighttpd binds tcp 224.0.0.1:80     reach it at 192.168.1.2:1080     80 is privileged and user cannot bind
13:28:23 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:80       reach it at 192.168.1.2:2080     80 is privileged and user cannot bind
13:28:23 plugins.VPN INFO         lighttpd binds tcp [fe80::a8e2:13ff:feba:b4a9]:443 reach it at 192.168.1.2:1443     443 is privileged and user cannot bind
13:28:23 plugins.VPN INFO         lighttpd binds tcp 127.0.0.1:80     reach it at 192.168.1.2:3080     80 is privileged and user cannot bind
13:28:23 plugins.VPN INFO          mserver binds udp 127.0.0.1:24629  reach it at 192.168.1.2:25629    24629 is already in use
13:28:23 plugins.VPN INFO         lighttpd binds udp 127.0.0.1:5555   reach it at 192.168.1.2:5555     
13:28:25 plugins.VPN INFO         lighttpd binds tcp 224.0.0.10:80    reach it at 192.168.1.2:4080     80 is privileged and user cannot bind
13:28:25 plugins.VPN INFO          mserver binds udp 224.0.0.10:24629 reach it at 192.168.1.2:25629    24629 is already in use
13:28:25 plugins.VPN INFO              and binds udp 224.0.0.10:24680 reach it at 192.168.1.2:24680    
main-loop: WARNING: I/O thread spun for 1000 iterations
13:28:41 plugins.VPN INFO          mfg_svr binds udp 127.0.0.1:5901   reach it at 192.168.1.2:5901     
13:28:41 plugins.VPN INFO          mfg_svr binds udp 224.0.0.1:5901   reach it at 192.168.1.2:6901     5901 is already in use
13:28:41 plugins.VPN INFO          mfg_svr binds udp 224.0.0.10:5901  reach it at 192.168.1.2:6901     5901 is already in use
13:28:41 plugins.VPN INFO          mfg_svr binds udp 0.0.0.0:5901     reach it at 192.168.1.2:6901     5901 is already in use
```
