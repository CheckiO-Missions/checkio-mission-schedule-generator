"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Monday", 1, ["customer service", "sales"]]],
            "answer": [[], ["Alice"]],
        },
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Monday", 2, ["customer service", "sales"]]],
            "answer": [["Charlie"], ["Alice"]],
        }, 
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory"]
    },
}, ["Wednesday", 1, ["customer service", "sales", "inventory"]]],
            "answer": [[], []], 
        }
    ],
    "Extra": [
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 1, ["customer service"]]],
            "answer": [[], ["Alice"]],
        },
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "inventory"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 1, ["customer service", "sales"]]],
            "answer": [["Bob"], []],
        }, 
        {
            "input": [{
    "Charlie": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
    "Alice": {
        "pref_shifts": ["second"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["inventory"]
    },
    "Bob": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales"]
    },
}, ["Wednesday", 4, ["customer service", "sales"]]],
            "answer": [["Bob", "Charlie"], ["Alice", "Charlie"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Monday", 3, ["customer service", "sales", "cleaning"]]], 
            "answer": [["Alice", "Eve"], ["Eve"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Tuesday", 2, ["inventory", "customer service"]]], 
            "answer": [["Eve"], ["David"]], 
        },
        {
            "input": [{
    "Alice": {
        "pref_shifts": ["first"],
        "days_off": ["Saturday", "Sunday"],
        "skills": ["customer service", "sales", "cleaning"]
    },
    "Bob": {
        "pref_shifts": ["second"],
        "days_off": ["Monday", "Tuesday"],
        "skills": ["customer service", "inventory", "cleaning"]
    },
    "Charlie": {
        "pref_shifts": ["first"],
        "days_off": ["Wednesday"],
        "skills": ["customer service", "inventory", "cleaning", "sales"]
    },
    "David": {
        "pref_shifts": ["second"],
        "days_off": ["Friday"],
        "skills": ["customer service", "inventory", "sales"]
    },
    "Eve": {
        "pref_shifts": ["first", "second"],
        "days_off": ["Thursday"],
        "skills": ["customer service", "sales"]
    }
}, ["Thursday", 4, ["sales", "inventory", "customer service", "cleaning"]]], 
            "answer": [["Alice", "Charlie"], ["Bob", "David"]], 
        },
    ]
}
