#!/bin/bash
# Grep messages that the kernel prints during system boot and while the system is running
sudo dmesg | grep "  device_id"
