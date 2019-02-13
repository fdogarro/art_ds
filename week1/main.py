//Pandas Code

def answer_one():
    return df.loc[df['Gold'].idxmax()].name
answer_one()


def answer_two():
    gold_diff = df['Gold'] - df['Gold.1']
    return gold_diff.idxmax()
answer_two()


def answer_three():
    df1 = df[(df['Gold']>1) & (df['Gold.1']>1)]
    df1 = df['Gold'] - df['Gold.1'] / df['Gold.2']
    return df1.idxmax()
answer_three()


def answer_four():
    df[(df['Gold.2'] * 3)]
#     df['Silver.2'] * 2
#     df['Bronze.2'] * 1
    return df['Gold.2'] * 3
answer_four()


def answer_five():
    census_df[(census_df['SUMLEV']== 50)]
    return census_df.loc[census_df['Gold'].idxmax()].name
answer_five()
