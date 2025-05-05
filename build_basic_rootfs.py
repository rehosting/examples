#!/usr/bin/env python3

import click
import requests
import os
import tempfile
import subprocess
import shutil

# The dirs required by penguin to be recognized as a rootfs
required_dirs = ['proc', 'bin', 'dev', 'etc', 'usr', 'var']

basic_micropython_www_server = r'''
#!/igloo/utils/micropython
import socket

s = socket.socket()

print("Socket created")

PORT = 80
addr = socket.getaddrinfo("127.0.0.1", PORT)[0][-1]

try:
    s.bind(addr)
    print("Server is listening")
    s.listen(1)

    while True:
        c, caddr = s.accept()
        val = c.recv(1024)
        ip = socket.inet_ntop(socket.AF_INET, caddr[4:8])
        print("Got connection from", ip)
        out = """HTTP/1.1 200 OK\r
Connection: close\r
Content-Type: text/html\r
Content-Length: 46\r
\r
<html><body><h1>Hello World</h1></body></html>"""
        c.send(out.encode())
        c.close()
except OSError as e:
    print(f"OSError: [Errno {e.errno}]")
    while True:
        pass
'''

basic_init = r'''
#!/igloo/utils/sh
/igloo/utils/micropython /www_server.py
'''


@click.command()
@click.argument('output')
@click.option('--arch', help='Architecture (e.g., armel)', required=True)
@click.option('--repo', default='rehosting/busybox',
              help='GitHub repository to fetch the busybox from.')
@click.option('--release', default='latest', help='Busybox version to fetch.')
def cli(arch, repo, release, output):
    """
    This is a CLI tool for building a basic roofs.
     Arguments:
        output: Output name for the rootfs tar.gz (e.g., basic_rootfs.tar.gz)
    """
    with tempfile.TemporaryDirectory() as working_dir:
        busybox_tgz = download_busybox(repo, release, working_dir)
        rootfs_path = os.path.join(working_dir, 'rootfs_targz')
        os.mkdir(rootfs_path)

        for dir_name in required_dirs:
            os.makedirs(os.path.join(rootfs_path, dir_name), exist_ok=True)
            click.echo(f"Created directory: {dir_name}")

        try:
            subprocess.run(['tar', '-xzf', busybox_tgz, '-C', working_dir],
                           check=True)
            # Extracting the binary directly to the rootfs wasn't behaving
            shutil.copy(os.path.join(working_dir, f'build/{arch}/busybox'),
                        os.path.join(rootfs_path, 'bin', 'busybox'))
            click.echo(f"Extracted busybox for {arch} to {rootfs_path}/bin")
        except subprocess.CalledProcessError as e:
            click.echo(f"Error extracting busybox for {arch}: {e}", err=True)
            return

        os.symlink('busybox', os.path.join(rootfs_path, 'bin', 'sh'))
        with open(os.path.join(rootfs_path, 'www_server.py'), 'w') as f:
            f.write(basic_micropython_www_server)
            click.echo("Created basic web server script")
        with open(os.path.join(rootfs_path, 'init'), 'w') as f:
            f.write(basic_init)
            click.echo("Created init script")
        os.chmod(os.path.join(rootfs_path, 'init'), 0o755)

        # Tar up everything with ./ as the root
        tar_output_path = os.path.abspath(output)
        click.echo(f"Creating tarball at {tar_output_path}...")
        subprocess.run(['tar', '-czf', tar_output_path, '-C', rootfs_path, '.'],
                       check=True)
        click.echo(f"Tarball created: {tar_output_path}")


def download_busybox(repo, release, output_dir):
    click.echo(f"Fetching the latest release for {repo}...")
    api_url = f"https://api.github.com/repos/{repo}/releases/{release}"
    response = requests.get(api_url)

    if response.status_code == 200:
        release_data = response.json()
        asset = release_data['assets'][0]
        download_url = asset['browser_download_url']
        file_name = asset['name']

        click.echo(f"Downloading {file_name} from {download_url}...")
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        with requests.get(download_url, stream=True) as download_response:
            with open(file_path, 'wb') as f:
                for chunk in download_response.iter_content(chunk_size=8192):
                    f.write(chunk)

        click.echo(f"Downloaded latest release to {file_path}")
    else:
        click.echo(f"Failed to fetch release info: {response.status_code} - {response.text}")
    return file_path


if __name__ == '__main__':
    cli()
