import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class UnitConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        

        self.title("Конвертер единиц измерения")
        self.geometry("700x500")
        self.resizable(False, False)
        

        self.conversion_data = {
            "Длина": {
                "Километр": {"Метр": 1000, "Сантиметр": 100000, "Миля": 0.621371, "Фут": 3280.84, "Дюйм": 39370.1},
                "Метр": {"Километр": 0.001, "Сантиметр": 100, "Миля": 0.000621371, "Фут": 3.28084, "Дюйм": 39.3701},
                "Сантиметр": {"Километр": 0.00001, "Метр": 0.01, "Миля": 0.00000621371, "Фут": 0.0328084, "Дюйм": 0.393701},
                "Миля": {"Километр": 1.60934, "Метр": 1609.34, "Сантиметр": 160934, "Фут": 5280, "Дюйм": 63360},
                "Фут": {"Километр": 0.0003048, "Метр": 0.3048, "Сантиметр": 30.48, "Миля": 0.000189394, "Дюйм": 12},
                "Дюйм": {"Километр": 0.0000254, "Метр": 0.0254, "Сантиметр": 2.54, "Миля": 0.0000157828, "Фут": 0.0833333}
            },
            "Масса": {
                "Килограмм": {"Грамм": 1000, "Фунт": 2.20462, "Унция": 35.274, "Тонна": 0.001},
                "Грамм": {"Килограмм": 0.001, "Фунт": 0.00220462, "Унция": 0.035274, "Тонна": 0.000001},
                "Фунт": {"Килограмм": 0.453592, "Грамм": 453.592, "Унция": 16, "Тонна": 0.000453592},
                "Унция": {"Килограмм": 0.0283495, "Грамм": 28.3495, "Фунт": 0.0625, "Тонна": 0.0000283495},
                "Тонна": {"Килограмм": 1000, "Грамм": 1000000, "Фунт": 2204.62, "Унция": 35274}
            },
            "Температура": {
                "Цельсий": {"Фаренгейт": lambda c: c * 9/5 + 32, "Кельвин": lambda c: c + 273.15},
                "Фаренгейт": {"Цельсий": lambda f: (f - 32) * 5/9, "Кельвин": lambda f: (f - 32) * 5/9 + 273.15},
                "Кельвин": {"Цельсий": lambda k: k - 273.15, "Фаренгейт": lambda k: (k - 273.15) * 9/5 + 32}
            },
            "Объем": {
                "Литр": {"Миллилитр": 1000, "Галлон": 0.264172, "Кубический метр": 0.001, "Пинта": 2.11338},
                "Миллилитр": {"Литр": 0.001, "Галлон": 0.000264172, "Кубический метр": 0.000001, "Пинта": 0.00211338},
                "Галлон": {"Литр": 3.78541, "Миллилитр": 3785.41, "Кубический метр": 0.00378541, "Пинта": 8},
                "Кубический метр": {"Литр": 1000, "Миллилитр": 1000000, "Галлон": 264.172, "Пинта": 2113.38},
                "Пинта": {"Литр": 0.473176, "Миллилитр": 473.176, "Галлон": 0.125, "Кубический метр": 0.000473176}
            },
            "Скорость": {
                "Км/ч": {"М/с": 0.277778, "Миль/ч": 0.621371, "Узел": 0.539957},
                "М/с": {"Км/ч": 3.6, "Миль/ч": 2.23694, "Узел": 1.94384},
                "Миль/ч": {"Км/ч": 1.60934, "М/с": 0.44704, "Узел": 0.868976},
                "Узел": {"Км/ч": 1.852, "М/с": 0.514444, "Миль/ч": 1.15078}
            },
            "Площадь": {
                "Квадратный метр": {"Квадратный километр": 0.000001, "Гектар": 0.0001, "Квадратная миля": 3.861e-7, "Акр": 0.000247105},
                "Квадратный километр": {"Квадратный метр": 1000000, "Гектар": 100, "Квадратная миля": 0.386102, "Акр": 247.105},
                "Гектар": {"Квадратный метр": 10000, "Квадратный километр": 0.01, "Квадратная миля": 0.00386102, "Акр": 2.47105},
                "Квадратная миля": {"Квадратный метр": 2590000, "Квадратный километр": 2.59, "Гектар": 259, "Акр": 640},
                "Акр": {"Квадратный метр": 4046.86, "Квадратный километр": 0.00404686, "Гектар": 0.404686, "Квадратная миля": 0.0015625}
            }
        }
        

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        

        self.title_label = ctk.CTkLabel(self.main_frame, text="Универсальный конвертер единиц измерения", 
                                       font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(0, 20))
        

        self.converter_frame = ctk.CTkFrame(self.main_frame)
        self.converter_frame.pack(pady=10, padx=20, fill="both", expand=True)
        

        self.category_label = ctk.CTkLabel(self.converter_frame, text="Выберите категорию:", 
                                         font=ctk.CTkFont(size=16))
        self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.category_var = tk.StringVar()
        self.category_combobox = ctk.CTkComboBox(self.converter_frame, values=list(self.conversion_data.keys()),
                                              variable=self.category_var, width=200,
                                              command=self.update_unit_options)
        self.category_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.category_combobox.set("Длина")
        

        self.from_label = ctk.CTkLabel(self.converter_frame, text="Из:", 
                                      font=ctk.CTkFont(size=16))
        self.from_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.from_var = tk.StringVar()
        self.from_combobox = ctk.CTkComboBox(self.converter_frame, values=list(self.conversion_data["Длина"].keys()),
                                           variable=self.from_var, width=200,
                                           command=self.update_to_units)
        self.from_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.from_combobox.set(list(self.conversion_data["Длина"].keys())[0])
        

        self.to_label = ctk.CTkLabel(self.converter_frame, text="В:", 
                                    font=ctk.CTkFont(size=16))
        self.to_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.to_var = tk.StringVar()
        self.to_combobox = ctk.CTkComboBox(self.converter_frame, 
                                         values=list(self.conversion_data["Длина"][list(self.conversion_data["Длина"].keys())[0]].keys()),
                                         variable=self.to_var, width=200)
        self.to_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.to_combobox.set(list(self.conversion_data["Длина"][list(self.conversion_data["Длина"].keys())[0]].keys())[0])
        

        self.value_label = ctk.CTkLabel(self.converter_frame, text="Значение:", 
                                       font=ctk.CTkFont(size=16))
        self.value_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.value_entry = ctk.CTkEntry(self.converter_frame, width=200)
        self.value_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.value_entry.insert(0, "1")
        

        self.convert_button = ctk.CTkButton(self.converter_frame, text="Конвертировать", 
                                          command=self.convert, width=150, 
                                          font=ctk.CTkFont(size=16, weight="bold"))
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)
        

        self.result_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.result_frame.pack(pady=10, padx=20, fill="x")
        
        self.result_label = ctk.CTkLabel(self.result_frame, text="Результат:", 
                                        font=ctk.CTkFont(size=16))
        self.result_label.pack(side="left", padx=10)
        
        self.result_value = ctk.CTkLabel(self.result_frame, text="", 
                                        font=ctk.CTkFont(size=18, weight="bold"))
        self.result_value.pack(side="left", padx=10)

        self.update_unit_options(self.category_var.get())
        
    def update_unit_options(self, category):

        self.from_combobox.configure(values=list(self.conversion_data[category].keys()))
        self.from_combobox.set(list(self.conversion_data[category].keys())[0])
        self.update_to_units(list(self.conversion_data[category].keys())[0])
        
    def update_to_units(self, from_unit):

        category = self.category_var.get()
        self.to_combobox.configure(values=list(self.conversion_data[category][from_unit].keys()))
        self.to_combobox.set(list(self.conversion_data[category][from_unit].keys())[0])
    
    def convert(self):

        try:
            value = float(self.value_entry.get())
            category = self.category_var.get()
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            

            conversion_factor = self.conversion_data[category][from_unit][to_unit]
            
   
            if callable(conversion_factor):
                result = conversion_factor(value)
            else:
                result = value * conversion_factor
            

            formatted_result = f"{value} {from_unit} = {result:.6g} {to_unit}"
            self.result_value.configure(text=formatted_result)
            
        except ValueError:
            self.result_value.configure(text="Ошибка: введите числовое значение")
        except Exception as e:
            self.result_value.configure(text=f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = UnitConverterApp()
    app.mainloop()