# nesting list , dictionary , inside another dictionary
#syntax
dict_1={
    "key1":[list],
    "key2":{dict}
}

#nesting a list in a dictionary

travel_log1={
    "France":["Paris","Lisle","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}

# nesting a dictionary in a dictionary

travel_log2={
    "France":{"cities_visited":["Paris","Lisle","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5},
}

#nesting a dictionary in a list
#syntax

list_1=[{
    "key1":[list],
    "key2":{dict}
},
{   "key1":"value1",
    "key2":"value2"
        }]

#example

travel_log3=[
    {
        "country":"France",
        "cities_visited":["Paris","Lisle","Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","hamburg","stuttgart"],
        "total_visits":5
    }
]

print(travel_log3[0]) # retriving item from list.
print(travel_log2["Germany"]) # retriving item from dictionary.