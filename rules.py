# rules.py

from expert import Rule
from condition import Condition, OR

# Zdefiniowanie reguł


# Zdefiniowanie reguł
rules = [
    Rule(
        name="Reguła 1",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            Condition("kaszel", "==", 0.5),
        ],
        conclusions={"inhibitory_ace": 0.7},
    ),
    Rule(
        name="Reguła 2",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.6),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            Condition("kaszel", ">", 0.5),
        ],
        conclusions={"inhibitory_ace": 0.1},
    ),
    Rule(
        name="Reguła 3",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            OR(Condition("kaszel", "<=", 0.4), Condition("kaszel", ">=", 0.6)),
        ],
        conclusions={"wariant2": 0.7},
    ),
    Rule(
        name="Reguła 3a",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
            OR(Condition("kaszel", "<=", 0.4), Condition("kaszel", ">=", 0.6)),
        ],
        conclusions={"wariant2": 0.5},
    ),
    Rule(
        name="Reguła 4",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
        ],
        conclusions={"lekarstwo_A": 0.7},
    ),
    Rule(
        name="Reguła 5",
        conditions=[
            Condition("skurcz_oskrzeli", ">", 0.5),
            Condition("dusznosc", ">", 0.5),
            Condition("wheezing", ">", 0.5),
        ],
        conclusions={"lekarstwo_A": 0.8},
    ),
]