# 3-8. Seeing the World: Think of at least five places in the world youd like to visit.
#  Store the locations in a list. Make sure the list is not in alphabetical order.
#  Print your list in its original order. Dont worry about printing the list neatly, just print it as a raw Python list.
#  Use sorted() to print your list in alphabetical order without modifying the actual list.
#  Show that your list is still in its original order by printing it.
#  Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#  Show that your list is still in its original order by printing it again.
#  Use reverse() to change the order of your list. Print the list to show that its order has changed.
#  Use reverse() to change the order of your list again. Print the list to show its back to its original order.
#  Use sort() to change your list so its stored in alphabetical order. Print the list to show that its order has been changed.
#  Use sort() to change your list so its stored in reverse alphabetical order.
# Print the list to show that its order has chang

# Store the locations in a list. Make sure the list is not in alphabetical order.
indian_city = ['Mumbai','Delhi','Ahmedabad','Bengaluru','Hyderabad']

# Print your list in its original order. Dont worry about printing the list neatly, just print it as a raw Python list.
print "01 Original list:"
print(indian_city)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print""
print "02 Sorted list:"
print(sorted(indian_city))

# Show that your list is still in its original order by printing it.
print""
print ("03 Original list after sorting:")
print(indian_city)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print ""
print ("04 In reverse alphabetical order without changing the order of the original list:")
print(sorted(indian_city, reverse=True))

# Show that your list is still in its original order by printing it.
print""
print "05 Original list after sorting reverse alphabetical order without changing the order of the original list: "
print(indian_city)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
print""
print "06 reverse() to change the order of the original list and print"
indian_city.reverse()
print(indian_city)

#  Use reverse() to change the order of your list again. Print the list to show its back to its original order.
print""
print "07 reverse() to change the order and back to its original order"
indian_city.reverse()
print(indian_city)

# Use sort() to change your list so its stored in alphabetical order. Print the list to show that its order has been changed.
print""
print "08 sort() to change the order permanently"
indian_city.sort()
print(indian_city)

# Use sort() to change your list so its stored in reverse alphabetical order. Print the list to show that its order has changed.
print""
print ("09 sort() to change your list so its stored in reverse alphabetical order. Print the list to show that its order has changed :")
indian_city.reverse()
print(indian_city)










