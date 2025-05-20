import tkinter as tk  
from tkinter import *
import tkinter.messagebox 
from forex_python.converter import CurrencyRates

# GUI
root = tk.Tk()
root.title("Currency Converter: ")

Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency Converter: GeeksForGeeks',
                     bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")

# Function for Real-Time Currency Conversion
def RealTimeCurrencyConversion():
    c = CurrencyRates()
    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
    elif from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency from the menu.")
    else:
        try:
            new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.delete(0, tk.END)  # Clear previous output
            Amount2_field.insert(0, str(new_amount))
        except Exception as e:
            tkinter.messagebox.showinfo("Error !!", f"Conversion failed: {str(e)}")

# Clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

label_amount = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label_amount.grid(row=2, column=0, sticky=W)

label_from_currency = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label_from_currency.grid(row=3, column=0, sticky=W)

label_to_currency = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label_to_currency.grid(row=4, column=0, sticky=W)

label_converted_amount = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label_converted_amount.grid(row=8, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

convert_button = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
                        command=RealTimeCurrencyConversion)
convert_button.grid(row=6, column=0)

clear_button = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                      command=clear_all)
clear_button.grid(row=10, column=0)

root.mainloop()
