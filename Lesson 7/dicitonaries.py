# dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# access items in a dict
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# veritfy a key exists
print("guitar" in band)
print("triangle" in band)

# change the values

band["vocals"] = "coverdale"
band.update({"bass": "JPJ"}
            )
print(band)

# remove items

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# delete or clear items

band["drums"] = "Bonham"
del band["drums"]
print(band)


print(band2)


band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band  # creates a reference, not a copy

# print("bad copy!")
# print(band2)
# print(band)
# band2["drums"] = "dave"
# print(band) # dont do this becasue as you can see if we add something to band2, it also changes the original band

band2 = band.copy()  # the correct way to do this, created a copy
band2["drums"] = "dave"
print("Good copy!")
print(band2)
print(band)

# or use the dict() constructor funtion
band3 = dict(band)
print("Good COpy!")
print(band3)

# nested dictionaries
member1 = {"name": "plant",
           "instrument": "vocals"
           }
member2 = {"name": "page",
           "instrument": "guitar"
           }
band = {
    "member1": member1,
    "member2": member2
}
print("")
print(band)
print(band["member1"]["name"])
print("")

# sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
# no duplicates allowed in a set

nums = {1, 2, 2, 3}
print(nums)
print("")
# true is a dupe of 1, false is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)
print("")

# check if a value is in a set
print(2 in nums)
print(8 in nums)
# but you cannot refer to an element in the set with an index position or key

# add a new elenment toi a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
# you can use update with list tuples, and dictionaries too.

# MERGE 2 SETS TO CREATE A NEW SET
one = {1, 2, 3}
two = {4, 5, 6}
mynewset = one.union(two)
print(mynewset)
# keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)
# keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
