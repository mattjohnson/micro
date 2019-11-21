#!/usr/bin/env python

import click
import os

@click.command()
@click.option('-b', '--build', is_flag=True, help='Flag to build project')
@click.option('-p', '--push', is_flag=True, help='Flag to push image(s)')
@click.argument('profiles', nargs=-1)
def cli(build, push, profiles):
    """Build and push docker images"""
    for profile in profiles:
        tag = 'iwhsona/nxrm-micro:{}'.format(profile)
        if build:
            os.system('./nxrm.groovy -f -profile "micro-{}"'.format(profile))
            os.system('docker build -t {} -f Dockerfile private/assemblies/nexus-micro/target'.format(tag))
        if push:
            os.system('docker push {}'.format(tag))
    click.echo('Done!')

if __name__ == '__main__':
    cli()
