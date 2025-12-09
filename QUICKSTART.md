# Quick Start Guide - CSE 270

## English Version

### What Is This?
This is a Python programming exercises repository for CSE 270. The main task is to implement functions in `tests/list_manager.py`.

### What You Need To Do

**Implement 6 functions in `tests/list_manager.py`:**
1. `get_list()` - Return the list
2. `reset_list()` - Empty the list
3. `add_to_list(item)` - Add an item
4. `remove_from_list(item)` - Remove an item (raise ValueError if not found)
5. `replace_item_in_list(item, replacement)` - Replace an item (raise ValueError if not found)
6. `get_item_at_position(position)` - Get item at position (1-based, raise ValueError if invalid)

### Setup & Run (5 Minutes)

```bash
# 1. Clone and setup
git clone https://github.com/mucacran/cse270.git
cd cse270
pip install -r requirements.txt

# 2. Edit the file
# Open tests/list_manager.py and implement the functions

# 3. Run tests
cd tests
pytest test_list_manager.py -v

# Success when you see 10 passed! ✓
```

### Key Tips
- Use `global my_list` in functions that modify the list
- Use `raise ValueError()` for error cases
- `get_item_at_position` uses 1-based indexing (position 1 = first item)

### Full Documentation
- **English**: [README.md](README.md)
- **Spanish**: [README.es.md](README.es.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Versión en Español

### ¿Qué Es Esto?
Este es un repositorio de ejercicios de programación en Python para CSE 270. La tarea principal es implementar funciones en `tests/list_manager.py`.

### ¿Qué Necesitas Hacer?

**Implementar 6 funciones en `tests/list_manager.py`:**
1. `get_list()` - Retornar la lista
2. `reset_list()` - Vaciar la lista
3. `add_to_list(item)` - Agregar un elemento
4. `remove_from_list(item)` - Eliminar un elemento (lanzar ValueError si no existe)
5. `replace_item_in_list(item, replacement)` - Reemplazar un elemento (lanzar ValueError si no existe)
6. `get_item_at_position(position)` - Obtener elemento en posición (base 1, lanzar ValueError si inválido)

### Configuración y Ejecución (5 Minutos)

```bash
# 1. Clonar y configurar
git clone https://github.com/mucacran/cse270.git
cd cse270
pip install -r requirements.txt

# 2. Editar el archivo
# Abre tests/list_manager.py e implementa las funciones

# 3. Ejecutar pruebas
cd tests
pytest test_list_manager.py -v

# ¡Éxito cuando veas 10 passed! ✓
```

### Consejos Clave
- Usa `global my_list` en funciones que modifican la lista
- Usa `raise ValueError()` para casos de error
- `get_item_at_position` usa indexación base 1 (posición 1 = primer elemento)

### Documentación Completa
- **Inglés**: [README.md](README.md)
- **Español**: [README.es.md](README.es.md)
- **Contribuir**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Example Implementation Hint

```python
# Example of how to implement a simple function:

def get_list():
    """Return the current list."""
    global my_list
    return my_list

def add_to_list(item):
    """Add an item to the list."""
    global my_list
    my_list.append(item)

# Your turn to implement the rest!
```

---

## Testing Your Work

```bash
# Run all tests
cd tests
pytest test_list_manager.py -v

# Run a single test
pytest test_list_manager.py::test_get_list -v

# Expected output when complete:
# ========== 10 passed in 0.05s ==========
```

---

## Project Structure

```
cse270/
├── tests/
│   ├── list_manager.py        ← YOU IMPLEMENT THIS
│   ├── test_list_manager.py   ← Tests (don't modify)
│   └── ...
├── directorydata_service/     ← Django app
├── teton/                     ← Web frontend
└── requirements.txt           ← Dependencies
```

---

## Need Help?

1. **Read the full documentation**: See [README.md](README.md) or [README.es.md](README.es.md)
2. **Check the tests**: Look at `test_list_manager.py` to understand what's expected
3. **Review Python lists**: https://docs.python.org/3/tutorial/datastructures.html
4. **Ask questions**: Open an issue on GitHub

---

## Success Criteria

✓ All 10 tests pass  
✓ No `pass` statements remain in your code  
✓ Functions handle edge cases (empty lists, invalid positions)  
✓ ValueError raised when appropriate  

Good luck! / ¡Buena suerte! 🚀
