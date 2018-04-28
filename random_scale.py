def random_scale():
    sizes =np.array ([352,384,416,448,480,512,544,576,608])
    pos = np.random.randint(0,9)
    slice_1 = sizes[pos]
    if pos==0:
       _list = sizes[0:7]
    elif pos==1:
       _list = sizes[1:8]
    else:
       _list = sizes[pos:]
    slice_2 = np.random.choice(_list,1)[0]
    meta = [slice_1,slice_2,3]
    print (meta)
    return meta