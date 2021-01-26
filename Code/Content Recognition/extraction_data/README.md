# Content Recognition Training Data

This subdirectory contains training data intended for use to train a machine learning model to extract recipe content
from webpages. It is structured as required by the [dragnet](https://github.com/dragnet-org/dragnet#trainingtest-data)
library.

## Contributing

You can help add more data in a few steps:

1. Add your source to `recipe_sources.json`; make sure to add a source category as well (if it's a new website).
2. Run `scrape_and_create_dragnet_structure` inside `scrape_recipes.py`.
   1. Consider utilizing `remove_duplicate_sources` before doing so, so our data collection doesn't get cluttered with
      duplicates (and inadvertently over-weigh certain sources). It'll save you time, too! No need to make a "corrected"
      file if someone already has.
3. Manually add the recipe content to the empty "corrected" files laid out by step 2.
4. Push your changes to give back to the project and to the community.
