# CSE 270 - Proyectos de Programación Python

## Introducción

Este repositorio contiene ejercicios prácticos de programación en Python para el curso CSE 270. El objetivo principal es aprender a trabajar con listas, funciones, pruebas unitarias y desarrollo web con Django.

## Contenido del Repositorio

### 📁 tests/ - Ejercicios de Python
Contiene ejercicios de práctica con sus respectivas pruebas:
- **list_manager.py**: Funciones para gestionar una lista (necesita implementación)
- **examples.py**: Ejemplos de funciones con diferentes patrones de prueba
- **build_sentences.py**: Generador de oraciones aleatorias

### 📁 directorydata_service/ - Aplicación Django
Servicio web completo construido con Django que incluye:
- Gestión de datos
- Gestión de usuarios
- Base de datos SQLite3

### 📁 teton/ - Frontend Web
Interfaz de usuario HTML/CSS/JavaScript

## 🎯 Tarea Principal: Implementar list_manager.py

### ¿Qué hacer?

Debes implementar las siguientes funciones en el archivo `tests/list_manager.py`:

#### 1. `get_list()`
**Propósito**: Obtener la lista actual  
**Retorna**: La lista `my_list`  
**Ejemplo**:
```python
reset_list()
add_to_list("manzana")
resultado = get_list()  # ["manzana"]
```

#### 2. `reset_list()`
**Propósito**: Limpiar completamente la lista  
**Efecto**: La lista queda vacía  
**Ejemplo**:
```python
add_to_list("A")
add_to_list("B")
reset_list()
get_list()  # []
```

#### 3. `add_to_list(item)`
**Propósito**: Agregar un elemento al final de la lista  
**Parámetro**: `item` - el elemento a agregar  
**Ejemplo**:
```python
reset_list()
add_to_list("primero")
add_to_list("segundo")
get_list()  # ["primero", "segundo"]
```

#### 4. `remove_from_list(item)`
**Propósito**: Eliminar un elemento de la lista  
**Parámetro**: `item` - el elemento a eliminar  
**Excepción**: Lanza `ValueError` si el elemento no existe  
**Ejemplo**:
```python
reset_list()
add_to_list("gato")
remove_from_list("gato")
get_list()  # []

remove_from_list("perro")  # ❌ ValueError!
```

#### 5. `replace_item_in_list(item, replacement)`
**Propósito**: Reemplazar un elemento por otro  
**Parámetros**:
- `item` - el elemento a buscar
- `replacement` - el nuevo elemento  
**Excepción**: Lanza `ValueError` si el elemento no existe  
**Ejemplo**:
```python
reset_list()
add_to_list("rojo")
replace_item_in_list("rojo", "azul")
get_list()  # ["azul"]

replace_item_in_list("verde", "amarillo")  # ❌ ValueError!
```

#### 6. `get_item_at_position(position)`
**Propósito**: Obtener el elemento en una posición específica  
**Parámetro**: `position` - posición del elemento (comienza en 1, no en 0)  
**Retorna**: El elemento en esa posición  
**Excepción**: Lanza `ValueError` si la posición es inválida  
**Ejemplo**:
```python
reset_list()
add_to_list("A")
add_to_list("B")
add_to_list("C")
get_item_at_position(1)  # "A"
get_item_at_position(2)  # "B"
get_item_at_position(3)  # "C"
get_item_at_position(0)  # ❌ ValueError!
get_item_at_position(4)  # ❌ ValueError!
```

## 🚀 Cómo Empezar

### Paso 1: Preparar el Entorno

```bash
# Clonar el repositorio (si aún no lo has hecho)
git clone https://github.com/mucacran/cse270.git
cd cse270

# Crear un entorno virtual (recomendado)
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 2: Entender las Pruebas

Antes de implementar, revisa las pruebas para entender qué se espera:

```bash
cd tests
cat test_list_manager.py
```

### Paso 3: Implementar las Funciones

Abre `tests/list_manager.py` y reemplaza cada `pass` con tu implementación.

**Pista importante**: Necesitarás usar la palabra clave `global` para modificar `my_list`:

```python
def reset_list():
    global my_list
    my_list = []
```

### Paso 4: Ejecutar las Pruebas

```bash
cd tests
pytest test_list_manager.py -v
```

Si todo está correcto, verás algo como:

```
test_get_list PASSED                    ✓
test_reset_list PASSED                  ✓
test_add_to_list PASSED                 ✓
test_remove_from_list PASSED            ✓
test_remove_from_list_missing_value PASSED ✓
test_replace_item PASSED                ✓
test_replace_item_missing_value PASSED  ✓
test_get_item_at_position PASSED        ✓
test_get_item_at_position_5 PASSED      ✓
test_get_item_at_bad_position PASSED    ✓

