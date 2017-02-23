class Bruch(object):
    def __init__(self, zaehler, nenner=1):
        """
        Konstruktor der Klasse Bruch.
        :param zaehler: Zaehler des Bruchs
        :param nenner: Nenner des Bruchs
        """
        self.zaehler = zaehler
        self.nenner = nenner
        if self.nenner == 0:
            raise ZeroDivisionError
        if type(self.zaehler) == float or type(self.nenner) == float:
            raise TypeError

    def __float__(self):
        """
        :return: Gibt den Bruch mit Komma zurück -> als Float.
        """
        return float(self.zaehler) / float(self.nenner)

    def __int__(self):
        """
        :return: Gibt den bruch als Integer zurück.
        """
        return int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        :return: Invertiert den Bruch (Zaehler/Nenner) und gibt (Nenner/Zaehler)
        """
        return Bruch(self.nenner, self.zaehler)

    def __abs__(self):
        """
        :return: Gibt den absoluten(positiven) Wert des Bruches zurück.
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        :return: Gibt einen negierten Bruch zurück
        """
        return Bruch(-self.zaehler, self.nenner)

    def __pow__(self, power):
        """
        :param power: Exponent der Zahl
        :return: Gibt einen potenzierten Bruch mit power zurück
        """
        if type(power) == int or type(power) == float:
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __add__(self, other):
        """
        :param other: Bruch mit dem addiert wird
        :return: Gibt den addierten Bruch zurück
        """
        if type(other) == int:
            return Bruch((self.zaehler + other * self.nenner), self.nenner)
        elif type(other) == Bruch:
            return Bruch((self.zaehler * other.nenner + other.zaehler * self.nenner), (self.nenner * other.nenner))
        else:
            raise TypeError

    @classmethod
    def __makeBruch(cls, value):
        """
        :param value: Integer der in einen Bruch umgewandelt werden soll
        :return: Gibt einen Bruch zurück
        """
        if type(value) == int:
            return Bruch(value)
        else:
            raise TypeError

    def __iadd__(self, other):
        """
        :param other: siehe __add__
        :return: siehe __add__
        """
        return self.__add__(other)

    def __radd__(self, other):
        """
        :param other: siehe __add__
        :return: siehe __add__
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        :param other: Bruch mit dem subtrahiert wird
        :return: Gibt Differenz der beiden Brüche zurück
        """
        if type(other) == int:
            return Bruch((self.zaehler - other * self.nenner), self.nenner)
        elif type(other) == Bruch:
            return Bruch((self.zaehler * other.nenner - other.zaehler * self.nenner), (self.nenner * other.nenner))
        else:
            raise TypeError

    def __isub__(self, other):
        """
        :param other: siehe __sub__
        :return: siehe __sub__
        """
        return self.__sub__(other)

    def __rsub__(self, other):
        """
        :param other: siehe __sub__
        :return: siehe __sub__
        """
        other = Bruch(other)
        return other.__sub__(self)

    def __eq__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt True zurück wenn beide Brüche floats sind
        """
        return float(self) == float(other)

    def __ge__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt True zurück wenn der erste Bruch groesser oder gleich other ist
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt True zurück wenn der erste Bruch groesser als other ist
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt True zurück wenn der erste Bruch kleiner gleich other ist
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt True zurück wenn der erste Bruch kleiner als other ist
        """
        return float(self) < float(other)

    def __iter__(self):
        """
        :return: Gibt in dem Fall das Tuple Zaehler/Nenner zurück.
        """
        return (self.zaehler, self.nenner).__iter__()

    def __mul__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt die Multiplikation mit other zurück
        """
        if type(other) == int:
            return Bruch(self.zaehler * other, self.nenner)
        elif type(other) == Bruch:
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        else:
            raise TypeError

    def __imul__(self, other):
        """
        :param other: siehe __mul__
        :return: siehe __mul__
        """
        return self.__mul__(other)

    def __rmul__(self, other):
        """
        :param other: siehe __mul__
        :return: siehe __mul__
        """
        return self.__mul__(other)

    def __str__(self):
        """
        :return: Gibt den Bruch schön-formatierte zurück
        """
        if (self.zaehler < 0) and (self.nenner < 0):
            return "(" + str(self.zaehler * -1) + "/" + str(self.nenner * -1) + ")"
        elif self.nenner == 1:
            return "(" + str(self.zaehler) + ")"
        return "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __truediv__(self, other):
        """
        :param other: Ein Bruch
        :return: Gibt den Quotienten zurück
        """
        if type(other) == int:
            if self == 0:
                raise ZeroDivisionError
            return float(self) / float(other)
        elif type(other) == Bruch:
            if other == 0:
                raise ZeroDivisionError
            return float(self) / float(other)
        else:
            raise TypeError

    def __itruediv__(self, other):
        """
        :param other: siehe __truediv__
        :return: siehe __truediv__
        """
        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        :param other: siehe __truediv__
        :return: siehe __truediv__
        """
        return self.__truediv__(other)
