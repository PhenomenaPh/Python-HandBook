1.

df3 = pd.merge(df1, df2, type = inner, on = ['date', 'acc'])

df3['Маржа'] = df3['revenue'] / df3['balance']

df4 = df3.group_by(['date', 'type', 'cur'])['balance', 'revenue'].sum()
df4['Маржа'] = df4['revenue'] / df4['balance']