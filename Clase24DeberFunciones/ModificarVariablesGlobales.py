
mi_variable_global = 30

def cambiar_variable_global():
    global mi_variable_global  
    mi_variable_global = 50  
    print(f"Variable global mi_variable_global modificada dentro de la función: {mi_variable_global}")

cambiar_variable_global()

print(f"Variable global mi_variable_global fuera de la función: {mi_variable_global}")