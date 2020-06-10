import numpy as np

# Python function to get dictionary keys as list  
def getList(dict): 
    return [*dict]

def remove_duplicates(x, y):
    seen = {}
    for i in range(len(x)):
        if x[i] not in seen:
            seen[x[i]] = float(y[i])
        else:
            seen[x[i]] += float(y[i])

    return getList(seen), list(seen.values())


def remove_zero_intensity(x, y):
    x_ = []
    y_ = []
    for i in range(len(y)):
        if y[i] > 10e-15:
            y_.append(y[i])
            x_.append(x[i])
    return np.array(x_), np.array(y_)

if __name__ == "__main__":
    import pandas as pd
    fname = 'xas.k6w.6311++g3df3pd.dat'

    data = pd.read_csv(fname, header=None, delim_whitespace = True)
    data.columns = ["x", "fx"]
    x, fx = remove_duplicates(data.x, data.fx)
    print(x)
    print(fx)
    x, fx = remove_zero_intensity(x, fx)
    print(fx)