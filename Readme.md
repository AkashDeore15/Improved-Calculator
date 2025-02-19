# 📟 Improved Calculator

An **advanced calculator** built using **Python**, adhering to **Object-Oriented Programming (OOP)** principles, including **SOLID design patterns** and the **Factory Method**. This calculator supports **basic arithmetic operations**, maintains a **history of calculations**, and provides robust **exception handling**.

---

## 🚀 Features

✔️ **Basic Operations**: Addition, Subtraction, Multiplication, Division  
✔️ **Calculation History**: Tracks and stores past calculations  
✔️ **OOP Design**: Implements **SOLID** principles and **Factory Method** pattern  
✔️ **Robust Exception Handling**: Manages errors such as **division by zero** ([Learn More](https://www.geeksforgeeks.org/python-try-except/))  
✔️ **Command-Line Interface (CLI)**: Uses `argparse` for CLI interaction ([Read More](https://realpython.com/command-line-interfaces-python-argparse/))  
✔️ **Unit Testing with Pytest**: Generates tests dynamically using `pytest.mark.parametrize` ([See Guide](https://pytest-with-eric.com/introduction/pytest-generate-tests/))  
✔️ **Fake Data Generation**: Uses `faker` to generate test cases ([See Documentation](https://faker.readthedocs.io/en/stable/providers.html))  

---

## 🛠 Technologies & Libraries Used

| Library         | Purpose |
|----------------|---------|
| **Python** | Core programming language |
| **pytest** | Unit testing framework ([Reference](https://pytest-with-eric.com/introduction/pytest-generate-tests/)) |
| **pylint** | Static code analysis tool |
| **decimal** | Precise decimal arithmetic operations |
| **argparse** | CLI parsing ([Learn More](https://realpython.com/command-line-interfaces-python-argparse/)) |
| **faker** | Generates test data ([Udacity Guide](https://www.udacity.com/blog/2023/03/creating-fake-data-in-python-using-faker.html)) |

---

## 📂 Key Files and Their Usage

### 🔹 `main.py` (Entry Point)
- Runs the calculator and provides **CLI functionality**.
- Uses `argparse` to parse user input and execute calculations.

🔹 **Run the Calculator**:
```bash
python main.py
```
🔹 **Example Usage**:
```bash
python main.py --operation add --num1 5 --num2 3
```
➡️ Expected Output: `8`

---

### 🔹 `calculator/` (Core Logic)
- **`operations.py`** - Defines arithmetic operations (`add`, `subtract`, `multiply`, `divide`).
- **`calculator.py`** - Manages calculation execution and history.
- **`exceptions.py`** - Custom exception handling for **safe calculations** ([Python Try-Except Guide](https://www.geeksforgeeks.org/python-try-except/)).

---

### 🔹 `tests/` (Unit Testing Suite)
- **`test_operations.py`** - Validates mathematical operations.
- **`test_calculator.py`** - Ensures calculator and history management work correctly.

🔹 **Run Tests**:
```bash
pytest
```
🔹 **Run Tests with Coverage**:
```bash
pytest --cov=calculator tests/
```

🔹 **Sample Test with `pytest.mark.parametrize`** ([Guide](https://pytest-with-eric.com/introduction/pytest-generate-tests/)):
```python
import pytest
from calculator.operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

### 🔹 `requirements.txt` (Dependencies)
Lists all required dependencies.

🔹 **Install Dependencies**:
```bash
pip install -r requirements.txt
```

---

## 🔬 Manual Testing Scenarios

| Operation | Input | Expected Output |
|-----------|-------|----------------|
| Addition | `5 + 3` | `8` |
| Subtraction | `10 - 4` | `6` |
| Multiplication | `7 * 2` | `14` |
| Division | `20 / 5` | `4` |
| Division by Zero | `5 / 0` | `Error: Division by zero is undefined.` |

---

## 🤖 Fake Data Testing with `faker`

Instead of manually providing test cases, `faker` can **generate fake numerical data** for testing ([Learn More](https://www.udacity.com/blog/2023/03/creating-fake-data-in-python-using-faker.html)).

🔹 **Example Usage in Testing**:
```python
from faker import Faker
fake = Faker()

num1 = fake.random_int(min=1, max=100)
num2 = fake.random_int(min=1, max=100)
print(f"Fake test case: {num1} + {num2} = {num1 + num2}")
```

🔹 **Run Automated Tests with Fake Data**:
```bash
pytest tests/test_operations.py --num_records=100
```

---

## 📏 Code Quality Check
To enforce **coding standards**, run:
```bash
pylint calculator/
```

---

## 👨‍💻 Contributing

🚀 **Want to contribute?** Follow these steps:

1. **Fork the repository** 📌  
2. **Clone your fork**:  
   ```bash
   git clone https://github.com/your-username/Improved-Calculator.git
   ```
3. **Create a new branch**:  
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes & commit**:  
   ```bash
   git commit -m "Added new feature"
   ```
5. **Push to GitHub & Create Pull Request** 🚀  

---

## 📜 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

### **🔗 References**
1. ✅ [pytest Parameterized Tests](https://pytest-with-eric.com/introduction/pytest-generate-tests/)  
2. ✅ [Creating Fake Data in Python Using Faker](https://www.udacity.com/blog/2023/03/creating-fake-data-in-python-using-faker.html)  
3. ✅ [Faker Providers Documentation](https://faker.readthedocs.io/en/stable/providers.html)  
4. ✅ [Command-Line Interfaces in Python](https://realpython.com/command-line-interfaces-python-argparse/)  
5. ✅ [Python Try-Except Handling](https://www.geeksforgeeks.org/python-try-except/)  

---

## 🎯 Final Thoughts

This **Improved Calculator** is designed for **accurate calculations, testability, and robust error handling**. Whether you are a **developer**, **tester**, or **Python enthusiast**, this project serves as a **great example of OOP design, unit testing, and CLI applications**. 🚀
