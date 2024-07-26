#!/bin/bash
# Read from /dev/nvme0n1 and write to /dev/zero
# - if=/dev/nvme0n1: input file is the NVMe device /dev/nvme0n1
# - of=/dev/zero: output file is /dev/zero
# - iflag=direct: use direct I/O for the input file
# - bs=16M: read and write in blocks of 16 megabytes
# - count=500: process 500 blocks
# - &: run in the background
dd if=/dev/nvme0n1 of=/dev/zero iflag=direct bs=16M count=500 &
dd if=/dev/nvme1n1 of=/dev/zero iflag=direct bs=16M count=500 &
dd if=/dev/nvme2n1 of=/dev/zero iflag=direct bs=16M count=500 &
dd if=/dev/nvme3n1 of=/dev/zero iflag=direct bs=16M count=500 &
# Loop over all background jobs
for job in $(jobs -p); do
  # Wait for each job to complete
  wait $job
done
