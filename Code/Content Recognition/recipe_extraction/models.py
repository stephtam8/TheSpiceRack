from enum import Enum as _Enum
from enum import unique as _unique
from typing import Iterable as _Iterable
import os as _os
import multiprocessing as _multiprocessing

from dragnet.extractor import Extractor as _Extractor
import dragnet.model_training as _model_training
import dragnet.data_processing as _data_processing
from sklearn.neighbors import KNeighborsClassifier as _KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier as _ExtraTreesClassifier
from sklearn.svm import SVC as _SVC
from sklearn.neural_network import MLPClassifier as _MLPClassifier


_DEFAULT_DRAGNET_FEATURES = ('kohlschuetter', 'weninger', 'readability')
_DEFAULT_DATA_DIRECTORY = _os.path.join(
    _os.path.dirname(_os.path.dirname(__file__)),
    'content_data/'
)


@_unique
class RecipeExtractionModel(_Enum):
    KNeighbors = _KNeighborsClassifier(
        n_neighbors=10,
        weights='distance'
    )
    ExtraTrees = _ExtraTreesClassifier(
        n_estimators=10,
        max_features=None,
        min_samples_leaf=75
    )
    SVC = _SVC(
        C=1,
        probability=True
    )
    MlpModel = _MLPClassifier(
        max_iter=1000
    )

    def __str__(self):
        return str(self.value)


def train(model: RecipeExtractionModel = RecipeExtractionModel.SVC,
          features: _Iterable[str] = _DEFAULT_DRAGNET_FEATURES,
          data_location: str = _DEFAULT_DATA_DIRECTORY) -> _Extractor:
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
