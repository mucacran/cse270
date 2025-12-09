# CSE 270 - Python Programming Projects

Este repositorio contiene varios proyectos de programación en Python para el curso CSE 270.

> **🚀 New to this project? Start here:** [QUICKSTART.md](QUICKSTART.md)  
> **📖 Full documentation:** [README.md](#) (English) | [README.es.md](README.es.md) (Español)

## ¿Qué es este proyecto? (What is this project?)

Este repositorio incluye tres componentes principales:

### 1. **Tests Directory** - Ejercicios de Programación en Python
Contiene ejercicios de práctica para aprender conceptos fundamentales de Python:

- **`list_manager.py`** - **REQUIERE IMPLEMENTACIÓN**: Módulo para gestionar listas
- **`examples.py`** - Ejemplos de funciones con pruebas unitarias
- **`build_sentences.py`** - Generador de oraciones aleatorias usando archivos JSON

### 2. **directorydata_service** - Aplicación Django
Servicio web Django para gestión de datos de directorio:
- Aplicación completa con Django 4.2.1
- Incluye apps para `data` y `users`
- Base de datos SQLite3

### 3. **teton** - Frontend Web
Interfaz web HTML/CSS/JavaScript (versión 1.5)

## ¿Qué hay que hacer? (What needs to be done?)

### TAREA PRINCIPAL: Implementar `list_manager.py`

El archivo `/tests/list_manager.py` contiene funciones stub que necesitan ser implementadas. Ya existen pruebas completas en `test_list_manager.py`.

#### Funciones a implementar:

```python
def get_list():
    """Retorna la lista my_list"""
    pass

def reset_list():
    """Vacía la lista my_list"""
    pass

def add_to_list(item):
    """Agrega un elemento a my_list"""
    pass

def remove_from_list(item):
    """Remueve un elemento de my_list
    Lanza ValueError si el elemento no existe"""
    pass

def replace_item_in_list(item, replacement):
    """Reemplaza un elemento en my_list
    Lanza ValueError si el elemento no existe"""
    pass

def get_item_at_position(position):
    """Retorna el elemento en la posición dada (1-based indexing)
    Lanza ValueError si la posición es inválida (<1 o > longitud)"""
    pass
```

## Estructura del Proyecto

```
cse270/
├── tests/                      # Ejercicios de Python
│   ├── list_manager.py        # ⚠️ NECESITA IMPLEMENTACIÓN
│   ├── test_list_manager.py   # Pruebas para list_manager
│   ├── examples.py            # Ejemplos de funciones
│   ├── test_examples.py       # Pruebas para examples
│   ├── build_sentences.py     # Generador de oraciones
│   ├── test_build_sentences.py
│   └── word_lists.json        # Datos para el generador
│
├── directorydata_service/     # Aplicación Django
│   ├── manage.py
│   ├── directorydata_service/ # Configuración del proyecto
│   ├── data/                  # App de datos
│   └── users/                 # App de usuarios
│
└── teton/                     # Frontend web
    └── 1.5/                   # Versión actual
```

## Cómo Ejecutar (How to Run)

### Prerrequisitos
```bash
# Instalar Python 3.8 o superior
python --version

# Instalar dependencias (si existe requirements.txt)
pip install -r requirements.txt

# O instalar manualmente:
pip install django pytest pytest-mock psycopg2-binary
```

### Ejecutar Pruebas del List Manager
```bash
cd tests
pytest test_list_manager.py -v
```

### Ejecutar Todas las Pruebas
```bash
cd tests
pytest -v
```

### Ejecutar Pruebas Específicas
```bash
cd tests
pytest test_examples.py -v
pytest test_build_sentences.py -v
```

### Ejecutar la Aplicación Django
```bash
cd directorydata_service
python manage.py migrate
python manage.py runserver
```

Luego visita http://localhost:8000 en tu navegador.

### Ejecutar el Generador de Oraciones
```bash
cd tests
python build_sentences.py
# Ingresa una palabra de al menos 7 letras cuando se solicite
```

## Requisitos de las Funciones

### `get_list()`
- Debe retornar la lista global `my_list`
- No debe modificar la lista

### `reset_list()`
- Debe vaciar completamente la lista `my_list`
- Después de llamar, `len(my_list)` debe ser 0

### `add_to_list(item)`
- Debe agregar `item` al final de `my_list`
- Mantiene el orden de inserción

### `remove_from_list(item)`
- Debe remover la primera ocurrencia de `item` de `my_list`
- Debe lanzar `ValueError` si `item` no está en la lista

### `replace_item_in_list(item, replacement)`
- Debe encontrar `item` en `my_list` y reemplazarlo con `replacement`
- Debe lanzar `ValueError` si `item` no está en la lista
- Solo reemplaza la primera ocurrencia

### `get_item_at_position(position)`
- Usa indexación 1-based (position 1 = primer elemento)
- Debe retornar el elemento en la posición dada
- Debe lanzar `ValueError` si:
  - position < 1
  - position > longitud de la lista

## Ejemplos de Implementación

Aquí hay pistas sobre cómo implementar las funciones:

```python
# Ejemplo: Acceder a la lista global
def get_list():
    global my_list
    return my_list

# Ejemplo: Modificar la lista global
def reset_list():
    global my_list
    my_list = []  # o my_list.clear()

# Ejemplo: Manejar excepciones
def remove_from_list(item):
    global my_list
    if item not in my_list:
        raise ValueError("Item not found")
    my_list.remove(item)
```

## Verificar tu Trabajo

Después de implementar las funciones, ejecuta:

```bash
cd tests
pytest test_list_manager.py -v
```

Todas las pruebas deben pasar (verde):
```
test_get_list PASSED
test_reset_list PASSED
test_add_to_list PASSED
test_remove_from_list PASSED
test_remove_from_list_missing_value PASSED
test_replace_item PASSED
test_replace_item_missing_value PASSED
test_get_item_at_position PASSED
test_get_item_at_position_5 PASSED
test_get_item_at_bad_position PASSED
```

## Recursos Adicionales

- **Python Lists**: https://docs.python.org/3/tutorial/datastructures.html
- **Python Exceptions**: https://docs.python.org/3/tutorial/errors.html
- **Pytest Documentation**: https://docs.pytest.org/
- **Django Documentation**: https://docs.djangoproject.com/

## Notas Importantes

- ⚠️ **No modifiques los archivos de prueba** - Solo implementa las funciones en `list_manager.py`
- ✅ **Usa `global my_list`** cuando necesites modificar la lista global
- ✅ **Lanza `ValueError`** cuando se especifica en los requisitos
- ✅ **Recuerda**: `get_item_at_position` usa indexación 1-based, no 0-based

## Licencia

Este es un proyecto educativo para CSE 270.
