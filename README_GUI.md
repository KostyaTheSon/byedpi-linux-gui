# ByeDPI Linux GUI

A graphical user interface for the ByeDPI DPI circumvention tool on Linux.

## Overview

ByeDPI Linux GUI provides a user-friendly interface for configuring and running the ByeDPI application, which helps bypass Deep Packet Inspection (DPI) systems used by some ISPs and firewalls to block access to certain websites and services.

## Features

- Graphical configuration of all ByeDPI options
- Real-time output monitoring
- Start/Stop controls for the ByeDPI service
- Command generation for advanced users
- Support for all Linux-specific features:
  - TCP MD5 Signatures
  - Transparent proxy mode
  - SACK packet dropping
  - TCP Fast Open

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- The compiled `ciadpi` executable (from the ByeDPI project)

## Installation and Setup

1. Make sure you have the `ciadpi` executable in the same directory as the GUI script
2. Ensure Python 3 is installed on your system
3. Run the GUI application:

```bash
python3 ByeDPI_GUI.py
```

## Usage

1. Configure your desired options in the GUI
2. Click "Generate Command" to preview the command that will be executed
3. Click "Start ByeDPI" to begin the service
4. Monitor the output in the text area at the bottom
5. Click "Stop ByeDPI" to terminate the service

## Configuration Options

The GUI provides access to all major ByeDPI configuration options:

- **Basic Options**: Interface, port, bind address
- **Protocol Modes**: TCP, DNS, HTTP, and TLS handling modes
- **Advanced Options**: Linux-specific features and packet fragmentation
- **HTTP Headers**: Custom headers for HTTP requests
- **TLS Settings**: TLS version, SNI, ciphers, and extensions
- **DNS Settings**: DNS server addresses and handling modes

## License

This project is based on the original ByeDPI project and inherits its license.