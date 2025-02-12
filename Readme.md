# Improved-Calculator

An enhanced calculator application designed with Object-Oriented Programming (OOP) principles, including **SOLID principles, Factory Method, and OOP operators**. This calculator performs arithmetic operations and maintains a **history of calculations** for easy reference.

## 🚀 Features

- ✅ **Basic Operations**: Addition, Subtraction, Multiplication, Division
- ✅ **Calculation History**: Stores past calculations
- ✅ **OOP Design**: Implements SOLID principles and Factory Method
- ✅ **Exception Handling**: Prevents division by zero errors
- ✅ **Modular Codebase**: Clean, maintainable, and scalable

---

## 🛠 Technologies & Libraries Used

- **Python** 🐍 (Core programming language)
- **pytest** 📌 (Unit testing framework)
- **pylint** ✅ (Static code analysis)
- **decimal** 🔢 (Precision handling for mathematical operations)

---

## 🎯 Object-Oriented Programming (OOP) Concepts Used

### 1️⃣ **SOLID Principles**
- **S**: **Single Responsibility Principle (SRP)** - Each class has a well-defined responsibility (e.g., `Calculation`, `Calculator`, `Operations`).
- **O**: **Open/Closed Principle (OCP)** - The calculator can be extended with new operations without modifying the existing code.
- **L**: **Liskov Substitution Principle (LSP)** - Derived classes can replace base classes without affecting functionality.
- **I**: **Interface Segregation Principle (ISP)** - Classes are kept focused, ensuring modularity.
- **D**: **Dependency Inversion Principle (DIP)** - The high-level `Calculator` class depends on abstractions (`Operations`), not concrete implementations.

### 2️⃣ **Factory Method Pattern**
- Used to **create instances of `Calculation` dynamically**, ensuring flexibility in operation execution.

### 3️⃣ **OOP Operators**
- **Encapsulation**: Data is wrapped within classes, restricting direct access.
- **Abstraction**: Users interact with high-level interfaces (`Calculator`) while internal operations are abstracted.
- **Inheritance**: `Calculation` class extends functionality while maintaining reusability.
- **Polymorphism**: Different arithmetic operations (`add`, `subtract`, etc.) are handled uniformly.

---

## 📦 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AkashDeore15/Improved-Calculator.git
cd Improved-Calculator
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Calculator
```sh
python main.py
```

## 🖥️ Usage
1.Run the program.
2.Enter numbers and select an operation.
3.View results.
4.Check calculation history for previous results.

##🧪 Running Tests
To verify functionality, run:
```sh
pytest --pylint --cov
```

## 🤝 Contributing
Contributions are welcome! To contribute:
1.Fork the repository.
2.Create a new branch (feature-branch).
3.Commit changes (git commit -m "Added new feature").
4.Push to your branch (git push origin feature-branch).
5.Open a Pull Request.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📩 Contact
For any queries, reach out to Akash Deore via GitHub.
