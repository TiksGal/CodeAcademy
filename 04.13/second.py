# Sukurkite klasę pavadinimu MyQueue, kurioje apibrėžti __bool__, __repr__ ir __len__ metodai.
# Metodas __bool__ turėtų grąžinti True, jei eilėje yra elementų, ir False, jei ji yra tuščia.
# Metodas __repr__ turėtų grąžinti eilutę formatu MyQueue(items), kur items yra eilės elementų sąrašas.
# Metodas __len__ turėtų grąžinti eilėje esančių elementų skaičių.
from typing import Optional, List


class MyQueue:
    def __init__(self) -> None:
        self.items: List[Optional: int, str, float] = []

    def __bool__(self) -> bool:
        return len(self.items) > 0

    def __repr__(self) -> str:
        return f"MyQueue({self.items})"

    def __len__(self) -> int:
        return len(self.items)


my_queue = MyQueue()
my_queue.items.append(2)
my_queue.items.append(3.14)
my_queue.items.append("hat")
print(bool(my_queue))
print(my_queue)
print(len(my_queue))





