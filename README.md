# Congruences Calculator

A mathematical tool for calculating modular exponentiation sequences for coprime numbers.

## Description

This program finds the sequence of n^x mod z for coprime numbers n and z, continuing until the result returns to 1. This is useful for understanding modular arithmetic and cyclic groups in number theory.

## Features

- **Python CLI Version**: Command-line interface for quick calculations
- **Web Frontend**: User-friendly web interface with real-time validation

## Usage

### Python CLI Version

Run the Python script directly:

```bash
python3 congruences.py
```

You will be prompted to enter two coprime numbers:
- Number 1 (n): The base number
- Number 2 (z): The modulus

Example:
```
Number 1: 3
Number 2: 7
```

Output:
```
3 ** 1 [ 7 ]-> 3
3 ** 2 [ 7 ]-> 2
3 ** 3 [ 7 ]-> 6
3 ** 4 [ 7 ]-> 4
3 ** 5 [ 7 ]-> 5
3 ** 6 [ 7 ]-> 1
```

### Web Frontend

1. Open `index.html` in your web browser, or
2. Serve it with a local web server:

```bash
python3 -m http.server 8000
```

Then navigate to `http://localhost:8000` in your browser.

The web interface features:
- Input validation for coprime numbers
- Clear error messages for invalid inputs
- Formatted results table with superscript notation
- Responsive design that works on all devices

## Requirements

- Python 3.x (for CLI version)
- Modern web browser (for web frontend)

## Mathematical Background

Two numbers are **coprime** (or relatively prime) if their greatest common divisor (GCD) is 1. 

For coprime numbers n and z, the sequence n^1 mod z, n^2 mod z, n^3 mod z, ... will eventually return to 1, demonstrating the cyclic nature of modular arithmetic.

## Examples

### Example 1: n=3, z=7
- 3^1 mod 7 = 3
- 3^2 mod 7 = 9 mod 7 = 2
- 3^3 mod 7 = 27 mod 7 = 6
- 3^4 mod 7 = 81 mod 7 = 4
- 3^5 mod 7 = 243 mod 7 = 5
- 3^6 mod 7 = 729 mod 7 = 1

### Example 2: n=2, z=5
- 2^1 mod 5 = 2
- 2^2 mod 5 = 4
- 2^3 mod 5 = 8 mod 5 = 3
- 2^4 mod 5 = 16 mod 5 = 1

## License

Open source - feel free to use and modify.
