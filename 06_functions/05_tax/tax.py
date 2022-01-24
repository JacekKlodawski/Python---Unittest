def calc_tax(amount, tax_rate, age):

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be an integer or a float')
    if not amount > 0:
        raise ValueError('The amount must be positive')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax rate must be a float')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax rate must be a value between 0 and 1')

    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if not age > 1:
        raise ValueError('Age must be positive')

    if age <= 18:
        return int((min(amount * tax_rate, 5000)))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int((min(amount * tax_rate, 8000)))
