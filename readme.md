# Simulated Annealing for Traveling Salesman problem

## Dependencies

`pip install -r requirements.txt`

## Dataset

[Initial dataset](https://gist.github.com/nalgeon/5307af065ff0e3bc97927c832fabe26b) contained almost all cities of Russia. Top 30 cities with biggest population were exported into smaller [dataset](/dataset/top30_cities.csv).

## Sources

- `export.py` - exports top 30 cities from `dataset/cities.csv` to `dataset/top30_cities.csv`
- `sa.py` - implementation of Simulated Annealing

## Graphics

See `images` directory.

![img2](https://user-images.githubusercontent.com/7482065/48836697-88bf9600-ed94-11e8-818c-40783c11c637.png)


![anneal_animation](https://user-images.githubusercontent.com/7482065/48839813-bceb8480-ed9d-11e8-9e8c-b4f800eef46d.gif)
