"""
Build script to create the executable using PyInstaller.
Run this script to generate the executable file.
"""
import PyInstaller.__main__
import os
import sys

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
gui_script = os.path.join(script_dir, 'congruences_gui.py')

# PyInstaller arguments
pyinstaller_args = [
    gui_script,
    '--onefile',  # Create a single executable file
    '--windowed',  # Don't show console window on Windows
    '--name=CongruencesCalculator',  # Name of the executable
    '--clean',  # Clean PyInstaller cache before building
    f'--distpath={os.path.join(script_dir, "dist")}',  # Output directory
    f'--workpath={os.path.join(script_dir, "build")}',  # Working directory
    f'--specpath={script_dir}',  # Spec file location
]

if __name__ == '__main__':
    print("Building executable with PyInstaller...")
    print(f"Source: {gui_script}")
    print("-" * 50)
    PyInstaller.__main__.run(pyinstaller_args)
    print("-" * 50)
    print("Build complete! Check the 'dist' folder for the executable.")
