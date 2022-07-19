from SupplyWriteOff import eat
import pandas as pd

m = ["APR 2022",
"MAY 2022",
"JUN 2022",
"JUL 2022",
"AUG 2022",
"SEP 2022",
"OCT 2022",]

v = [570.0,
645.0,
702.0,
826.0,
815.0,
848.0,
850.0,]

s = pd.Series(data=v, index=m)

print(eat(s,4327))