def evaluate(r): return {"passed":r.get("physical_control") is False and len(r.get("results",[]))==6}
