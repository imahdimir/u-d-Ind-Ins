"""

    """

from pathlib import Path

import pandas as pd
from namespace_mahdimir import tse as ns
from persiantools.jdatetime import JalaliDateTime

from main import c
from main import cn
from main import fpn

# namespace %%%%%%%%%%%%%%%%%%%%
cd = ns.DInsIndCols()

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

def rename_cols(df) :
    cns = {
            '0'  : c.d ,

            '1'  : cd.bdc ,
            '2'  : cd.bsc ,
            '3'  : cd.sdc ,
            '4'  : cd.ssc ,

            '5'  : cd.bdv ,
            '6'  : cd.bsv ,
            '7'  : cd.sdv ,
            '8'  : cd.ssv ,

            '9'  : cd.bdva ,
            '10' : cd.bsva ,
            '11' : cd.sdva ,
            '12' : cd.ssva ,

            }

    return df.rename(columns = cns)

def remove_nan_rows(df) :
    cols = df.columns.difference([c.ftic , c.tse_id])
    return df.dropna(subset = cols)

def check_all_vals_are_notna(df) :
    msk = df.isna().any(axis = 1)
    df1 = df[msk]

    assert df1.empty , 'there are some nan values'

def check_date_vals_and_make_jdate(df) :
    df[c.d] = pd.to_datetime(df[c.d] , format = '%Y%m%d')

    df[c.jd] = df[c.d].apply(JalaliDateTime.to_jalali)

    df[c.jd] = df[c.jd].apply(lambda x : x.strftime('%Y-%m-%d'))
    df[c.d] = df[c.d].apply(lambda x : x.strftime('%Y-%m-%d'))

    return df

def add_today_date(df) :
    tod_date = JalaliDateTime.today().strftime('%Y-%m-%d')
    # tod_date = '1402-03-09'  # manually set
    df[c.get_date] = tod_date
    return df

def check_ftick_date_is_unique_mostly(df) :
    msk = df.duplicated(subset = [c.ftic , c.d] , keep = False)
    df1 = df[msk]

    assert len(df1) < 30

    return df[~ msk]

def reorder_cols(df) :
    col_ord = {
            c.get_date : None ,

            c.ftic     : None ,
            c.tse_id   : None ,

            c.d        : None ,
            c.jd       : None ,

            cd.bdc     : None ,
            cd.bsc     : None ,
            cd.sdc     : None ,
            cd.ssc     : None ,

            cd.bdv     : None ,
            cd.bsv     : None ,
            cd.sdv     : None ,
            cd.ssv     : None ,

            cd.bdva    : None ,
            cd.bsva    : None ,
            cd.sdva    : None ,
            cd.ssva    : None ,
            }

    return df[col_ord.keys()]

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
    df = rename_cols(df)

    ##
    df = remove_nan_rows(df)

    ##
    df = df.drop_duplicates()

    ##
    check_all_vals_are_notna(df)

    ##
    df = check_date_vals_and_make_jdate(df)

    ##
    df = add_today_date(df)

    ##
    df = check_ftick_date_is_unique_mostly(df)

    ##
    df = reorder_cols(df)

    ##
    df.to_parquet('temp_data/t3.prq' , index = False)

    ##

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
