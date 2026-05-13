# import pandas as pd
#
# data = {'Yes': [130, 50, 25], 'No': [50, 56, 100], 'Yes_1': [115, 589, 541], 'No_1': [115, 589, 541],
#         'Yes_2': [115, 589, 541], 'No_2': [115, 589, 541]}
#
# df = pd.DataFrame(data, index=[1, 2, 3])
# print(df)


# import pandas as pd
#
# df = pd.read_excel('winemag-data-130k-v2.xlsx')
#
# italy_df = df.loc[df.country == 'Italy']
# print(italy_df)


# import pandas as pd
#
# df = pd.read_excel("winemag-data-130k-v2.xlsx")
#
# new_df = df.groupby('country')
# print(new_df.price.mean())

# import pandas as pd
#
# df = pd.read_excel('winemag-data-130k-v2.xlsx')
#
# df.sort_values(by='price', inplace=True, ascending=False)
#
# print(df.head().price)

import pandas as pd

df = read_excel('winemag-data-130k-v2.xlsx')

new_df = df.groupby('county')