#!/bin/bash

IP=$(ip -4 addr show tun0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}' --color=none)

echo "VPN IP is : $IP"