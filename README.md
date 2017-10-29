# guiNumKnife ![Travis](https://img.shields.io/travis/fspoettel/blaupause.svg?maxAge=2592000?style=flat-square)

[![Greenkeeper badge](https://badges.greenkeeper.io/fspoettel/blaupause.svg)](https://greenkeeper.io/)

> Copyright (C) <2017>  <Rohit Goswami>

guiNumKnife is an attempt to ease the burden of undergraduate B.Tech coursework, and maybe even foster interest.

## TO-DO

- Check Secant
- Add Max Iterations for secant
- Hide and enable UI elements per method
- Use Naive Gauss Elimination Again 

## Methods Covered
The methods (modules) are:
1. Root Finding
    i. Bisection
    ii. Newton Raphson
    iii. Regula Falsi
    iv. Secant
2. Simultaneous Linear Equations
    i. Gauss Seidel
    ii. Gauss Jordan
    iii. Gauss Elimination (Naive + Pivoting)
3. ODE
    i. Milne's Method
    ii. Runge-Kutta Methods
        * RK - I (Euler)
        * RK - II
        * RK - III
        * RK - IV

## Acknowledgments
This software is built on the following (incomplete):

- PyQt 5
- Python 3
- Qt Designer
- PyInstaller
- SymPy

Additionally the following books and resources have been used (also mentioned in-code):

- Summerfield, M. (2007). Rapid GUI programming with Python and Qt: the definitive guide to PyQt programming. Pearson Education.
- Kiusalaas, J. (2013). Numerical methods in engineering with Python 3. Cambridge university press.
- [Tales of the DevOps](https://devopslog.wordpress.com/2012/12/23/newton-raphson-method-using-python-sympy/) 

## Contributions
Pull requests welcome!
Please add yourself to the Contributors file as well, with a summary and contact details (optinal).

## License
The code itself is under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) however it is built with PyQt, so as per [this](https://opensource.stackexchange.com/questions/5383/under-what-licenses-can-i-release-open-source-software-that-uses-pyqt) StackExchange thread, the PyQT portion is under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).