#!/bin/bash
# The script to add new user with the SSH public keys.
# Usage:
# $ new_user.sh john "ssh-rsa AAABBBCCC..."
adduser $1 --disabled-password
usermod -a -G sudo $1
usermod -a -G render $1
usermod -a -G video $1
su - $1 -c "mkdir /home/$1/.ssh"
su - $1 -c "echo $2 > /home/$1/.ssh/authorized_keys"
