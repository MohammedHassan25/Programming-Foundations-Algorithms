# --------------------------------------------------------------------------------------------------------------------
# A hash table is a form of what's called an associative array.
# One of the primary benefits of hash tables is their ability to uniquely map a given key to a specific value
# Hash tables are typically very fast
# For small datasets, arrays are usually more efficient
# Hash tables don't order entries in a predictable way
# --------------------------------------------------------------------------------------------------------------------

# Example

# create hash table

moh = dict({"moh1": 1, "moh2": 2, "moh3": 3})
print(moh)

# create empty hash table

Moh = {}
Moh["MOH1"] = 1
Moh["MOH2"] = 2
Moh["MOH3"] = 3
Moh["MOH4"] = 4
print(Moh)

# replace an item

Moh["MOH3"] = 'three'
print(Moh)

# iterate the keys and values in te dictionary

for m, n in Moh.items():
    print(("Key :", m, " value: ", n))
