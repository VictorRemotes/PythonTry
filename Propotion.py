import fractions


class Propotion:

    def __init__(self, sort, code, name, percent):
        self.Sort = sort
        self.Code = code
        self.Name = name
        self.Percent = fractions.Fraction(percent[:-1])

    def __repr__(self):
        return(
            f'class Propotion {{'
            f'Sort={self.Sort}'
            f'Code={self.Code}'
            f'Name={self.Name}'
            f'Percent={float(self.Percent):.4f}%'
            f'}}'
        )
