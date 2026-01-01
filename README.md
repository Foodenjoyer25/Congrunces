# Congruences Calculator

A Python application that calculates congruences with both console and GUI interfaces.

## Features

- Calculate congruences for coprime numbers
- User-friendly graphical interface
- Can be compiled into a standalone executable

## Files

- `congruences.py` - Original console-based version
- `congruences_gui.py` - GUI version with tkinter
- `build_exe.py` - Script to build the executable
- `requirements.txt` - Python dependencies

## Running the Application

### Console Version

```bash
python congruences.py
```

### GUI Version

```bash
python congruences_gui.py
```

## Building the Executable

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Build Steps

#### Option 1: Using the build script (Recommended)

```bash
python build_exe.py
```

#### Option 2: Using PyInstaller directly

```bash
pyinstaller --onefile --windowed --name=CongruencesCalculator congruences_gui.py
```

### Build Output

After building, you'll find:
- `dist/CongruencesCalculator` (Linux/Mac) or `dist/CongruencesCalculator.exe` (Windows) - The standalone executable
- `build/` - Temporary build files (can be deleted)
- `CongruencesCalculator.spec` - PyInstaller specification file

### Running the Executable

Simply double-click the executable file in the `dist` folder, or run it from the command line:

**Windows:**
```bash
dist\CongruencesCalculator.exe
```

**Linux/Mac:**
```bash
./dist/CongruencesCalculator
```

## How to Use

1. Enter two coprime numbers (numbers whose greatest common divisor is 1)
2. Click "Calculate" to see the congruence results
3. Results will show the pattern: `n ** x [z] -> i`
4. Click "Clear" to reset and try with different numbers

## Example

For coprime numbers 2 and 5:
- 2 ** 1 [5] -> 2
- 2 ** 2 [5] -> 4
- 2 ** 3 [5] -> 3
- 2 ** 4 [5] -> 1

## Notes

- Numbers must be coprime (GCD = 1) for the calculation to work
- The application will notify you if numbers are not coprime
- Large numbers may take longer to calculate
