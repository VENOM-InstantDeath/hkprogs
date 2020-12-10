def params(MIN=0, MAX=0, sub=None, T=[], excp=None):
    EXCP = {
            "lack_of_args": "El comando requiere al menos 1 parámetro.",
            "too_much_args": "Demasiados argumentos.",
            "intbs": "Numeric argument expected, got string"
            }
    if excp in EXCP:
        return EXCP[excp]
    if len(T) < MIN:
        return EXCP["lack_of_args"]
    if len(T) > MAX:
        return EXCP["too_much_args"]
    return None

