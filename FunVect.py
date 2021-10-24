def superposition(funmod, funseq):
    funres = []
    for i in funseq:
        def res(x, j = i):
            return lambda par: x(j(par))
        funres.append(res(funmod))
    return funres
