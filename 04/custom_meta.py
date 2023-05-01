class CustomMeta(type):
    def __new__(mcs, name, bases, attr):
        new_attr = {}
        for item in attr:
            if not item[:2] == "__" and not item[-2:] == "__":
                new_attr[f"custom_{item}"] = attr[item]
            else:
                new_attr[item] = attr[item]

        def custom_setattr(self, key, value):
            if not key[:2] == "__" and not key[-2:] == "__":
                super(self.__class__, self).__setattr__(f"custom_{key}", value)
            else:
                super(self.__class__, self).__setattr__(key, value)

        new_attr["__setattr__"] = custom_setattr

        return super().__new__(mcs, name, bases, new_attr)
