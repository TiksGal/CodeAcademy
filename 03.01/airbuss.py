# Create a Plane, Boeing, Airbus classes.
# Base class should contain methods to get:  plane name, plane type (A320, B737 etc),
# max_speed (should be the funciotn: base_speed * model_speed_coeficient).
# Both plane subclasses should only take model type as input argument.

# class Plane:
#     def __init__(self, model: str):
#         self.model = model
#         self.name_suffix = ""

#     def get_name(self) -> str:
#         return f"{self.model}{self.name_suffix}"

#     def get_type(self) -> str:
#         raise NotImplementedError

#     def get_max_speed(self) -> float:
#         raise NotImplementedError


# class Boeing(Plane):
#     model_speed_coefficients = {"737": 0.8, "747": 0.85, "777": 0.9}

#     def __init__(self, model: str):
#         super().__init__(model)
#         self.name_suffix = " (Boeing)"

#     def get_type(self) -> str:
#         return f"B{self.model}"

#     def get_max_speed(self) -> float:
#         base_speed = 750
#         if self.model not in self.model_speed_coefficients:
#             raise ValueError(f"Invalid model: {self.model}")
#         model_speed_coefficient = self.model_speed_coefficients[self.model]
#         return base_speed * model_speed_coefficient


# class Airbus(Plane):
#     model_speed_coefficients = {"320": 0.75, "330": 0.85, "380": 0.9}

#     def __init__(self, model: str):
#         super().__init__(model)
#         self.name_suffix = " (Airbus)"

#     def get_type(self) -> str:
#         return f"A{self.model}"

#     def get_max_speed(self) -> float:
#         base_speed = 800
#         if self.model not in self.model_speed_coefficients:
#             raise ValueError(f"Invalid model: {self.model}")
#         model_speed_coefficient = self.model_speed_coefficients[self.model]
#         return base_speed * model_speed_coefficient

# my_plane = Boeing("737")
# print(my_plane.get_name())
# print(my_plane.get_type())
# print(my_plane.get_max_speed())

# my_plane = Airbus("380")
# print(my_plane.get_name())
# print(my_plane.get_type())
# print(my_plane.get_max_speed())


class Plane:
    BASE_SPEED = 750    
    def __init__(self, model_type: str, model_speed_coeficient: float, name_suffix: str)-> None:
        self.model_type = model_type        
        self.model_speed_coeficient = model_speed_coeficient        
        self.name_suffix = name_suffix    
    def get_plane_name(self)-> str:
        return self.name_suffix + self.model_type    
    def get_plane_type(self)-> str:
        return self.model_type    
    def get_max_speed(self)-> float:
        return self.model_speed_coeficient * self.BASE_SPEED
    
class Boeing(Plane):
    NAME_SUFFIX = "B"    
    BOEING_TYPE_SPEED_COEF = {
        "737" : 1,
        "747" : 1.2,
        "757" : 1.35,
        "767" : 1.5,
        "777" : 1.8,
        }
    def __init__(self, model_type: str)-> None:
        self.model_type = model_type        
        speed_coef = self._get_type_speed_coef()
        super().__init__(model_type = model_type, name_suffix = self.NAME_SUFFIX, model_speed_coeficient= speed_coef)
    def _get_type_speed_coef(self)-> float:
        return self.BOEING_TYPE_SPEED_COEF.get(self.model_type)
    
class Airbus(Plane):
    NAME_SUFFIX = "A"    
    def __init__(self, model_type: str)-> None:
        super().__init__(model_type)
        
my_plane = Boeing("747")
print(my_plane.get_plane_name())
print(f"Your plane speed is {my_plane.get_max_speed()} km/h")