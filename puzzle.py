from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# GLOBAL KNOWLEDGE
global_knowledge = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Info about the structure of the problem
    global_knowledge,

    # What they imply
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
a_says = And(AKnave, BKnave)
# B says nothing.

knowledge1 = And(
    # Info about the structure of the problem
    global_knowledge,

    # What they imply
    Implication(AKnight, a_says),
    Implication(AKnave, Not(a_says)),
)

# Puzzle 2
# A says "We are the same kind."
a_says = Or(And(AKnight, BKnight), And(AKnave, BKnave))
# B says "We are of different kinds."
b_says = Or(And(BKnight, Not(AKnight)), And(BKnave, Not(AKnave)))

knowledge2 = And(
    # Info about the structure of the problem
    global_knowledge,

    # What they imply
    Implication(AKnight, a_says),
    Implication(AKnave, Not(a_says)),
    Implication(BKnight, b_says),
    Implication(BKnave, Not(b_says)),

)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
a_says = Or(AKnight, AKnave)
# B says "A said 'I am a knave'."
# B says "C is a knave."
b_says = And(AKnave, CKnave)
# C says "A is a knight."
c_says = AKnight

knowledge3 = And(
    # Info about the structure of the problem
    global_knowledge,

    # What they imply
    Implication(AKnight, a_says),
    Implication(AKnave, Not(a_says)),
    Implication(BKnight, b_says),
    Implication(BKnave, Not(b_says)),
    Implication(CKnight, c_says),
    Implication(CKnave, Not(c_says)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
