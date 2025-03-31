import customtkinter as ctk
from src.backend.limit_logic import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import re
from pyparsing import Forward, Word, infixNotation, oneOf, CaselessKeyword, alphas, nums, opAssoc
import operator


class LimitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Math Concepts')
        self.geometry('500x800')
        self.function = None
        self.limitpoint = None
        self.safe_functions = {
                                    "sin": np.sin,
                                    "cos": np.cos,
                                    "tan": np.tan,
                                    "exp": np.exp,
                                    "log": np.log,
                                    "sqrt": np.sqrt,
                                    "e": np.exp
                                }
        
        self.fig, self.ax = plt.subplots()
        self.canvas_frame = ctk.CTkFrame(self)
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.canvas_frame)

        self.function_field = ctk.CTkEntry(self, placeholder_text='Enter Your Function Here')
        self.function_field.grid(row=0, column=0, padx=(10, 5), pady=20, sticky='ew')
        self.graph_function = ctk.CTkButton(self, text='Graph Function', command=self.plot_graph)
        self.graph_function.grid(row=0, column=1, padx=(0,10))

        self.limitpoint_field = ctk.CTkEntry(self, placeholder_text='Enter Your limit point Here')
        self.limitpoint_field.grid(row=1, column=0, padx=(10, 5), pady=(0, 20), sticky='ew')
        self.animate_function = ctk.CTkButton(self, text='Animate points')
        self.animate_function.grid(row=1, column=1, padx=(0,10), pady=(0, 20))

        self.calculate_limit = ctk.CTkButton(self, text='Calculate Limit', command=self.calculate)
        self.calculate_limit.grid(row=2, column=0, pady=(0,5), padx=(10,5))
        self.estimated_limit_label = ctk.CTkLabel(self, text='Estimated Limit is')
        self.estimated_limit_label.grid(row=3, column=0, pady=(0,5), padx=(10,5))

        self.grid_columnconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def evaluate_expression(self, expression):
        """Replaces standard math functions with NumPy equivalents and evaluates the function."""
        try:
            for item in self.safe_functions:
                if item in expression:
                    new_expression = self.safe_functions[item]
                    var = re.sub('[()]', '', expression[len(item):])  
                    break
            return new_expression, var
        except Exception as e:
            return f"Error: {e}"

    def plot_graph(self,):
        """Event for Graph Function button"""
        self.function = self.function_field.get()
        self.limitpoint = self.limitpoint_field.get()

        # print(self.function.__class__)
        self.func = self.evaluate_expression(self.function)
        self.test_limit = Limit(lambda x: self.func[0](eval(self.func[1])), float(self.limitpoint))
        self.canvas_frame.grid(row=4, column=0)
        self.canvas_frame.grid_columnconfigure(0, weight=1)

        self.ax.clear()
        self.test_limit.draw(self.ax)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='ew')


    def calculate(self,):
        """Event for Calculate widget"""
        self.function = self.function_field.get()
        self.limitpoint = self.limitpoint_field.get()

        self.func = self.evaluate_expression(self.function)

        self.test_limit = Limit(lambda x: self.func[0](eval(self.func[1])), float(self.limitpoint))
        self.estimated_limit_label.configure(text=f'Estimated Limit is {self.test_limit.solve_epsilon()}')

    def on_close(self):
        plt.close(self.fig)
        self.quit()
        self.destroy()

    def parse_expression(self, expression):
        opn = {
                        '+':operator.add, 
                        '-':operator.sub, 
                        '*': operator.mul, 
                        '/':operator.truediv, 
                        '^':operator.pow, 
                        '**':operator.pow
               }
        
        variable = Word(alphas, exact=1)
        number = Word(nums)
        operators = oneOf(' '.join(opn.keys()))
        operand = variable | number 
        expr = Forward()
        expr <<= infixNotation(operand, [
            ("*", 2, opAssoc.LEFT),
            ("/", 2, opAssoc.LEFT),
            ("+", 2, opAssoc.LEFT),
            ("-", 2, opAssoc.LEFT),
            ("**", 2, opAssoc.LEFT),
            ("^", 2, opAssoc.LEFT),
        ])
        e = CaselessKeyword('E')
        pi = CaselessKeyword('PI')

        parsed = expr.parseString(expression, parseAll=True)

        

# app = LimitApp()

# app.mainloop()