# Calculus Visualization Project

## Overview
This project is an ongoing project. The goal is to allow students and anyone interested in mathematics at a college level a tool to visualize, practice, test their understanding of various concepts. For now this project only includes the limits of a function. Other concepts to follow soon 🔥🔥

## Features
- **Graphing Functions**: Visual representation of functions.

- **Animated Limit Approaches**: Shows points moving toward a target value from the left and right.

- **Left & Right Limit Calculation**: Verifies limit values from both directions.

- **Limit Equality Check**: Confirms whether the left and right limits are the same and uses this as a guess for the epsilon-delta verification.

- **Epsilon-Delta Verification**: Uses the formal definition of a limit to verify guesses.

- **Future Enhancements**: Planned additions include handling more edge cases and adding differentiation functionality.
## Installation & Setup

### Prerequisites

- Python 3.x
- Required libraries: `matplotlib`, `numpy`

<!-- ### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/calculus-visualization.git
   cd calculus-visualization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the project:
   ```bash
   python main.py
   ``` -->

## How to Use

1. Run the script to open an interactive graph.
2. Choose a function and a point to analyze its limit.
3. Observe animations for approaching values.
4. Use the epsilon-delta check to confirm the limit formally.

## Examples

Example: Approximating the limit of `f(x) = 1/x` as `x` approaches `0`.

```python
limit_calculator(lambda x: 1/x, 0)
```

Output:
```
Left Limit: -∞
Right Limit: ∞
Conclusion: Limit does not exist.
```

## Future Plans
- **Differentiation**: Visualizing tangent lines, derivative functions.
- **More Edge Cases**: Discontinuous and oscillatory functions.
- **Interactive UI**: Web-based version for broader accessibility.

## Contributing
Contributions are welcome! If you have ideas or find issues, feel free to submit a pull request or open an issue.


## Contact
For any questions or feedback, reach out via PearlPearl-Pearl on GitHub.

