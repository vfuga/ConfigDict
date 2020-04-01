# ConfigDict
from scratch

The puprose of this POC is to find and justify a better approach for storing configuration of any arbitrary data science model

    - On of the most sufficient ideas is having tree based structue and access to any parameter using a string with dots as a key. Easy access to parameter in IDE using "intellisense".This should allow easily extract/save any related group of parameters

    - The second idea is the abitity to unroll the tree structue into one dimentional array. This should allow easily access and change values of any the node in a tree just using key/value syntax as well as making a dictionary of all nodes.

    - The __repr__() method should reflect the actuall tree-based structure of the config container

    - The __str__() method must work like the __repr__() method, but all the indentation, spaces and carriage returns or new line symbols have to be removed from the returning string

    - constructor have to convert any dictionary of nested dictionay into the ConfigDict object
    serialize ConfigDict into ordinary dict and vice versa
