import pandas as pd
import wlr

df = pd.ExcelFile('CC_ratios_all.xlsx')
sheet_names = df.sheet_names

sheet_dict = dict(zip(range(1,8),sheet_names))

sheet_to_process = sheet_dict[7]
df = pd.read_excel('CC_ratios_all.xlsx', sheet_name=sheet_to_process, index_col='Sample lables')

df = df.loc['CC1':'CC13']

x = list(df['Specified Amount'])
y = list(df['12CC'])
dict_values = dict(zip(x,y))

poped_list = [
0.010,
0.025,
0.050,
0.100,
0.250,
0.500,
1.000,
2.500,
5.000,
10.000,
20.000,
30.000,
50.000
]

for item in poped_list:
	dict_values.pop(item)
    
wlr.WeightedLinReg.__1X2__(list(dict_values.keys()),list(dict_values.values()))
print(poped_list)

