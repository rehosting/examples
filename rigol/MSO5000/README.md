# MSO5000

The MSO5000 is a mixed signal oscilloscope from Rigol.

Product Page: https://www.rigolna.com/products/digital-oscilloscopes/MSO5000/

Useful links: https://web.archive.org/web/20240228184535/https://tortel.li/post/insecure-scope/

## Building the root filesystem

This device fails to be handled by fw2tar.

## Configuration changes

There are no technically required changes to the configuration.

The `/dev/ttyPS0` device is helpful to have in the configuration.

Further, it is faster to replace the `/usr/sbin/nanddump` utility with `exit0.sh` to avoid the slow utility that does nothing.

## Run the rehosting

Run your configuration under penguin. You can connect to the root shell using `telnet` as described in the output a few moments after the run begins. The device will take about 30 seconds to boot. You can view the `console.log` file in the results directory as it boots.

```
20:55:01 penguin.runner INFO Loading plugins
20:55:01 plugins.core INFO Root shell will be available at: 192.168.0.2:23
20:55:01 plugins.core INFO Connect with: telnet 192.168.0.2
20:55:01 penguin.runner INFO Launching rehosting
20:55:56 plugins.VPN INFO          rpcbind binds udp 0.0.0.0:111      reach it at 192.168.0.2:1111     111 is privileged and user cannot bind
20:55:56 plugins.VPN INFO          rpcbind binds udp 0.0.0.0:859      reach it at 192.168.0.2:1859     859 is privileged and user cannot bind
20:55:56 plugins.VPN INFO          rpcbind binds tcp 0.0.0.0:111      reach it at 192.168.0.2:1111     111 is privileged and user cannot bind
20:55:58 plugins.VPN INFO         lighttpd binds tcp 0.0.0.0:80       reach it at 192.168.0.2:1080     80 is privileged and user cannot bind
20:55:59 plugins.VPN INFO            cupsd binds udp 0.0.0.0:631      reach it at 192.168.0.2:1631     631 is privileged and user cannot bind
```

It's worth noting that this rehosting fails to load the web server because the loopback interface is never brought up.

You can fix this by running the following command in the root shell:

```
ifconfig lo up
```