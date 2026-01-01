#!/bin/bash
# Simple build script for Linux/Mac

echo "=========================================="
echo "Congruences Calculator - Build Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3 and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "Error: pip is not installed!"
    echo "Please install pip and try again."
    exit 1
fi

echo "✓ pip found"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Failed to install dependencies!"
    exit 1
fi

echo ""
echo "✓ Dependencies installed"
echo ""

# Build the executable
echo "Building executable..."
python3 build_exe.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Build failed!"
    exit 1
fi

echo ""
echo "=========================================="
echo "✓ Build completed successfully!"
echo "=========================================="
echo ""
echo "Your executable is located at: dist/CongruencesCalculator"
echo ""
echo "To run it:"
echo "  ./dist/CongruencesCalculator"
echo ""
