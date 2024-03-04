import tkinter as tk

class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.equations = []

        self.equation_entry = tk.Entry(root, width=30)
        self.equation_entry.grid(row=0, column=0)

        self.add_button = tk.Button(root, text="Agregar ecuación", command=self.add_equation)
        self.add_button.grid(row=0, column=1)

        self.equations_label = tk.Label(root, text="Ecuaciones:")
        self.equations_label.grid(row=1, column=0, columnspan=2)

        self.equations_text = tk.Text(root, width=40, height=10)
        self.equations_text.grid(row=2, column=0, columnspan=2)

        self.solve_button = tk.Button(root, text="Resolver", command=self.show_result)
        self.solve_button.grid(row=3, column=0, columnspan=2)

    def add_equation(self):
        equation = self.equation_entry.get()
        self.equations.append(equation)
        self.equations_text.insert(tk.END, equation + "\n")
        self.equation_entry.delete(0, tk.END)

    def show_result(self):
        result_message = f"El resultado de las ecuaciones:\n{'  ;  '.join(self.equations)}\n\nY el resultado de ello es: RESULTADO"
        result_window = tk.Toplevel(self.root)
        result_label = tk.Label(result_window, text=result_message)
        result_label.pack()

def main():
    root = tk.Tk()
    root.title("Solver de Ecuaciones")
    app = EquationSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
