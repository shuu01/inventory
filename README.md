# inventory

dynamic inventory script for ansible

### usage

ansible mikrotik -i inventory.py -m raw -a '/ip service disable www; quit' --limit '!UL0V-8BT5' -vvv

### mysql database structure

tables.sql
