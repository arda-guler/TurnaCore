class Binary:
    def __init__(self, value=0):
        # Ensure the value is within the range of a 16-bit binary number
        if value < 0 or value > 65535:
            raise ValueError("Value must be between 0 and 65535 inclusive.")
        self.value = value

    def __repr__(self):
        return f"Binary({self.value})"

    def __str__(self):
        return bin(self.value)[2:].zfill(16)  # Pad with zeros to ensure 16 bits

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, Binary):
            return False
        return self.value == other.value

    def __add__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        result = self.value + other.value
        return Binary(result & 0xFFFF)  # Keep only the lowest 16 bits

    def __sub__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        result = self.value - other.value
        return Binary(result & 0xFFFF)  # Keep only the lowest 16 bits

    def __lt__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        return self.value < other.value

    def __le__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        return self.value <= other.value

    def __gt__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Unsupported operand type: must be Binary")
        return self.value >= other.value
