# CS50AI | Lecture 1 - Knowledge | Project 1 - `Knights`

This project is a mandatory assignment from **[CS50AI – Lecture 1: "Knowledge"](https://cs50.harvard.edu/ai/2024/projects/1/knights/)**.

### 📌 Usage

To run the project locally, follow these steps:

1. **Clone the repository** to your local machine.

2. **Navigate to the project directory**:

   ```sh
   cd path/to/knowledge
   ```

3. Run `python puzzle.py`

<br>

### Overview

This project is an implementation of the _"Knights and Knaves"_ logic puzzles as described in Raymond Smullyan's book _"What is the Name of This Book?"_. In these puzzles, characters are either knights, who always tell the truth, or knaves, who always lie. The objective is to determine the identity of each character based on their statements.

Using propositional logic and logical connectives, this project models and solves four puzzles. It demonstrates how logical reasoning can be represented programmatically to allow an AI system to solve problems using model checking. The solution uses the `logic.py` framework provided as part of the project distribution to define logical sentences and perform model checks.


### My Role in the Project

I implemented the "global knowledge" and the logical knowledge bases for four puzzles by translating the rules and statements into propositional logic. This involved:

1. Understanding the puzzle structure and constraints.

2. Encoding the rules for knights and knaves.

3. Translating each character's statements into logical expressions.

4. Using implications to capture the truth-telling or lying behavior of knights and knaves.