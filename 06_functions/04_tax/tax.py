def calc_tax(amount, tax_rate):

    if not isinstance(amount, (int, float)):
        raise TypeError('')
    if not amount > 0:
        raise ValueError('')

    if not isinstance(tax_rate, (int, float)):
        raise TypeError('')
    if not 0 < tax_rate < 1:
        raise ValueError('')

    return amount * tax_rate
