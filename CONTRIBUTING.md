# Contributing to CSE 270

Thank you for your interest in contributing to the CSE 270 project!

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Python and testing

### Setup Development Environment

1. **Clone the repository**
```bash
git clone https://github.com/mucacran/cse270.git
cd cse270
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Project Structure

```
cse270/
├── tests/                      # Python exercises and tests
│   ├── list_manager.py        # Main exercise file
│   ├── test_*.py              # Test files
│   └── *.json                 # Data files
├── directorydata_service/     # Django application
├── teton/                     # Web frontend
├── README.md                  # English documentation
├── README.es.md               # Spanish documentation
└── requirements.txt           # Python dependencies
```

## Running Tests

### Run All Tests
```bash
cd tests
pytest -v
```

### Run Specific Test File
```bash
cd tests
pytest test_list_manager.py -v
```

### Run Single Test Function
```bash
cd tests
pytest test_list_manager.py::test_get_list -v
```

### Run with Coverage
```bash
cd tests
pytest --cov=. --cov-report=html
```

## Django Application

### Initial Setup
```bash
cd directorydata_service
python manage.py migrate
python manage.py createsuperuser  # Optional
```

### Run Development Server
```bash
python manage.py runserver
```

### Run Django Tests
```bash
python manage.py test
```

## Code Style Guidelines

### Python Style
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names

### Example
```python
# Good
def add_to_list(item):
    """Add an item to the global list."""
    global my_list
    my_list.append(item)

# Avoid
def add(x):
    global my_list
    my_list.append(x)
```

### Documentation
- Add docstrings to all functions
- Include examples in docstrings when helpful
- Keep comments concise and relevant

```python
def get_item_at_position(position):
    """
    Get item at the specified position (1-based indexing).
    
    Args:
        position (int): Position of the item (1 to len(list))
        
    Returns:
        The item at the specified position
        
    Raises:
        ValueError: If position is < 1 or > list length
        
    Examples:
        >>> reset_list()
        >>> add_to_list("A")
        >>> get_item_at_position(1)
        'A'
    """
    # Implementation here
```

## Testing Guidelines

### Writing Tests
- Test one thing per test function
- Use descriptive test names
- Follow Arrange-Act-Assert pattern
- Test both success and failure cases

```python
def test_remove_from_list():
    # Arrange
    reset_list()
    add_to_list("item")
    
    # Act
    remove_from_list("item")
    result = get_list()
    
    # Assert
    assert len(result) == 0, "Item was not removed"

def test_remove_from_list_missing_value():
    # Arrange
    reset_list()
    add_to_list("item")
    
    # Assert
    with pytest.raises(ValueError):
        remove_from_list("different_item")
```

### Test Coverage
- Aim for 100% coverage of your code
- Test edge cases (empty lists, invalid inputs, etc.)
- Test error conditions

## Git Workflow

### Branching Strategy
```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Commit your changes
git add .
git commit -m "Add feature: description"

# Push to GitHub
git push origin feature/your-feature-name
```

### Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issues when applicable

Examples:
```
Add implementation for list_manager functions
Fix bug in get_item_at_position validation
Update README with setup instructions
Add tests for edge cases in remove_from_list
```

## Pull Request Process

1. **Before Creating PR**
   - Ensure all tests pass
   - Update documentation if needed
   - Check code style
   - Verify no unnecessary files are included

2. **Creating the PR**
   - Provide a clear title
   - Describe what changes you made and why
   - Reference any related issues
   - Add screenshots for UI changes

3. **After Creating PR**
   - Respond to feedback promptly
   - Make requested changes
   - Update the PR description if scope changes

## Common Issues and Solutions

### Issue: Tests fail with "ModuleNotFoundError"
**Solution**: Make sure you're in the correct directory and have installed dependencies
```bash
cd tests
pip install -r ../requirements.txt
pytest -v
```

### Issue: Django migrations not working
**Solution**: Delete the database and recreate it
```bash
cd directorydata_service
rm db.sqlite3
python manage.py migrate
```

### Issue: "global name 'my_list' is not defined"
**Solution**: Add `global my_list` at the start of functions that modify the list
```python
def reset_list():
    global my_list  # This is required
    my_list = []
```

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Documentation](https://git-scm.com/doc)

## Questions?

If you have questions or need help:
1. Check existing issues on GitHub
2. Review the README files (README.md, README.es.md)
3. Open a new issue with your question

## License

This is an educational project for CSE 270.
