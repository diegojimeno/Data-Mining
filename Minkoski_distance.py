#!/usr/bin/python

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, 
          	      "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, 
                      "The Strokes": 2.5, "Vampire Weekend": 2.0},

	     "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, 
                      "Deadmau5": 4.0, "Phoenix": 2.0, 
                      "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},  

             "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, 
                      "Deadmau5": 1.0, "Norah Jones": 3.0, 
                      "Phoenix": 5, "Slightly Stoopid": 1.0}, 

              "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, 
                      "Deadmau5": 4.5, "Phoenix": 3.0, 
                      "Slightly Stoopid": 4.5, "The Strokes": 4.0, 
                      "Vampire Weekend": 2.0},   
    
           "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, 
                      "Norah Jones": 4.0, "The Strokes": 4.0, 
                      "Vampire Weekend": 1.0}, 

           "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, 
                      "Phoenix": 5.0, "Slightly Stoopid": 4.5, 
                      "The Strokes": 4.0, "Vampire Weekend": 4.0}, 

              "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, 
                      "Norah Jones": 3.0, "Phoenix": 5.0, 
                      "Slightly Stoopid": 4.0,  "The Strokes": 5.0},  
 
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, 
                      "Phoenix": 4.0,  "Slightly Stoopid": 2.5, 
                      "The Strokes": 3.0}}

def minkowski( r, dataset1, dataset2 ):
	"""Generates minkowski analysis over a data set given . r determines the
	   type of analysis so to determine the values to be yielded"""
	
	closestDistance = 0
	
	for key in dataset1:
		if( key in dataset2 ):
			closestDistance += pow(abs(dataset1[key] - dataset2[key]), r)
	
	return pow( closestDistance , ( 1/r ) )
			
def computeNearestNeighbor( r, username, users ):
    	"""creates a sorted list of users based on their distance to
    	   username using previous defined minkowski's"""
    	distances = []
    	for user in users:
        	if user != username:
            		distance = minkowski( r, users[user], users[username] )
            		distances.append(( distance, user ))
    	# sort based on distance -- closest first
    	distances.sort()
	return distances



print minkowski(1,users["Angelica"], users["Bill"])
print minkowski(2,users["Chan"], users["Veronica"])
print computeNearestNeighbor(1,"Angelica", users)
print computeNearestNeighbor(2,"Angelica", users)

