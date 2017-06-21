# !/usr/bin/env python

# -*- coding:utf-8 -*-

import urllib2
import json
import os
import tarfile
import shutil
import subprocess


def main():
    latest = latest_version()
    download(latest['name'], latest['browser_download_url'])
    docker_build(latest['name'])


def docker_build(file_name):
    tar = tarfile.open(file_name)
    tar.extractall()
    tar.close()

    if os.path.isdir('frp'):
        shutil.rmtree('frp')

    target = file_name.replace('.tar.gz', '')
    os.rename(target, "frp")
    tag = target.split('_')

    cmd = 'docker build -f Dockerfile.server -t lyf362345/frp-server:' + tag[1] + ' -t lyf362345/frp-server:latest .'
    code = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)
    if code == 0:
        print 'server image build done'

    cmd = 'docker build -f Dockerfile.client -t lyf362345/frp-client:' + tag[1] + ' -t lyf362345/frp-client:latest .'
    code = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)
    if code == 0:
        print 'client image build done'


def download(name, url):
    if not os.path.isfile(name) or os.path.getsize(name) <= 0:
        f = urllib2.urlopen(url)
        with open(name, 'wb') as code:
            code.write(f.read())

    print name + ' downloaded'

    return os.path.getsize(name)


def latest_version():
    request = urllib2.Request('https://api.github.com/repos/fatedier/frp/releases')

    token = os.getenv('DOCKER_FRP_BUILD_TOKEN')
    if not token:
        request.add_header('Authorization', 'token ' + token)

    response = urllib2.urlopen(request)
    data = json.load(response)

    for item in data:
        if item['draft']:
            continue

        print 'latest version: ' + item['tag_name']
        f = open('version', 'w')
        f.write(item['tag_name'])
        f.close()

        for asset in item['assets']:
            if 'linux_amd64' not in asset['name']:
                continue

            return asset


if __name__ == '__main__':
    main()
