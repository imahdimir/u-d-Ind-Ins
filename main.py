"""

    """

from pathlib import Path

from mirutil.ns import rm_ns_module
from mirutil.ns import update_ns_module

update_ns_module()
import ns

# namespace
c = ns.Col()

# classes
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class GDU :
    slf = "https://github.com/imahdimir/u-d-Ins-Ind"
    src_ids = "https://github.com/imahdimir/d-TSETMC_ID-2-Ticker"

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

# classes instances
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
    rm_ns_module()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
from nested_namespace import NestedNamespace

x = NestedNamespace()

x.some_attr = {
        'a'    : {
                'b' : 'c'
                } ,
        'will' : 'be transformed'
        }

x

##
fp = '/Users/mahdi/Dropbox/GitHub/u-d-Ins-Ind/DAllCodalLetters.json'

import json

with open(fp , 'r') as f :
    y = json.load(f)

##
type(y)

##
x = NestedNamespace()

x = x.transform(y)
x
##
x.DAllCodalLetters = NestedNamespace().transform(y)

##
x.DAllCodalLetters.as_dict()

##
x1 = x.DAllCodalLetters

x1

##
(x1.TracingNo)
x1.TracingNo1
x1.TracingNon

##
x.DAllCodalLetters.s1 = 'some string'

##
x.s1 = NestedNamespace()

##
x.s1.s2 = 'some other string'

##

##
