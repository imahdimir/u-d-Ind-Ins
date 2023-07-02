"""

    """

from pathlib import Path

from mirutil.ns import rm_ns_module
from mirutil.ns import update_ns_module

update_ns_module()
import ns

# namespace
gdu = ns.GDU()
c = ns.Col()

# classes
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Const :
    # institutional & individual ownership url format
    url = 'http://old.tsetmc.com/tsev2/data/clienttype.aspx?i={}'

class FPN :
    # temp data files
    t1 = Path('temp-1.prq')
    t2 = Path('temp-2.prq')

class ColName :
    url = 'url'
    res_txt = 'res_text'

# classes instances
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fpn = FPN()
cn = ColName()
k = Const()

def main() :
    pass

    ##
    import _0_get_all_data
    import _1_data_cleaning
    import _2_upload_data_on_github

    ##
    _0_get_adj_prices.main()

    ##
    _1_data_cleaning.main()

    ##
    _2_upload_data_on_github.main()

    ##
    rm_ns_module()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