========== 10 passed in 0.05s ==========
```

## 📚 Conceptos Clave

### Variables Globales en Python

```python
mi_lista = []  # Variable global

def modificar_lista():
    global mi_lista  # Necesario para modificar
    mi_lista.append("nuevo")

def leer_lista():
    # No se necesita 'global' solo para leer
    return mi_lista
```

### Manejo de Excepciones

```python
def buscar_elemento(item):
    if item not in my_list:
        raise ValueError("Elemento no encontrado")
    return my_list.index(item)
```

### Operaciones con Listas

```python
# Agregar
lista.append(item)

# Eliminar (lanza ValueError si no existe)
lista.remove(item)

# Encontrar índice (lanza ValueError si no existe)
indice = lista.index(item)

# Acceso por índice
elemento = lista[0]  # Primer elemento
elemento = lista[-1]  # Último elemento

# Reemplazar
lista[indice] = nuevo_valor

# Vaciar
lista.clear()
# o
lista = []

# Verificar existencia
if item in lista:
    print("Encontrado!")
```

### Indexación 1-based vs 0-based

Python usa indexación 0-based naturalmente, pero `get_item_at_position` requiere 1-based:

```python
# 0-based (Python normal)
lista = ["A", "B", "C"]
lista[0]  # "A"
lista[1]  # "B"
lista[2]  # "C"

# 1-based (lo que necesitas)
get_item_at_position(1)  # debe retornar "A"
get_item_at_position(2)  # debe retornar "B"
get_item_at_position(3)  # debe retornar "C"

# Conversión: position_1based - 1 = index_0based
```

## 🔍 Estrategia de Resolución

### 1. Empieza Simple
Implementa primero las funciones más fáciles:
- `get_list()`
- `reset_list()`
- `add_to_list()`

### 2. Prueba Frecuentemente
Después de cada función, ejecuta las pruebas:
```bash
pytest test_list_manager.py::test_get_list -v
pytest test_list_manager.py::test_reset_list -v
```

### 3. Maneja Excepciones
Para las funciones que necesitan lanzar errores:
- `remove_from_list()`
- `replace_item_in_list()`
- `get_item_at_position()`

### 4. Verifica Todos los Casos
Asegúrate de que tus funciones pasen todos los tests, incluyendo los casos de error.

## 💡 Solución de Problemas

### Error: "name 'my_list' is not defined"
**Solución**: Agrega `global my_list` al inicio de la función.

### Error: "list index out of range"
**Solución**: Verifica los límites antes de acceder a la lista.

### Error: "ValueError not raised"
**Solución**: Asegúrate de lanzar la excepción con `raise ValueError()`.

### Las pruebas fallan después de la primera ejecución
**Solución**: Verifica que `reset_list()` limpie completamente la lista.

## 🎓 Otros Ejercicios en el Repositorio

### Generador de Oraciones (build_sentences.py)
```bash
cd tests
python build_sentences.py
# Ingresa una palabra de al menos 7 letras
```

Este programa genera oraciones aleatorias usando:
- Estructuras de oraciones predefinidas
- Listas de palabras de un archivo JSON
- Reglas gramaticales simples

### Aplicación Django
```bash
cd directorydata_service
python manage.py migrate
python manage.py runserver
```

Visita http://localhost:8000 para ver la aplicación web.

## 📖 Recursos Adicionales

- [Tutorial Oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Python Lists](https://docs.python.org/es/3/tutorial/datastructures.html)
- [Python Exceptions](https://docs.python.org/es/3/tutorial/errors.html)
- [Pytest Guía](https://docs.pytest.org/en/stable/getting-started.html)
- [Django Tutorial](https://docs.djangoproject.com/es/4.2/intro/tutorial01/)

## 🤝 Contribuir

Si encuentras errores o tienes sugerencias:
1. Abre un issue en GitHub
2. Describe el problema claramente
3. Incluye ejemplos si es posible

## ✅ Lista de Verificación

Antes de considerar tu trabajo completo:

- [ ] Todas las funciones están implementadas (no hay `pass`)
- [ ] Todas las pruebas pasan sin errores
- [ ] Las funciones manejan correctamente las excepciones
- [ ] El código está comentado donde sea necesario
- [ ] Has probado casos límite (listas vacías, posiciones inválidas, etc.)

## 📝 Conclusión

Este proyecto te ayuda a aprender:
- ✓ Manipulación de listas en Python
- ✓ Manejo de excepciones
- ✓ Pruebas unitarias con pytest
- ✓ Variables globales
- ✓ Buenas prácticas de programación

¡Buena suerte con tu implementación! 🚀
