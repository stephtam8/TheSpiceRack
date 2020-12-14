import os
from typing import Iterable
import requests
import multiprocessing

import dragnet.model_training
from dragnet.data_processing import extract_all_gold_standard_data
from dragnet.extractor import Extractor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier


KNeighborsModel = KNeighborsClassifier(
    n_neighbors=10,
    weights='distance'
)

ExtraTreesModel = ExtraTreesClassifier(
    n_estimators=10,
    max_features=None,
    min_samples_leaf=75
)

DEFAULT_FEATURES = ('kohlschuetter', 'weninger', 'readability')


def train_model(features: Iterable[str] = DEFAULT_FEATURES,
                model=KNeighborsModel):
    """Train a content extraction model using dragnet and sklearn

    Parameters
    ----------
    features : str iterable
        The `dragnet` features to use in this model
    model
        An initialized `sklearn` classifier, e.g. KNeighborsClassifier

    Returns
    -------
    dragnet.Extractor
        The trained content extraction model. A pickled version is also saved
        to disk in the `training_output/` directory
    """

    rootdir = os.path.join(os.path.dirname(__file__), 'content_data/')
    outdir = os.path.join(os.path.dirname(__file__), 'training_output/')
    extract_all_gold_standard_data(rootdir,
                                   nprocesses=multiprocessing.cpu_count() - 1,
                                   overwrite=True)

    base_extractor = Extractor(
        features=features,
        to_extract='content',
        model=model
    )
    extractor = dragnet.model_training.train_model(base_extractor,
                                                   rootdir,
                                                   outdir)
    return extractor


if __name__ == "__main__":
    extractor = train_model()
