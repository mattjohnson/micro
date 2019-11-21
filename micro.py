#!/usr/bin/env python

# Sonatype Nexus (TM) Open Source Version
# Copyright (c) 2008-present Sonatype, Inc.
# All rights reserved. Includes the third-party code listed at http://links.sonatype.com/products/nexus/oss/attributions.
#
# This program and the accompanying materials are made available under the terms of the Eclipse Public License Version 1.0,
# which accompanies this distribution and is available at http://www.eclipse.org/legal/epl-v10.html.
#
# Sonatype Nexus (TM) Professional Version is available from Sonatype, Inc. "Sonatype" and "Sonatype Nexus" are trademarks
# of Sonatype, Inc. Apache Maven is a trademark of the Apache Software Foundation. M2eclipse is a trademark of the
# Eclipse Foundation. All other trademarks are the property of their respective owners.

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

            os.system('./nxrm.groovy -f -profile "micro-{},micro-ui"'.format(profile))
            os.system('docker build -t {}-ui -f Dockerfile private/assemblies/nexus-micro/target'.format(tag))
        if push:
            os.system('docker push {}'.format(tag))
            os.system('docker push {}-ui'.format(tag))
    click.echo('Done!')


if __name__ == '__main__':
    cli()
