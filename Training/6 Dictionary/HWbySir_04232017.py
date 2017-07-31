from collections import Counter
import string

# A variable with multi lines string
multi_line_string = """Large volumes of hard rock dumped into rivers by landslides can increase flood risk up to hundreds
                    of kilometres downstream, potentially affecting millions of people, researchers say. The findings
                    could help researchers improve flood risk maps for the Ganga Plain, a low-lying region covering parts
                    of India, Nepal and Pakistan. They could also provide fresh insight into the long-term impacts of
                    earthquakes and storms in the region. Until now, little was known about how landslides in the
                    Himalaya could affect flood risk downstream on the Ganga Plain.For the first time, scientists at
                    the University of Edinburgh have traced the path of rocks washed down from the Himalayan mountains
                    onto the Plain. They found that large landslides in the southern, lower elevation ranges of the
                    Himalaya are more likely to increase flood risk than those in the high mountains further north.Rocks
                    in the south are extremely hard and travel only a short distance -- less than 20 km -- to reach the
                    Plain. This means much of this rock -- such as quartzite -- reaches the Plain as gravel or pebbles,
                    which can build up in rivers, altering the natural path of the water, the team says.Rocks from more
                    northerly regions of the Himalaya tend to be softer, and the team found they often travel at least
                    100 km to reach the Plain. These types of rock -- including limestone and gneiss -- are gradually
                    broken down into sand which, unlike gravel and pebbles, is dispersed widely as it travels downstream.
                    Understanding whether landslides will produce vast quantities of gravel or sand is crucial for
                    predicting how rivers on the Ganga Plain will be affected, researchers say.The study is published
                    in the journal Nature. The research was funded by the Natural Environment Research Council.Elizabeth
                    Dingle, PhD student in the University of Edinburgh's School of GeoSciences, who led the study,
                    said: "Our findings help to explain how events in the Himalaya can have drastic effects on rivers
                    downstream and on the people who live there. Knowing where landslides take place in the mountains
                    could help us better predict whether or not large deposits of gravel will reach the Ganga Plain
                    and increase flood risk." ?.-;: """

print string.punctuation

# Use set(string.punctuation) to remove all punctuation
punct = set(string.punctuation)
sans_punct = ''.join(x for x in multi_line_string if x not in punct)

# remove_space = multi_line_string.replace(' ','')
# print(remove_space)

# Remove the punctuation using regex
# multi_line_string = re.sub(r'[?||.|!|-|,|;|:|(|)|{|}|[|]|^| ]', r'', multi_line_string)
# print (multi_line_string)

wordCount = {}

# Slice the multi_line_strint string variable and convert in to a list
for string in sans_punct.splitlines():
    for word in string.split():
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

print wordCount

print "################"


splitted_string = sans_punct.split(" ")

# Store list in a dictionary
dictionary = {
              'key': splitted_string
             }
