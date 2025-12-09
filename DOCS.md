# Project Documentation Index

## 📚 Documentation Files

This repository contains comprehensive documentation to help you understand and work with the CSE 270 projects.

### Quick Access

| Document | Purpose | Language | Best For |
|----------|---------|----------|----------|
| [QUICKSTART.md](QUICKSTART.md) | Fast 5-minute setup | 🇬🇧 🇪🇸 Both | Complete beginners |
| [README.md](README.md) | Complete documentation | 🇬🇧 English | Full reference |
| [README.es.md](README.es.md) | Documentación completa | 🇪🇸 Español | Referencia completa |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Development guide | 🇬🇧 English | Contributors |

## 🎯 Choose Your Path

### Path 1: I Just Want to Complete the Assignment
→ Go to [QUICKSTART.md](QUICKSTART.md)  
→ 5 minutes to setup, then start coding!

### Path 2: I Want to Understand Everything
→ Start with [README.md](README.md) (English) or [README.es.md](README.es.md) (Español)  
→ Deep dive into concepts and examples

### Path 3: I Want to Contribute or Extend
→ Read [CONTRIBUTING.md](CONTRIBUTING.md)  
→ Learn about testing, style guides, and workflows

## 📋 What You Need to Do

**Main Task**: Implement 6 functions in `tests/list_manager.py`

```
tests/list_manager.py
├── get_list()                    ← Return the list
├── reset_list()                  ← Empty the list
├── add_to_list(item)             ← Add an item
├── remove_from_list(item)        ← Remove an item
├── replace_item_in_list(...)     ← Replace an item
└── get_item_at_position(pos)     ← Get item at position
```

All these functions already have tests written in `test_list_manager.py`.

## 🏗️ Project Structure

```
cse270/
│
├── 📄 Documentation (START HERE!)
│   ├── QUICKSTART.md            ← 5-minute quick start
│   ├── README.md                ← Full documentation (EN)
│   ├── README.es.md             ← Documentación completa (ES)
│   ├── CONTRIBUTING.md          ← Developer guide
│   └── DOCS.md                  ← This file
│
├── 📂 tests/                    ← YOUR WORK HERE
│   ├── list_manager.py          ← ⚠️ IMPLEMENT THESE FUNCTIONS
│   ├── test_list_manager.py     ← Tests for your code
│   ├── examples.py              ← Example functions (complete)
│   ├── test_examples.py         ← Tests for examples
│   ├── build_sentences.py       ← Sentence generator (complete)
│   ├── test_build_sentences.py  ← Tests for sentence builder
│   └── word_lists.json          ← Data for sentence generator
│
├── 📂 directorydata_service/    ← Django Web Application
│   ├── manage.py                ← Django management
│   ├── directorydata_service/   ← Project settings
│   ├── data/                    ← Data app
│   └── users/                   ← Users app
│
├── 📂 teton/                    ← Web Frontend
│   └── 1.5/                     ← Version 1.5 (HTML/CSS/JS)
│
├── requirements.txt             ← Python dependencies
└── .gitignore                   ← Git ignore rules
```

## ✅ Success Checklist

Before you consider your work complete:

- [ ] Read [QUICKSTART.md](QUICKSTART.md)
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Implement all 6 functions in `tests/list_manager.py`
- [ ] Run tests: `cd tests && pytest test_list_manager.py -v`
- [ ] See "10 passed" in the test results
- [ ] No `pass` statements remain in your code
- [ ] Functions handle edge cases properly
- [ ] ValueError raised when appropriate

## 🆘 Getting Help

### Step 1: Check Documentation
1. [QUICKSTART.md](QUICKSTART.md) - Fast answers
2. [README.md](README.md) or [README.es.md](README.es.md) - Detailed info
3. [CONTRIBUTING.md](CONTRIBUTING.md) - Development details

### Step 2: Review Examples
Look at working code in `tests/examples.py` to see patterns

### Step 3: Run Tests
```bash
cd tests
pytest test_list_manager.py -v
```
Test output tells you exactly what's wrong

### Step 4: Check Test File
Read `test_list_manager.py` to understand expectations

### Step 5: Ask for Help
- Open an issue on GitHub
- Include error messages
- Describe what you tried

## 🔗 External Resources

- [Python Lists Tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## 📝 Summary

This project helps you learn:
- ✅ Python list operations
- ✅ Function implementation
- ✅ Exception handling
- ✅ Unit testing
- ✅ Working with global variables

**Time to complete**: 1-2 hours for beginners, 30 minutes for experienced programmers

**Difficulty**: Beginner to Intermediate

**Prerequisites**: Basic Python knowledge

---

## 🌟 Quick Command Reference

```bash
# Setup
git clone https://github.com/mucacran/cse270.git
cd cse270
pip install -r requirements.txt

# Test your list_manager implementation
cd tests
pytest test_list_manager.py -v

# Test everything
pytest -v

# Run Django app
cd directorydata_service
python manage.py migrate
python manage.py runserver

# Run sentence generator
cd tests
python build_sentences.py
```

---

**Ready to start?** Go to [QUICKSTART.md](QUICKSTART.md) now! 🚀
