# Estructura
Este repositorio está diseñado con el fin de proporcionar ejemplos prácticos y didácticos que permitan poner en práctica los principios de diseño SOLID.

A continuación, se presenta la estructura del módulo de principios SOLID.

Todos los ejemplos están desarrollados en Python, la estructura contiene:
- Archivo de ejemplo
- read.md con una expliación

solid/
├── 1_SRP_Single_Responsibility_Principle/
│   ├── example.py
│   └── SRP.md
├── 2_OCP_Open_Closed_Principle/
│   ├── example.py
│   └── OCP.md
├── 3_LSP_Liskov_Substitution_Principle/
│   ├── example.py
│   └── LSP.md
├── 4_ISP_Interface_Segregation_Principle/
│   ├── example.py
│   └── ISP.md
├── 5_DIP_Dependency_Inversion_Principle/
│   ├── example.py
│   └── DIP.md
└── SOLID.md

# - Principios SOLID

Los principios SOLID son un conjunto de reglas y prácticas para el diseño de clases orientadas a objetos (POO). Estos principios ayudan a comprender la implementación de patrones de diseño y la arquitectura de software.

A continuación se presentan sus acrónimos y descripciones:

SRP (Single Responsibility Principle)
El principio de responsabilidad única indica que una clase debe tener una única razón para cambiar, es decir, debe encargarse de una sola funcionalidad.

OCP (Open-Closed Principle)
Este principio establece que las clases deben estar abiertas a la extensión pero cerradas a la modificación. Así, el comportamiento de una clase puede extenderse sin alterar su código fuente.

LSP (Liskov Substitution Principle)
Indica que las subclases deben ser sustituibles por sus clases base sin alterar el correcto funcionamiento del programa.

ISP (Interface Segregation Principle)
Este principio sugiere mantener las interfaces específicas y separadas, evitando que las clases dependan de métodos que no utilizan.

DIP (Dependency Inversion Principle)
Plantea que las clases deben depender de abstracciones (interfaces o clases abstractas) y no de implementaciones concretas.

###### ENGLISH VERSION ######

# Structure
This repository is designed to provide practical and educational examples to put the SOLID design principles into practice.

Below is the structure of this SOLID principles module.

All examples are developed in Python and each folder contains:
- An example Python script
- A README.md explaining the principle

solid/
├── 1_SRP_Single_Responsibility_Principle/
│   ├── example.py
│   └── SRP.md
├── 2_OCP_Open_Closed_Principle/
│   ├── example.py
│   └── OCP.md
├── 3_LSP_Liskov_Substitution_Principle/
│   ├── example.py
│   └── LSPDME.md
├── 4_ISP_Interface_Segregation_Principle/
│   ├── example.py
│   └── ISP.md
├── 5_DIP_Dependency_Inversion_Principle/
│   ├── example.py
│   └── DIP.md
└── SOLID.md

# SOLID Principles
The SOLID principles are a set of rules and practices for designing object-oriented classes (OOP). These principles help in understanding the implementation of design patterns and software architecture.

Below are their acronyms and descriptions:

SRP (Single Responsibility Principle)
This principle states that a class should have only one reason to change, meaning it should be responsible for a single functionality.

OCP (Open-Closed Principle)
This principle establishes that classes should be open for extension but closed for modification. This allows extending the behavior of a class without altering its source code.

LSP (Liskov Substitution Principle)
This principle states that subclasses must be substitutable for their base classes without affecting the correctness of the program.

ISP (Interface Segregation Principle)
This principle suggests keeping interfaces specific and separated, avoiding that classes depend on methods they do not use.

DIP (Dependency Inversion Principle)
This principle states that classes should depend on abstractions (interfaces or abstract classes) rather than concrete implementations.

