"""

    """

from pathlib import Path

import pandas as pd
from persiantools.jdatetime import JalaliDateTime

from main import c
from main import cn
from main import fpn
from main import gdu
from main import k

def split_into_df_cols(res_text) :
    df = pd.DataFrame(res_text.split(';'))
    return df[0].str.split(',' , expand = True)

def split_all_rows(dft) :
    df = pd.DataFrame()

    for indx , row in dft.iterrows() :
        print(indx , ' : ' , row[c.ftic])

        df1 = split_into_df_cols(row[cn.res_txt])

        df1[c.ftic] = row[c.ftic]
        df1[c.tse_id] = row[c.tse_id]

        df = pd.concat([df , df1])

        # break

    return df

def main() :
    pass

    ##
    dft = pd.read_parquet(fpn.t1)

    ##
    df = split_all_rows(dft)

    ##
    df.to_parquet(fpn.t2 , index = False)

    ##
    df = pd.read_parquet(fpn.t2)

    ##
    cns = {
            0 : c.d ,
            1 : c.ahi ,
            2 : c.alow ,
            3 : c.aopen ,
            4 : c.aclose ,
            5 : c.vol ,
            6 : c.alast ,
            }

    dfp = dfp.rename(columns = cns)

    ##
    pat = r'\d{4}\d{2}\d{2}'
    msk = ~ dfp[c.d].str.fullmatch(pat)

    df1 = dfp[msk]

    ##
    dfp = dfp[~ msk]

    ##
    msk = dfp.isna().any(axis = 1)
    df1 = dfp[msk]

    assert df1.empty

    ##
    dfp[c.d] = pd.to_datetime(dfp[c.d] , format = '%Y%m%d')

    ##
    dfp[c.jd] = dfp[c.d].apply(JalaliDateTime.to_jalali)

    ##
    dfp[c.jd] = dfp[c.jd].apply(lambda x : x.strftime('%Y-%m-%d'))

    ##
    dfp[c.d] = dfp[c.d].apply(lambda x : x.strftime('%Y-%m-%d'))

    ##
    tod_date = JalaliDateTime.today().strftime('%Y-%m-%d')
    dfp[cn.get_date] = tod_date

    ##
    msk = dfp.duplicated(subset = [c.ftic , c.d] , keep = False)
    df1 = dfp[msk]

    assert df1.empty

    ##
    col_ord = {
            cn.get_date : None ,
            c.tse_id    : None ,
            c.ftic      : None ,
            c.d         : None ,
            c.jd        : None ,
            c.aopen     : None ,
            c.ahi       : None ,
            c.alow      : None ,
            c.alast     : None ,
            c.vol       : None ,
            c.aclose    : None ,
            }

    dfp = dfp[col_ord.keys()]

    ##
    dfp.to_parquet(fps , index = False)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##

if False :
    pass

    ##
    # 1 row case
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    df = pd.read_parquet(fpn.t1)

    ##
    r0 = df.loc[0 , cn.res_txt]

    df1 = pd.DataFrame(r0.split(';'))

    ##
    df2 = df1[0].str.split(',' , expand = True)

    ##
