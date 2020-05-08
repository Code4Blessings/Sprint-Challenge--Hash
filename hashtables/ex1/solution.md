Merging Two Packages


Given a package with a weight limit `limit` and a list `weights` of item


weights, implement a function `get_indices_of_item_weights` that finds

two items whose sum of weights equals the weight limit `limit`. Your
- 

function will return an instance of an `Answer` tuple that has the
following form:

```
(zero, one)
```

where each element represents the item weights of the two packages.
_**The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.**_ If such a
pair doesn’t exist for the given inputs, your function should return
`None`.

Your solution should run in linear time.

Example:
```
input: weights = [4, 6, 10, 15, 16], length = 5, limit = 21
# since these are the indices of weights 15 and 6 whose sum equals 21
output: [3, 1]
```


What is an item in a dictionary?
- A key: value pair 
- A package would be the dictionary
Therefore:
    package = {
        "limit": 100
        "weight": [weight1, weight3, weight3]
    }

