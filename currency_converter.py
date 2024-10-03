from tkinter import *
from tkinter import ttk
import requests

window = Tk()
window.geometry('310x340+500+200')
window.title('Currency Converter')
window.resizable(height=FALSE, width=FALSE)


API_KEY = "03740bd9a4c40e473a16bdb0"
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = requests.get(f'{url}').json()
currencies = dict(response['conversion_rates'])

def convert_currency():
    source = from_currency_combo.get()
    destination = to_currency_combo.get()
    amount = amount_entry.get()
    result = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source}/{destination}/{amount}').json()
    converted_result = result['conversion_result']
    formatted_result = f'{amount} {source} = {converted_result} {destination}'
    result_label.config(text=formatted_result)
    time_label.config(text='Last updated,' + result['time_last_update_utc'])

primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'
top_frame = Frame(window, bg=primary, width=300, height=80)
top_frame.grid(row=0, column=0)
name_label = Label(top_frame, text='Currency Converter', bg=primary, fg=white, pady=30, padx=24, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)
bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)
from_currency_label = Label(bottom_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
from_currency_label.place(x=5, y=10)
to_currency_label = Label(bottom_frame, text='TO:', font=('Poppins 10 bold'), justify=RIGHT)
to_currency_label.place(x=160, y=10)
from_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=5, y=30)
to_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font=('Poppins 10 bold'))
to_currency_combo.place(x=160, y=30)
amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
amount_label.place(x=5, y=55)
amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
amount_entry.place(x=5, y=80)
result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=5, y=115)
time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
time_label.place(x=5, y=135)
convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'), command=convert_currency)
convert_button.place(x=5, y=165)

window.mainloop()
