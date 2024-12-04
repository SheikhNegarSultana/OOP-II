class Automobile:
    def __init__(self, paint_color):
        self.__paint_color = paint_color

    def get_paint_color(self):
        return self.__paint_color

    def set_paint_color(self, paint_color):
        self.__paint_color = paint_color

    def display_info(self):
        print(f"Paint Color: {self.__paint_color}")


class Sedan(Automobile):
    def __init__(self, paint_color, model, seat_count, engine_type):
        super().__init__(paint_color)
        self.__model = model
        self.__seat_count = seat_count
        self.__engine_type = engine_type

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_seat_count(self):
        return self.__seat_count

    def set_seat_count(self, seat_count):
        self.__seat_count = seat_count

    def get_engine_type(self):
        return self.__engine_type

    def set_engine_type(self, engine_type):
        self.__engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Model: {self.__model}")
        print(f"Seat Count: {self.__seat_count}")
        print(f"Engine Type: {self.__engine_type}")


# Create instances
sedan1 = Sedan("Red", "Audi A4", 5, "Petrol")
sedan2 = Sedan("Black", "Mercedes E-Class", 5, "Diesel")

# Access and modify properties
sedan1.set_model("Audi A6")
sedan2.set_engine_type("Electric")

# Display automobile information
sedan1.display_info()
sedan2.display_info()
