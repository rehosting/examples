# Trendnet TV

The Trendnet TV-IP201 is a Wireless Network Camera Server w/ Audio.

Product Page: https://www.trendnet.com/support/support-detail.asp?prod=125_TV-IP201W


## Obtain firmware and package rootfs

Download the firmware

```sh
$ wget 'https://downloads.trendnet.com/tv-ip201w/firmware/fw_tv-ip201_201w(v2.00.110).zip'
```

Extract the root filesystem with `fw2tar`
```sh
$ fw2tar fw_tv-ip201_201w(v2.00.110).zip
```

The generated `fw_tv-ip201_201w(v2.00.110).rootfs.tar.gz` will likely have a sha1sum of `d3df1d59f2b752773efd7a31bd0778a4bfa30415`.

## Initialize rehosting
Now take your `fw_tv-ip201_201w(v2.00.110).rootfs.tar.gz` and initialize a penguin project:

```sh
$ penguin init fw_tv-ip201_201w(v2.00.110).rootfs.tar.gz`
```

### Configuration chagnes

This device expects to have a non-standard network interface named `adm0`. First add this into the list of network devices in the `netdevs` section:

```yaml
netdevs:
- adm0
...
```

Shell scripts on this device are broken by our instrumented version of sh. Disable this instrumentation by deleting the following lines in the `static_files` setcion of your config:
```yaml
  /igloo/utils/sh.orig:
    type: move
    from: /bin/sh
  /bin/sh:
    type: symlink
    target: /igloo/utils/busybox
```

## Run the rehosting

Run your configuration under penguin. You can connect to the root shell using `telnet` as described in the output a few moments after the run begins. The device will take about 30 seconds to boot. You can view the `console.log` file in the results directory as it boots.

```
17:06:16 penguin.runner INFO Launching rehosting
17:06:35 plugins.VPN INFO             upnp binds tcp 0.0.0.0:61003    reach it at 192.168.1.2:61003
17:06:35 plugins.VPN INFO             upnp binds udp 0.0.0.0:1900     reach it at 192.168.1.2:1900
17:06:35 plugins.VPN INFO              udp binds udp 0.0.0.0:62976    reach it at 192.168.1.2:62976
17:06:35 plugins.VPN INFO          portmap binds udp 0.0.0.0:111      reach it at 192.168.1.2:35811    111 is privileged and user cannot bind
17:06:35 plugins.VPN INFO          portmap binds tcp 0.0.0.0:111      reach it at 192.168.1.2:38653    111 is privileged and user cannot bind
17:06:35 plugins.VPN INFO             webs binds tcp 0.0.0.0:80       reach it at 192.168.1.2:55315    80 is privileged and user cannot bind
```
