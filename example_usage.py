from client import HindleyMilnerInferencer

def main():
    print("=== Hindley-Milner Algorithm W Type Inferencer ===")
    inferencer = HindleyMilnerInferencer()
    res = inferencer.unify_types("'a", "Int")
    print("Unification Result:", res)
    assert res["unifiable"] is True
    assert res["substitutions"]["'a"] == "Int"

    print("Hindley-Milner Inferencer verified successfully!")

if __name__ == "__main__":
    main()
