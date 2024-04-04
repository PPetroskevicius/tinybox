#!/bin/bash
sudo dd if=/dev/md0 of=/dev/null bs=256M count=500 iflag=direct
