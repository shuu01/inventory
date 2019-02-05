#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inventory.py
#
#  Copyright 2018 shuu01 <shuu01@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

# example:
# ansible mikrotik -i inventory.py -m raw -a '/ip service disable www; quit' --limit '!UL0V-8BT5' -vvv

# dependencies: sshpass

# output:
"""
data = {
    '_meta': {
        'hostvars': {
            '0D3E-3M0R': {
                'ansible_ssh_user': 'admin',
                'ansible_ssh_pass': 'password',
                'ansible_host': '10.10.68.9'
            },
            '192.168.0.4': {}
        }
    },
    'mikrotik': {
        'children': [],
        "vars": {},
        'hosts': [
            '0D3E-3M0R',
        ]
    },
    'ubnt': {
        'children': [],
        'vars': {},
        'hosts': [
            '0027221EF265',
        ]
    },
    'openwrt': {
        'children': [],
        "vars": {},
        'hosts': [
            'F4F26DD3ECFB',
        ]
    },
    'all': {
        'children': [
        ],
        'hosts': [],
        'vars': {}
    }
}
"""

import json
import MySQLdb

mysql_host = 'mysql_server'
mysql_user = 'inventory'
mysql_passwd = 'inventory'
mysql_db = 'inventory'

def main(args):

    conn = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('set session group_concat_max_len=2048;')

    cursor.execute('select credentials.serial, name, user, password, type, group_concat(address separator ";") as addresses from credentials inner join device inner join address on credentials.serial = device.serial and credentials.serial = address.serial where device.updatedAt > 0 group by serial;')

    hosts = cursor.fetchall()

    conn.close()

    data = {'_meta': {'hostvars': {}}, 'all': {'hosts': []}}

    for host in hosts:

        hostname = host['serial']
        name = host['name']
        hosttype = host['type']
        user = host['user']
        password = host['password']
        addresses = [host.split('/')[0] for host in host['addresses'].split(';')]

        data['_meta']['hostvars'][hostname] = {
            'name': name,
            'ansible_user': user,
            'ansible_ssh_pass': password,
            'ansible_host': addresses[0],
            'ansible_hosts': addresses
        }

        data.setdefault(hosttype, {}).setdefault('hosts', []).append(hostname)

    print(json.dumps(data))

if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))
