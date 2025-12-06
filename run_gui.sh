#!/bin/bash

# ByeDPI Linux GUI Launcher Script

# Check if ciadpi executable exists
if [ ! -f "./ciadpi" ]; then
    echo "Error: ciadpi executable not found!"
    echo "Please make sure you have compiled ByeDPI first."
    echo "You can compile it by running: make"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if tkinter is available
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Error: tkinter module is not available"
    echo "On Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "On CentOS/RHEL: sudo yum install tkinter"
    exit 1
fi

echo "Starting ByeDPI Linux GUI..."
python3 ByeDPI_GUI.py