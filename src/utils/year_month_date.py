def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


def _min_year() -> int:
    return 1


def _max_year() -> int:
    return 9999


class YearMonthDate:
    __slots__ = "_year", "_month", "_hashcode"

    def __new__(cls, year: int, month: int):
        if month is None and isinstance(year, (bytes, str)) and len(year) == 4 and 1 <= ord(year[2:3]) <= 12:
            # Pickle support
            if isinstance(year, str):
                try:
                    year = year.encode('latin1')
                except UnicodeEncodeError:
                    # More informative error message.
                    raise ValueError(
                        "Failed to encode latin1 string when unpickling "
                        "a date object. "
                        "pickle.load(data, encoding='latin1') is assumed.")
            self = object.__new__(cls)
            self.__setstate(year)
            self._hashcode = -1
            return self
        year, month = cls._check_date_fields(year, month)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._hashcode = -1
        return self

    def iso_format(self):
        return "%04d-%02d" % (self._year, self._month)

    __str__ = iso_format

    def __setstate(self, string):
        yhi, ylo, self._month = string
        self._year = yhi * 256 + ylo

    @classmethod
    def _check_date_fields(cls, year, month):
        year = int(year)
        month = int(month)
        if not _min_year() <= year <= _max_year():
            raise ValueError('year must be in %d..%d' % (_min_year(), _max_year()), year)
        if not 1 <= month <= 12:
            raise ValueError('month must be in 1..12', month)
        return year, month

    @property
    def year(self):
        """year (1-9999)"""
        return self._year

    @property
    def month(self):
        """month (1-12)"""
        return self._month

    def _cmp(self, other):
        assert isinstance(other, YearMonthDate)
        y, m = self._year, self._month
        y2, m2 = other._year, other._month
        return _cmp((y, m), (y2, m2))

    def __eq__(self, other):
        if isinstance(other, YearMonthDate):
            return self._cmp(other) == 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, YearMonthDate):
            return self._cmp(other) <= 0
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, YearMonthDate):
            return self._cmp(other) < 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, YearMonthDate):
            return self._cmp(other) >= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, YearMonthDate):
            return self._cmp(other) > 0
        return NotImplemented
