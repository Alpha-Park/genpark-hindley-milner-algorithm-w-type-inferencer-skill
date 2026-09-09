class HindleyMilnerInferencer:
    """Monomorphic/Polymorphic unification and type reconstruction."""
    def unify_types(self, t1: str, t2: str) -> dict:
        subst = {}
        if t1 == t2:
            return {"unifiable": True, "substitutions": subst}
        if t1.startswith("'"):
            subst[t1] = t2
            return {"unifiable": True, "substitutions": subst}
        if t2.startswith("'"):
            subst[t2] = t1
            return {"unifiable": True, "substitutions": subst}
        return {"unifiable": False, "substitutions": {}}
