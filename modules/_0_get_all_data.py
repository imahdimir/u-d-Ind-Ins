"""

    """

import time
from pathlib import Path

import pandas as pd
import requests
from githubdata import get_data_from_github
from mirutil.const import Const as MConst

from main import c
from main import cn
from main import fpn
from main import gdu
from main import k

mk = MConst()

def get_all_firm_ids() :
    """ get all TSETMC ids """
    df = get_data_from_github(gdu.src_ids)
    df = df.astype('string')
    return df

def make_adjusted_price_url(firmticker_id) :
    return k.url.format(firmticker_id)

def filter_to_get_items(df) :
    msk = df[cn.res_txt].isna()
    msk |= df[cn.res_txt].eq('')

    df = df[msk]
    print('empty ones count:' , len(df))

    return df

def main() :
    pass

    ##
    # get all firm ids
    df = get_all_firm_ids()

    ##
    # make a col for url
    df[cn.url] = df[c.tse_id].apply(make_adjusted_price_url)

    ##
    # make a col for response text
    df[cn.res_txt] = None

    ##
    # get all data
    for i in range(1 , 11) :
        print('loop:' , i)

        df1 = filter_to_get_items(df)
        if df1.empty :
            break

        for indx , ro in df1.iterrows() :
            print(indx , ' : ' , ro[c.tic])

            if not (pd.isna(ro[cn.res_txt]) or ro[cn.res_txt] == '') :
                continue

            r = requests.get(ro[cn.url] , headers = mk.headers)

            if r.status_code == 200 :
                df.loc[indx , cn.res_txt] = r.text
                print(r.text[:50])
            else :
                print(r.status_code)

            time.sleep(1)

            # break

        # break

    ##
    # save temp data
    df.to_parquet(fpn.t1 , index = False)

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    gd = GitHubDataRepo(gdu.src_ids)
    gd.clone_overwrite()

    ##
    df = gd.read_data()

    ##
    df = get_data_from_github(gdu.src_ids)

    ##
    x = '10331088713418617'
    x = 'http://old.tsetmc.com/tsev2/data/clienttype.aspx?i=28797257472175528'

    ##
    x = 'http://cdn.tsetmc.com/api/ClientType/GetClientType/28797257472175528/1/0'

    ##
    r = requests.get(x , headers = mk.headers)
    r.text

    ##

    ##

    ##
