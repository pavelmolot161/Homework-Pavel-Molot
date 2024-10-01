
### - Модуль 11_3

def introspection_info(obj):
    тип_объекта = type(obj)
    атриб_мет = dir(obj)
    модуль = getattr(obj, 'module', None)
    return {f'type: {тип_объекта}, methods: {атриб_мет}, module {модуль}'}
number_info = introspection_info(42)
print(number_info)
