# 🎸 Exploring Argentina’s Music Scene

This is a GUI-based Python application that explores a real dataset of registered music bands across neighborhoods in Argentina. It was developed as a final project for a university-level Python programming course, combining OOP principles, data manipulation, and interactive interface design using PyQt5.

## 🧩 Project Overview

The application loads a dataset containing information about local bands (genre, style, social media presence, neighborhood, etc.) and offers a series of 14 functionalities to interact with this data, including:

- Calculating band counts by neighborhood
- Visualizing genre prevalence and personality traits
- Viewing most socially connected bands
- Displaying genre/style diversity
- Filtering by registration dates and producing .txt reports

The tool also includes graphical components such as horizontal bar charts and calendar-based selectors. The objective was not only technical but also exploratory: to investigate cultural dynamics in Argentina’s musical landscape through structured data.

## ⚙️ Technologies Used

- Python 3
- PyQt5
- matplotlib
- CSV handling
- OOP principles
- GUI event handling
- Custom styling via `.qss`

## 📁 Files Included

| File                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `banda.py`                | Defines the `Banda` class and logic for parsing and organizing the dataset. |
| `gui.py`                  | Main interface and functionality navigation with PyQt5.                     |
| `opciones.py`             | Implements the 14 analytical options offered in the GUI.                    |
| `bandas-inscriptas.csv`   | Input dataset with band data (genre, date, location, social media, etc).    |
| `estilo.qss`              | Custom stylesheet to improve UI aesthetics.                                 |

## 🧠 What I Learned

This project strengthened my understanding of how to combine object-oriented thinking with GUI development and real-world data. It helped me appreciate how interfaces and logic can be modularized effectively, and taught me how to manage user inputs and outputs in a clean, intuitive way.
