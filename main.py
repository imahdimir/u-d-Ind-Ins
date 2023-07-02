"""

    """

from pathlib import Path

from namespace_mahdimir import github_data_url as mgdu
from namespace_mahdimir import tse as ns

# namespace
c = ns.Col()

# class %%%%%%%%%%%%%%%%%%%%
class GDU :
    g = mgdu.GitHubDataUrl()

    slf = g.u_d_ins_ind
    src_ids = g.d_tsetmc_id_2_ticker

class FPN :
    # temp data files
    t1 = Path('temp_data/t1.prq')
    t2 = Path('temp_data/t2.prq')

class Const :
    # institutional & individual ownership url format
    url = 'http://old.tsetmc.com/tsev2/data/clienttype.aspx?i={}'

class ColName :
    url = 'url'
    res_txt = 'res_text'

# class instances   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
gdu = GDU()
fpn = FPN()
cn = ColName()
k = Const()

def main() :
    pass

    ##
    from modules import _1_data_cleaning
    from modules import _2_upload_data_on_github

    ##
    _0_get_adj_prices.main()

    ##
    _1_data_cleaning.main()

    ##
    _2_upload_data_on_github.main()

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
