

import pandas as pd

header_list = ['Column A', 'Column B', 'Column C']
row_list = [['A1', 'B1', 'C1'],
            ['A2', 'B2', 'C2'],
            ['A3', 'B3', 'C3']]

df = pd.DataFrame(row_list, columns=header_list)

print(df)