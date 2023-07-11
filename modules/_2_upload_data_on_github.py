"""

    """

from pathlib import Path

import pandas as pd
from githubdata import GitHubDataRepo
from mirutil.df import save_df_as_prq
from persiantools.jdatetime import JalaliDateTime

from main import c
from main import cd
from main import fpn
from main import gdu

def clone_target_repo() :
    gdt = GitHubDataRepo(gdu.trg)
    gdt.clone_overwrite()
    return gdt

def add_today_date(df) :
    tod_date = JalaliDateTime.today().strftime('%Y-%m-%d')
    # tod_date = '1402-03-09'  # manually set
    df[c.get_date] = tod_date
    return df

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

def check_complete_backward_compatibility(gdt) :
    dfo = gdt.read_data()

    dfo = dfo.drop(columns = [c.get_date])

    df = pd.read_parquet(fpn.t3)

    dfo1 = dfo.merge(df , how = 'left' , indicator = True)

    assert dfo1['_merge'].eq('both').all() , 'Not backward compatible!'

    return df

def main() :
    pass

    ##
    gdt = clone_target_repo()

    ##
    df = check_complete_backward_compatibility(gdt)

    ##
    df = add_today_date(df)

    ##
    df = reorder_cols(df)

    ##
    gdt.data_fp.unlink()

    ##
    tjd = JalaliDateTime.now().strftime('%Y-%m-%d')
    fp = gdt.local_path / f'{tjd}.prq'

    ##
    save_df_as_prq(df , fp)

    ##
    msg = 'Updated on ' + tjd
    msg += ' by ' + gdu.slf

    ##
    gdt.commit_and_push(msg , branch = 'main')

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
if False :
    pass

    ##

    ##
