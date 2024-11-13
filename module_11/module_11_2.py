def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [
            attr
            for attr in dir(obj)
            if not callable(getattr(obj, attr)) and not attr.startswith('__')
        ],
        'methods': [
            method
            for method in dir(obj)
            if callable(getattr(obj, method)) and not method.startswith('__')
        ],
        'module': getattr(obj, '__module__', None),
    }

    # Дополнительные свойства
    if isinstance(obj, (list, dict, set)):
        info['length'] = len(obj)

    return info


# Пример использования
class MyClass:
    def __init__(self):
        self.attribute1 = 'Hello'

    @staticmethod
    def my_method():
        return 'Method called'


number_info = introspection_info(42)
print(number_info)

my_object = MyClass()
object_info = introspection_info(my_object)
print(object_info)
