# VM Manager - Virtual Machine Management Tool

## Overview

**VM Manager** is a Python-based command-line tool that allows you to interact with virtual machines managed by **libvirt**. It provides functionalities to list, start, stop, visualize, and retrieve IP addresses of virtual machines. It also allows you to fetch the hostname of the hypervisor.

This tool is particularly useful for managing **QEMU/KVM** virtual environments.

## Features

- List all virtual machines and their details.
- Start a selected virtual machine.
- Visualize a virtual machine using **virt-viewer**.
- Stop a running virtual machine.
- Retrieve IP addresses (IPv4/IPv6) of a virtual machine.
- Display the name of the hypervisor.

## Prerequisites

Before using this script, ensure the following requirements are met:

1. **Python** (>= 3.x)
2. **libvirt** library and Python bindings:
   - Install with: `sudo apt-get install libvirt-dev python3-libvirt`
3. **QEMU/KVM** installed and running.
4. **virt-viewer** installed for visualization:
   - Install with: `sudo apt-get install virt-viewer`
5. User permissions to access libvirt (e.g., add your user to the `libvirt` group).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vm-manager.git
   cd vm-manager
   ```

2. Ensure dependencies are installed:
   ```bash
   sudo apt-get update
   sudo apt-get install libvirt-dev python3-libvirt virt-viewer
   ```

## Usage

Run the script using Python 3:

```bash
python3 vm_manager.py
```

## Notes

- Ensure **qemu-guest-agent** is installed on virtual machines to retrieve IP addresses seamlessly.
- Use the `virsh` command-line utility to configure or troubleshoot virtual machines.

## Collaborators

- **Rezak AZIZ**
- **MECHARBAT Lotfi Abdelkrim**
