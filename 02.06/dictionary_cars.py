cars = {
    "SUV": {
        "Luxury": {
            "Electric": {
                "Tesla": {
                    "Model X": {
                        "Year": "2022",
                        "Price": "$90,000"
                    }
                },
                "Jaguar": {
                    "F-TYPE": {
                        "Year": "2021",
                        "Price": "$70,000"
                    }
                }
            },
            "Gasoline": {
                "Mercedes-Benz": {
                    "GLE": {
                        "Year": "2022",
                        "Price": "$70,000"
                    }
                },
                "BMW": {
                    "X7": {
                        "Year": "2022",
                        "Price": "$75,000"
                    }
                }
            }
        },
        "Non-Luxury": {
            "Gasoline": {
                "Jeep": {
                    "Cherokee": {
                        "Year": "2022",
                        "Price": "$40,000"
                    }
                },
                "Ford": {
                    "Explorer": {
                        "Year": "2022",
                        "Price": "$45,000"
                    }
                }
            }
        }
    },
    "Sedan": {
        "Luxury": {
            "Electric": {
                "Tesla": {
                    "Model S": {
                        "Year": "2022",
                        "Price": "$80,000"
                    }
                },
                "Audi": {
                    "e-tron": {
                        "Year": "2022",
                        "Price": "$65,000"
                    }
                }
            },
            "Gasoline": {
                "Mercedes-Benz": {
                    "S-Class": {
                        "Year": "2022",
                        "Price": "$90,000"
                    }
                },
                "BMW": {
                    "7 Series": {
                        "Year": "2022",
                        "Price": "$85,000"
                    }
                }
            }
        },
        "Non-Luxury": {
            "Gasoline": {
                "Toyota": {
                    "Camry": {
                        "Year": "2022",
                        "Price": "$25,000"
                    }
                },
                "Honda": {
                    "Accord": {
                        "Year": "2022",
                        "Price": "$30,000"
                    }
                }
            }
        }
    }
}

print(cars["Sedan"]["Non-Luxury"]["Gasoline"]["Honda"])
