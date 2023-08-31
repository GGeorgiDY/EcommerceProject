class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    # правим си динамично максималната дължина на gender да е 9 - понеже DoNotShow е най-дългия стринг и е с 9 букви
    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())