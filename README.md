<h1 align="center">THE AIRBNB PROJECT.</h1>
This is the first project of the AirBnB.

This first step is very important because we will use what we build during this project with all other following projects.

**Classes**
We are going to create a number of classes.

The first class which is the parent class is the **BaseModel Class** .

We will the create other classes that inherit common attributes from this class and their own attributes.

The classes that we will create together with their specific attributes include; 

    1. User                                                               2. Amenity       
            ✹email             ✹first_name                                      ✹name           
            ✹password          ✹last_name
                       

    3. Place                                                              4. State
    
            ✹city_id    ✹description        ✹max_guest                         ✹name                 
            ✹user_id    ✹number_rooms       ✹price_by_night               
            ✹name       ✹number_bathrooms   ✹latitude
            ✹longitude  ✹amenity_ids    
    5. City                                                               6. Review
            ✹State_id                                                           ✹place_id    ✹text
            ✹name                                                               ✹user_id
            
 
 We will then create the **FileStorage Class** 
 
Every time the backend is initialized, an instance of FileStorage called storage is instanciated. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.
  
 <h2>The Console.</h2> 
  
  
  
   
  
         
         
     
         
         
 
