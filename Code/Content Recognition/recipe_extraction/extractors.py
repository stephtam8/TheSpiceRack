from enum import Enum as _Enum
from enum import unique as _unique
from typing import Iterable as _Iterable
import os as _os
import multiprocessing as _multiprocessing
import pprint as _pprint

from dragnet.extractor import Extractor as _Extractor
import dragnet.model_training as _model_training
import dragnet.data_processing as _data_processing
from sklearn.neighbors import KNeighborsClassifier as _KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier as _ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier as _BaggingClassifier
from sklearn.svm import SVC as _SVC
from sklearn.neural_network import MLPClassifier as _MLPClassifier
from sklearn.externals import joblib as _joblib


DEFAULT_DRAGNET_FEATURES = ('kohlschuetter', 'weninger', 'readability')
DEFAULT_DATA_DIRECTORY = _os.path.join(
    _os.path.dirname(_os.path.dirname(__file__)),
    'extraction_data'
)


@_unique
class RecipeExtractionModel(_Enum):
    KNeighbors = _KNeighborsClassifier(
        n_neighbors=10,
        weights='distance',
        n_jobs=-1
    )
    ExtraTrees = _ExtraTreesClassifier(
        n_estimators=10,
        max_features=None,
        min_samples_leaf=75,
        n_jobs=-1
    )
    Bagging = _BaggingClassifier(
        n_estimators=10,
        n_jobs=-1
    )
    SVC = _SVC(
        C=1,
        probability=True,
        gamma='auto'
    )
    MLP = _MLPClassifier(
        max_iter=1000
    )

    def __str__(self):
        return _pprint.pformat(self.value)


def train(model: RecipeExtractionModel = RecipeExtractionModel.SVC,
          features: _Iterable[str] = DEFAULT_DRAGNET_FEATURES,
          data_location: str = DEFAULT_DATA_DIRECTORY) -> _Extractor:
    """Train a content extraction model using dragnet and sklearn

    Parameters
    ----------
    model : RecipeExtractionModel
        The initialized model (an sklearn classifier) to train
    features : str iterable
        The `dragnet` features to use in this model
    data_location : str
        The system filepath of the training data

    Returns
    -------
    dragnet.Extractor
        The trained content extraction model
    """

    _data_processing.extract_all_gold_standard_data(
        data_location,
        nprocesses=_multiprocessing.cpu_count() - 1,
        overwrite=False
    )

    print('Beginning training...')
    print(model)
    base_extractor = _Extractor(
        features=features,
        to_extract='content',
        model=model.value
    )
    extractor = _model_training.train_model(
        base_extractor,
        data_location,
    )
    return extractor


def save(extractor: _Extractor,
         output_path: str = None):
    """
    Save a pickled version of an Extractor

    Parameters
    ----------
    extractor : dragnet.Extractor
        The trained content extraction model
    output_path : str
        (Optional) The output location of the saved model. If omitted, a
        timestamped file will be placed in '/training_output/` adjacent to the
        default data directory.
    """

    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    if output_path is None:
        from datetime import datetime as _date
        output_path = _os.path.join(
            _os.path.dirname(DEFAULT_DATA_DIRECTORY),
            'training_output',
            _date.now().strftime("%Y%m%d%H%M%S") + '_' + 'model.gz'
        )

    _joblib.dump(extractor, output_path, compress=3)


def load(pickled_model_path: str) -> _Extractor:
    """
    Load a pickled version of an Extractor

    Parameters
    ----------
    pickled_model_path : str
        The location of the saved model

    Returns
    -------
    dragnet.Extractor
        The trained content extraction model
    """

    return _joblib.load(pickled_model_path)
