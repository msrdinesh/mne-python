# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#
# License: BSD (3-clause)

import os.path as op
from ...utils import verbose
from ...fixes import partial
from ..utils import (has_dataset, _data_path, _get_version, _version_doc,
                     _data_path_doc)

has_brainstorm_data = partial(has_dataset, name='brainstorm')


@verbose
def data_path(path=None, force_update=False, update_path=True, download=True,
              verbose=None):
    archive_name = dict(brainstorm='bst_raw.tar.bz2')
    data_path = _data_path(path=path, force_update=force_update,
                           update_path=update_path, name='brainstorm',
                           download=download, archive_name=archive_name)
    if data_path != '':
        return op.join(data_path, 'bst_raw')
    else:
        return data_path


_data_path_doc = _data_path_doc.format(name='brainstorm',
                                       conf='MNE_DATASETS_BRAINSTORM_DATA'
                                            '_PATH')
_data_path_doc = _data_path_doc.replace('brainstorm dataset',
                                        'brainstorm (bst_raw) dataset')
data_path.__doc__ = _data_path_doc


def get_version():
    return _get_version('brainstorm')

get_version.__doc__ = _version_doc.format(name='brainstorm')
