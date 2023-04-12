class Integer:
    def __set_name__(self, owner, name):
        self._instance_name = f"int_field_{name}"

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Только цело число!")
        print(f"{self._instance_name} --> {value}")
        return setattr(instance, self._instance_name, value)

    def __get__(self, instance, owner):
        if instance is None or owner is None:
            return
        return getattr(instance, self._instance_name)

    def __delete__(self, instance):
        print(f"{self._instance_name} удалено")
        return delattr(instance, self._instance_name)


class String:
    def __set_name__(self, owner, name):
        self._instance_name = f"str_field_{name}"

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Только строка!")
        print(f"{self._instance_name} --> {value}")
        return setattr(instance, self._instance_name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return
        return getattr(instance, self._instance_name)

    def __delete__(self, instance):
        print(f"{self._instance_name} удалено")
        return delattr(instance, self._instance_name)


class PositiveInteger:
    def __set_name__(self, owner, name):
        self._instance_name = f"pos_int_field_{name}"

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("Только целое положительное число!")
        print(f"{self._instance_name} --> {value}")
        return setattr(instance, self._instance_name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return
        return getattr(instance, self._instance_name)

    def __delete__(self, instance):
        print(f"{self._instance_name} удалено")
        return delattr(instance, self._instance_name)
