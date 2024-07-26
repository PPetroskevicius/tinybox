#!/bin/bash
# Define the color red using ANSI escape codes.
# '\033[0;31m' sets the text color to red.
RED='\033[0;31m'
# Define the "no color" (reset) using ANSI escape codes.
# '\033[0m' resets the text color to default.
NC='\033[0m'
# Print the word "gpus" in red, then reset the text color.
echo -e "${RED}gpus${NC}"
# "edge" - refers to GPU edge temperature
sudo sensors | grep edge
echo -e "${RED}disks${NC}"
# For each NVMe disk (/dev/nvme0 to /dev/nvme3), run the 'nvme smart-log'
# command with the '-H' option to display SMART health information.
nvme smart-log /dev/nvme0 -H | grep temperature
nvme smart-log /dev/nvme1 -H | grep temperature
nvme smart-log /dev/nvme2 -H | grep temperature
nvme smart-log /dev/nvme3 -H | grep temperature
echo -e "${RED}network${NC}"
# https://network.nvidia.com/products/adapter-software/firmware-tools/
#
# Run the 'mget_temp' command to get the temperature of a network
# adapter identified by '/dev/mst/mt4121_pciconf0'
mget_temp -d /dev/mst/mt4121_pciconf0
#mget_temp -d /dev/mst/mt4123_pciconf0
