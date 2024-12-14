class CarSelection:
    def __init__(self, cars):
        self.cars = cars
        self.selected_model = None
        self.selected_car = None
        self.selected_color = None
        self.payment_method = None

    def input_number(self, prompt, max_num):
        while True:
            selected = input(prompt)
            if selected.isdigit():
                selected = int(selected)
                if 1 <= selected <= max_num:
                    return selected
                print(f"Error: Enter a number between 1 and {max_num}!")
            else:
                print("Enter numbers only!")

    def select_car_model(self):
        print("\n========================================")
        print("            Select a Model              ")
        print("========================================")
        models = list(self.cars.keys())
        for index, model in enumerate(models, start=1):
            print(f"{index} - {model}")
        print("========================================")
        choice = self.input_number("\nEnter model ID number: ", len(models))
        self.selected_model = models[choice - 1]

    def select_car(self):
        print(f"\nSelected model: {self.selected_model}")
        print("\n========================================")
        print("            Select a Car                ")
        print("========================================")
        cars = list(self.cars[self.selected_model].items())
        for index, (car, price) in enumerate(cars, start=1):
            print(f"{index} - {car}: ${price}")
        print("========================================")
        choice = self.input_number("\nEnter car ID number: ", len(cars))
        self.selected_car, self.car_price = cars[choice - 1]

    def select_color(self):
        colors = ["Black", "White", "Gray"]
        print("\n========================================")
        print("           Choose a Color               ")
        print("========================================")
        for index, color in enumerate(colors, start=1):
            print(f"{index} - {color}")
        print("========================================")
        choice = self.input_number("\nEnter color ID number: ", len(colors))
        self.selected_color = colors[choice - 1]

    def confirm_payment(self):
        print("\n========================================")
        print("            Review Details              ")
        print("========================================")
        print(
            f"Model: {self.selected_model}\nCar: {self.selected_car}\nPrice: ${self.car_price}\nColor: {self.selected_color}"
        )
        print("========================================")
        print("Do you want to buy the car?\n\n1 - Yes\n2 - No")
        choice = self.input_number("\nChoose 1 or 2: ", 2)
        if choice == 1:
            self.select_payment_method()
        else:
            print("\n========================================")
            print("          Operation Canceled!           ")
            print("========================================")

    def select_payment_method(self):
        print("\n========================================")
        print("          Select Payment Method         ")
        print("========================================")
        print("1 - Cash\n2 - Card")
        choice = self.input_number("\nChoose 1 or 2: ", 2)
        self.payment_method = "Cash" if choice == 1 else "Card"
        self.display_sales_information()

    def display_sales_information(self):
        print("\n========================================")
        print("          Payment Confirmation          ")
        print("========================================")
        print(
            f"Payment method: {self.payment_method}\nModel: {self.selected_model}\nCar: {self.selected_car}\nColor: {self.selected_color}\nPrice: ${self.car_price}\nTotal amount paid: ${self.car_price}"
        )
        print("========================================\n")


cars = {
    "sedan": {
        "Toyota Camry": 30000,
        "Honda Accord": 28000,
        "Hyundai Sonata": 27000,
    },
    "hatchback": {
        "Volkswagen Golf": 25000,
        "Ford Focus": 22000,
        "Mazda 3": 23000,
    },
    "coupe": {
        "BMW 4 Series": 45000,
        "Audi A5": 43000,
        "Chevrolet Camaro": 37000,
    },
    "minivan": {
        "Chrysler Pacifica": 35000,
        "Honda Odyssey": 34000,
        "Toyota Sienna": 36000,
    },
    "SUV": {
        "Toyota RAV4": 32000,
        "Honda CR-V": 31000,
        "Ford Explorer": 40000,
    },
}

print("========================================")
print("     Welcome to the Car Selection Program     ")
print("========================================\n")

car_selection = CarSelection(cars)
car_selection.select_car_model()
car_selection.select_car()
car_selection.select_color()
car_selection.confirm_payment()
