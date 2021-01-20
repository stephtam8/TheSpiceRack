import requests as _requests
import os as _os
import json as _json


def _create_dirs(filename):
    try:
        _os.makedirs(_os.path.dirname(filename))
    except FileExistsError:
        pass


def _write_html(filename, html_content):
    _create_dirs(filename)
    with open(filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


def scrape_and_create_dragnet_structure(sources_path,
                                        outputdir=None,
                                        overwrite=False):
    """Scrape recipe websites, saving in dragnet-required structure

    This script takes in a JSON of recipes, delimited by their sources, and
    outputs a directory structure to `outputdir`, containing:
      `HTML/`: The HTML files scraped from this function
      'Corrected/': Blank "corrected" versions of each HTML file

    Parameters
    ----------
    sources_path : str
        The filepath of the recipe sources JSON
    outputdir : str
        The desired filepath for the output of this function. Defaults to a
        directory named 'scraped_data' in your working directory.
    overwrite : bool
        A flag determining if files that already exist should be replaced.
        Defaults `False` (do not overwrite)
    """

    sources = remove_duplicate_sources(sources_path, False)
    if outputdir is None:
        outputdir = _os.path.join(_os.getcwd(), 'scraped_data')

    # Some sites close their content for 'bots', so user-agent must be supplied
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    }
    # Begin scraping each source in our input, as needed
    for source in sources.keys():
        unique_sources = list(dict.fromkeys(sources[source]))
        for index, url in enumerate(unique_sources):
            base_name = str(source) + '-' + str(index + 1) + '.html'
            filename = _os.path.join(outputdir, 'HTML', base_name)

            if overwrite or not _os.path.exists(filename):
                # Extract the HTML content and write it
                html_content = str(_requests.get(url, headers=HEADERS).text)
                _write_html(filename, html_content)

            # Create an empty "corrected" file in "Corrected" directory
            filename = _os.path.join(outputdir, 'Corrected',
                                     base_name + '.corrected.txt')
            if overwrite or not _os.path.exists(filename):
                _create_dirs(filename)
                with open(filename, 'w') as _:
                    pass


def remove_duplicate_sources(sources_path, overwrite=True):
    """Remove duplicate entries in recipe sources JSON

    Parameters
    ----------
    sources_path : str
        The filepath of the recipe sources JSON
    overwrite : bool
        Overwrite the input sources JSON? Defaults true.

    Returns
    -------
    sources : dict
        The unique sources dictionary
    """

    with open(sources_path) as json_file:
        sources = _json.load(json_file)
    for key in sources.keys():
        # In Python 3.7 and up, this even maintains order (not that it strictly
        # needs to, but it's nice)
        sources[key] = list(dict.fromkeys(sources[key]))
    if overwrite:
        with open(sources_path, 'w') as json_file:
            _json.dump(sources, json_file)

    return sources


if __name__ == "__main__":
    scrape_and_create_dragnet_structure(
        '/Users/benhollar/Documents/College/Senior Design/TheSpiceRack/Code/Content Recognition/content_data/recipe_sources.json',
        '/Users/benhollar/Documents/College/Senior Design/TheSpiceRack/Code/Content Recognition/content_data',
        False
    )
