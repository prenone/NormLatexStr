# NormLatexStr

This package provides a function to format numbers with their uncertainties in LaTeX format using the SIunitx package syntax.

This package automatically chooses the right number of significant figures for the uncertainties (2 figures if unc < 2., 1 figure otherwise) and chooses the right number of figures for the value so that it has the same number of figures as the uncertainties. See *Example usage* to get an idea.

## Installation

pip install -e "git+https://github.com/prenone/NormLatexStr"

## Example usage

```
print(norm_latex_str(12.34, 0.12, r'\volt'))
print(norm_latex_str(5.67, 0.05, r'\meter'))
print(norm_latex_str(0.891, 0.009, r'\second'))
print(norm_latex_str(3.45, 0.03, r'\ampere'))
print(norm_latex_str(78.9, 0.8, r'\watt'))
print(norm_latex_str(0.0045, 0.0001, r'\tesla'))
print(norm_latex_str(150.0, 2.0, r'\newton'))
print(norm_latex_str(0.002, 0.0003, r'\coulomb'))
print(norm_latex_str(65.3, 1.2, r'\joule'))
print(norm_latex_str(9.81, 0.1, r'\meter \per \second^2'))
print(norm_latex_str(1.602, 0.001, r'\electronvolt'))

# \qty{12.34 \pm 0.12}{\volt}
# \qty{5.67 \pm 0.05}{\meter}
# \qty{0.891 \pm 0.009}{\second}
# \qty{3.45 \pm 0.03}{\ampere}
# \qty{78.8 \pm 0.8}{\watt}
# \qty{0.00450 \pm 0.00010}{\tesla}
# \qty{150 \pm 2}{\newton}
# \qty{0.0020 \pm 0.0003}{\coulomb}
# \qty{65.3 \pm 1.2}{\joule}
# \qty{9.81 \pm 0.10}{\meter \per \second^2}
# \qty{1.6020 \pm 0.0010}{\electronvolt}
```


