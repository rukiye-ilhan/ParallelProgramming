custom_power = lambda x = 0,/,e = 1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *,c: int = 1) -> float:
    """
    Takes arguments in the correct order and format according to the specified parameter types and calculates the sum of two numbers raised to powers, then divides the result by a third number.

    :param x: The base for the exponentiation operation .  only positionally. Default value is 0.
    :type x: int, float
    :param y: The base for the exponentiation operation  only  positionally. Default value is 0.
    :type y: int, float
    :param a: The exponent for the x value . positionally or  a keyword . Default value is 1.
    :type a: int
    :param b: The exponent for the y value positionally or  a keyword argument. Default value is 1.
    :type b: int
    :param c: The number by which the total result of the exponentiation sum will be divided only  a keyword argument. This is a required parameter.
    :type c: int, float
    :return: Returns the result of the expression (x^a + y^b) / c.
    :rtype: float
    :raises ZeroDivisionError: Raises this error if c is zero.

    Example:

    .. code-block:: python

        result = custom_equation(3, 5, a=2, b=3, c=4)
        print(result)  # Output: 5.2
    """
    return (x ** a + y ** b) / c
print(custom_equation(3, 5, a=2, b=3, c=4))


class Counter:
    def __init__(self):
        self.counter = 0
        self.dict_ = {}

    def fn_w_counter(self) -> tuple[int, dict[str, int]]:
        self.counter += 1
        caller_function_name = __name__

        if caller_function_name in self.dict_:
            self.dict_[caller_function_name] += 1
        else:
            self.dict_[caller_function_name] = 1

        return (self.counter, self.dict_)


# Counter nesnesi oluşturulur oluşan nesne üzeridne  sınıfın metotoları(fonkdsiyonları) çağrılır
counter_instance = Counter()

for i in range(10):
    counter_instance.fn_w_counter()

result = counter_instance.fn_w_counter()
