#!/bin/bash

# ByeDPI Linux GUI Installation Script

echo "ByeDPI Linux GUI Installation"
echo "=============================="

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "Warning: This script is designed for Linux systems"
fi

# Check for required packages
echo "Checking for required packages..."

if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Ubuntu/Debian: sudo apt-get install python3"
    echo "CentOS/RHEL: sudo yum install python3"
    exit 1
fi

if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Error: tkinter module is not available"
    echo "Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "CentOS/RHEL: sudo yum install tkinter"
    exit 1
fi

echo "Python 3 and tkinter are available"

# Check if ciadpi executable exists
if [ ! -f "./ciadpi" ]; then
    echo "ciadpi executable not found. Attempting to compile..."
    if [ -f "Makefile" ]; then
        make
        if [ $? -ne 0 ]; then
            echo "Error: Failed to compile ciadpi"
            exit 1
        fi
        echo "Successfully compiled ciadpi"
    else
        echo "Error: Makefile not found, cannot compile ciadpi"
        exit 1
    fi
else
    echo "Found ciadpi executable"
fi

# Create a directory for the GUI application
INSTALL_DIR="$HOME/.local/share/byedpi-gui"
mkdir -p "$INSTALL_DIR"

# Copy files to installation directory
cp ByeDPI_GUI.py "$INSTALL_DIR/"
cp run_gui.sh "$INSTALL_DIR/"
cp README_GUI.md "$INSTALL_DIR/"
cp ciadpi "$INSTALL_DIR/"

echo "Files copied to $INSTALL_DIR"

# Create executable in PATH
BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"
cat > "$BIN_DIR/byedpi-gui" << 'EOF'
#!/bin/bash
cd $HOME/.local/share/byedpi-gui
python3 ByeDPI_GUI.py "$@"
EOF

chmod +x "$BIN_DIR/byedpi-gui"

echo "Created executable at $BIN_DIR/byedpi-gui"

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "Adding $HOME/.local/bin to PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Please run 'source ~/.bashrc' or restart your terminal to update PATH"
fi

# Create desktop entry
DESKTOP_DIR="$HOME/.local/share/applications"
mkdir -p "$DESKTOP_DIR"

# Create desktop entry file
cat > "$DESKTOP_DIR/byedpi-gui.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ByeDPI Linux GUI
Comment=A graphical interface for the ByeDPI DPI circumvention tool
Exec=$HOME/.local/share/byedpi-gui/ByeDPI_GUI.py
Icon=network-wired
Terminal=false
Categories=Network;Proxy;
Path=$HOME/.local/share/byedpi-gui
EOF

chmod +x "$DESKTOP_DIR/byedpi-gui.desktop"
echo "Created desktop entry at $DESKTOP_DIR/byedpi-gui.desktop"

echo
echo "Installation completed!"
echo
echo "You can now run ByeDPI Linux GUI by:"
echo "1. Running 'byedpi-gui' in terminal"
echo "2. Using the desktop application"
echo
echo "To start the application now, run:"
echo "  byedpi-gui"