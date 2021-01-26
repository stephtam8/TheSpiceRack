import numpy as _numpy
import pandas as _pandas
import os as _os


DEFAULT_DATA_DIRECTORY = _os.path.join(
    _os.path.dirname(_os.path.dirname(__file__)),
    'extraction_data',
    'Corrected')
DEFAULT_OUTPUT_PATH = _os.path.join(
    _os.path.dirname(__file__),
    'classification_data.csv')


def generate_data(extraction_data=DEFAULT_DATA_DIRECTORY,
                  output_path=DEFAULT_OUTPUT_PATH):
    """Generate classification training data from content extraction dataset

    This function is highly dependent on the structure of the content extraction
    dataset and should be used accordingly. If changes are made there, they will
    effect the result of this function. Check the output accordingly.

    Given the "Corrected" extraction data, create a CSV for each line of those
    files, assigning a class -- "title", "ingredient", "instruction", "other" --
    to each line.

    Parameters
    ----------
    extraction_data : string
        The path to the directory containing the "Corrected" extraction training
        data
    output_path : string
        The desired path of the output CSV
    """

    original_text = _numpy.array([], dtype='object')
    classified_type = _numpy.array([], dtype='object')

    for filename in _os.listdir(extraction_data):
        filename = _os.path.join(extraction_data, filename)
        with open(filename) as text_file:
            if not filename.endswith('.txt'):
                continue

            lines = [line.rstrip() for line in text_file]

            original_text = _numpy.append(original_text, lines[0])
            classified_type = _numpy.append(classified_type, 'title')

            current_class = ''
            ingredients_done = False
            for line in lines[1:]:
                if line == '':
                    current_class = 'other'
                    continue

                original_text = _numpy.append(original_text, line)
                classified_type = _numpy.append(classified_type, current_class)

                if current_class == 'other':
                    if not ingredients_done:
                        current_class = 'ingredient'
                    else:
                        current_class = 'instruction'
                    ingredients_done = True

    data_frame = _pandas.DataFrame(columns=['Text', 'Class'])
    data_frame['Text'] = original_text
    data_frame['Class'] = classified_type
    data_frame.to_csv(output_path, index=False)


if __name__ == '__main__':
    generate_data()
