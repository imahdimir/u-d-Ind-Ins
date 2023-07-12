"""

    """

import shutil
from pathlib import Path

from githubdata import default_containing_dir
from mirutil.run_modules import run_modules_from_dir_in_order
from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu

# namespace     %%%%%%%%%%%%%%%
c = tse_ns.Col()
cd = tse_ns.DIndInsCols()

# class         %%%%%%%%%%%%%%%
class GDU :
    g = tgdu.GitHubDataUrl()

    slf = tgdu.m + 'u-d-Ind-Ins'

    src_ids = g.id_2_tic
    trg = g.ind_ins

class Dirs :
    md = Path('modules/')
    md.mkdir(exist_ok = True)

    gd = default_containing_dir

    td = Path('temp_data/')
    td.mkdir(exist_ok = True)

class FPN :
    dyr = Dirs()
    td = dyr.td

    # temp data files
    t0 = td / 't0.prq'
    t1_0 = td / 't1_0.prq'
    t1_1 = td / 't1_1.prq'

class Const :
    # institutional & individual ownership url format
    url = 'http://old.tsetmc.com/tsev2/data/clienttype.aspx?i={}'

class ColName :
    url = 'url'
    res_txt = 'res_text'

# class instances   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
gdu = GDU()
dyr = Dirs()
fpn = FPN()
cn = ColName()
k = Const()

def clean_cache() :
    print('cleaning cache ...')

    dyrs = {
            dyr.gd : None ,
            dyr.td : None ,
            }

    for di in dyrs.keys() :
        shutil.rmtree(di , ignore_errors = True)

def main() :
    pass

    ##
    run_modules_from_dir_in_order(dyr.md)

    ##
    clean_cache()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


if False :
    pass

    ##
    def test() :
        pass

        ##

        ##

        ##

##
