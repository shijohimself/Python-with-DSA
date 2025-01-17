# keyword arguments

def marks(sci , eng , hin , sst , comp ):
    print(sci,eng,hin, sst , comp)
    total = sci + sst + hin + eng + comp
    print(total)

marks(sci = 92 , eng = 77 , hin = 56 , sst = 98 ,comp = 100)
marks(56,23,comp = 100, sst = 77, hin = 33)
# order should be maintained