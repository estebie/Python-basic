"""
Exercise 22: Read from file

Given a .txt file that has a list of a bunch of names, 
	count how many of each name there are in the file, 
	and print out the results to the screen. 

I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), 
	take this .txt file, and count how many of each “category” of each image there are. 

This text file is actually a list of files corresponding to the SUN database scene recognition database, 
	and lists the file directory hierarchy for the images. 

Once you take a look at the first line or two of the file, 
	it will be clear which part represents the scene category. 

"""
import re

with open('22-SunDatabase.txt', 'r') as file:
	image_categories = []
	current_image_category = ""

	images = file.read()
	categories = re.findall('(?<=\/.{1}\/)\w+', images)

	for category in categories:
		if current_image_category != category:
			image_categories.append(category)
			current_image_category = category
	print("There are ", len(image_categories), "image categories")

input()