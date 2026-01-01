import math
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


def gcd(p, q):
    """Create the gcd of two positive integers."""
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    """Check if two numbers are coprime."""
    return gcd(x, y) == 1


class CongruencesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Congruences Calculator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="Congruences Calculator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Number 1 input
        ttk.Label(main_frame, text="Number 1:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.number1_entry = ttk.Entry(main_frame, width=20)
        self.number1_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Number 2 input
        ttk.Label(main_frame, text="Number 2:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.number2_entry = ttk.Entry(main_frame, width=20)
        self.number2_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Calculate button
        self.calculate_btn = ttk.Button(main_frame, text="Calculate", command=self.calculate)
        self.calculate_btn.grid(row=1, column=2, rowspan=2, padx=5, pady=5)
        
        # Results area
        ttk.Label(main_frame, text="Results:").grid(row=3, column=0, sticky=(tk.W, tk.N), pady=5)
        
        # Scrolled text for results
        self.results_text = scrolledtext.ScrolledText(main_frame, width=60, height=20, 
                                                       wrap=tk.WORD, state='disabled')
        self.results_text.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), 
                              pady=5)
        
        # Clear button
        self.clear_btn = ttk.Button(main_frame, text="Clear", command=self.clear_results)
        self.clear_btn.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
    def calculate(self):
        """Calculate congruences based on user input."""
        try:
            # Get input values
            n = int(self.number1_entry.get())
            z = int(self.number2_entry.get())
            
            # Clear previous results
            self.results_text.config(state='normal')
            self.results_text.delete(1.0, tk.END)
            
            # Check if numbers are coprime
            if is_coprime(n, z):
                self.status_var.set(f"Calculating congruences for {n} and {z}...")
                self.root.update()
                
                i = 2
                x = 1
                results = []
                
                # Calculate congruences
                while i != 1:
                    d = n ** int(x)
                    i = int(d) % int(z)
                    result_line = f"{n} ** {x} [{z}] -> {i}\n"
                    results.append(result_line)
                    self.results_text.insert(tk.END, result_line)
                    x = x + 1
                    
                    # Safety limit to prevent infinite loops
                    if x > 10000:
                        self.results_text.insert(tk.END, "\n(Calculation stopped at 10000 iterations)\n")
                        break
                
                self.status_var.set(f"Calculation complete. Found {len(results)} results.")
            else:
                messagebox.showwarning("Not Coprime", 
                                      f"Numbers {n} and {z} are not coprime (GCD = {gcd(n, z)}). "
                                      "Please enter coprime numbers.")
                self.status_var.set("Ready - Please enter coprime numbers")
            
            self.results_text.config(state='disabled')
            
        except ValueError:
            messagebox.showerror("Invalid Input", 
                               "Please enter valid integer numbers.")
            self.status_var.set("Error: Invalid input")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
    
    def clear_results(self):
        """Clear all input fields and results."""
        self.number1_entry.delete(0, tk.END)
        self.number2_entry.delete(0, tk.END)
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state='disabled')
        self.status_var.set("Ready")


def main():
    root = tk.Tk()
    app = CongruencesGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
