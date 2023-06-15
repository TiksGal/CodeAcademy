def kmi(weight: int, height: float) -> float:
    if weight < 20 or weight > 200:
        raise ValueError("Invalid weight value. Weight should be between 20 and 200 kg.")
    if height < 1 or height > 3:
        raise ValueError("Invalid height value. Height should be between 1 and 3 meters.")

    kmi = weight / (height ** 2)
    return kmi
