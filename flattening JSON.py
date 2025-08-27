def flatten_data(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

sample_dict = {'a':{'101':25,'202':123},'b':[{'zh':1,'gh':12},{'uu':34,'yy':34}]}
j = flatten_data(sample_dict)
print(j)