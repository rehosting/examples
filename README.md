# rehostings

This repository generates docker images for rehosting devices.

Images are organized by manufacturer and device. Each device has a `Dockerfile` that builds the image and a `README.md` that describes the device and how to obtain the firmware and root filesystem.

## Building images

You can build a docker image by running from the root of the repository. For example, to build the `dns320` image:
```
docker build -t dns320 -f ./d-link/dns320/Dockerfile.dns320 .
```

You can also use the `build_target` script to build images. It takes one argument, the target to build. For example, to build the `dns320` image:
```
./build_target dns320
```

This is the appropriate argument because the file in the `d-link/dns320` directory is named `Dockerfile.dns320`.

## Running images

You can run the image with the "repro" or "reproduce" command. This command takes a docker tag as an argument. For example, to run the locally built `dns320` image:
```
penguin repro dns320
```

## Extracting projects

Sometimes you want to take a project and tinker with it. You can do that by extracting the project from the docker image. For example, to extract the `dns320` project to your current directory:
```
docker pull rehosting/examples:dns320
id=$(docker create rehosting/examples:dns320)
docker cp $id:/workspace . # copy the workspace to local folder
docker rm -v $id
```

Now you can run penguin normally:
```
penguin run .
```

NOTE: Images are tagged with specific penguin versions. Copying projects from the workspace can produce different results than running the image with the same penguin version.


## SSH port forwarding for GUI interactions

If your running your rehosting on a remote server and you wish to interact with a service from your local machine (i.e., your GUI web browser), you can use ssh port forwarding to map a local port to forward traffic into your development box and then to a specific IP and port (i.e., the IP that the VPN has exposed the rehosting's service at).

For example, if you see a log message about `httpd` and you wish to connect to it:


```
plugins.VPN INFO            httpd binds tcp 192.168.0.1:80   reach it at 192.168.0.2:55367    80 is privileged and user cannot bind
```

You can reach it at the `192.168.0.2:55367` IP/port from your development machine.

Or you can set up SSH port forwarding from your local machine to bridge the connection to your development machine and then forward traffic to that IP and port. This command would make port 8000 on your local machine connect to the IP and port shown above.

```sh
ssh -N -L 8000:192.168.0.2:55367 user@dev_box
```

After this you could connect to `http://localhost:8000` in a graphical web browser and interact with the rehosted service. If you are running penguin locally, you can do not need to do this step, and you can point your web browser directly at the IP address and port reported by the VPN

# Test image

For penguin development or when working on your own utils you may find `build_basic_rootfs.py` useful.  This script creates a penguin-compatible rootfs tar.gz that provides a very basic http response.

Example usage:
```sh
$ ./build_basic_rootfs.py --arch armel ./test_arm.rootfs.tar.gz
$ penguin init test_arm.rootfs.tar.gz
$ penguin run ./projects/test_arm
```

# Disclaimer

DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.

This material is based upon work supported under Air Force Contract No. FA8702-15-D-0001 or FA8702-25-D-B002. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the U.S. Air Force.

© 2025 Massachusetts Institute of Technology

The software/firmware is provided to you on an As-Is basis.

Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other than as specifically authorized by the U.S. Government may violate any copyrights that exist in this work.
