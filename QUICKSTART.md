# Quick Start Guide - Congruences Calculator

## What is this?

This is a mathematical tool that calculates congruences for coprime numbers. It shows the pattern of powers of one number modulo another number.

## Getting Started

### For End Users (Just want to use the app)

1. **Get the executable**
   - Download the executable file from the `dist` folder after it's been built
   - On Windows: `CongruencesCalculator.exe`
   - On Linux/Mac: `CongruencesCalculator`

2. **Run it**
   - Double-click the executable file
   - Or from terminal: `./CongruencesCalculator` (Linux/Mac) or `CongruencesCalculator.exe` (Windows)

3. **Use it**
   - Enter two coprime numbers (numbers with no common factors except 1)
   - Click "Calculate" to see the results
   - Click "Clear" to try different numbers

### For Developers (Want to build from source)

#### Prerequisites
- Python 3.x installed
- pip (Python package manager)

#### Steps to Build

1. **Clone the repository**
   ```bash
   git clone https://github.com/Foodenjoyer25/Congrunces.git
   cd Congrunces
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the executable**
   ```bash
   python build_exe.py
   ```

4. **Find your executable**
   - Look in the `dist/` folder
   - The file will be named `CongruencesCalculator` (or `.exe` on Windows)

## Examples

### Example 1: Simple coprime numbers
- Number 1: `2`
- Number 2: `5`

Results:
```
2 ** 1 [5] -> 2
2 ** 2 [5] -> 4
2 ** 3 [5] -> 3
2 ** 4 [5] -> 1
```

### Example 2: Another pair
- Number 1: `3`
- Number 2: `7`

Results:
```
3 ** 1 [7] -> 3
3 ** 2 [7] -> 2
3 ** 3 [7] -> 6
3 ** 4 [7] -> 4
3 ** 5 [7] -> 5
3 ** 6 [7] -> 1
```

## Troubleshooting

### "Numbers are not coprime" error
- Make sure the two numbers have no common factors
- Try: 2 and 3, 3 and 5, 5 and 7, etc.
- Don't use: 4 and 6 (both divisible by 2), 6 and 9 (both divisible by 3)

### The executable won't run
- Make sure you have execute permissions (Linux/Mac): `chmod +x CongruencesCalculator`
- On Windows, you might need to allow it in Windows Defender

### Build fails
- Make sure Python 3.x is installed: `python --version`
- Make sure tkinter is installed:
  - Linux: `sudo apt-get install python3-tk`
  - Mac: Should be included with Python
  - Windows: Should be included with Python
- Try reinstalling PyInstaller: `pip install --upgrade pyinstaller`

## What are Coprime Numbers?

Two numbers are coprime (or relatively prime) if they share no common factors other than 1.

**Examples of coprime pairs:**
- 2 and 3 ✓
- 5 and 7 ✓
- 4 and 9 ✓
- 8 and 15 ✓

**Examples of non-coprime pairs:**
- 4 and 6 ✗ (both divisible by 2)
- 6 and 9 ✗ (both divisible by 3)
- 10 and 15 ✗ (both divisible by 5)

## Support

For issues or questions, please open an issue on the GitHub repository.
