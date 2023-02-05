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
 
 This is the command line interpreter used to handle and manipulate all classes utilized by the application.
 
 This is how it can be used;
 
 **Start it**
 
 It can be started by running the console.py file.
 
 For example; 
  
     $ ./console.py
     
 In interactive mode, there will be a **(hbnb)** prompt.
 
 Enter the **quit** command to quit.
 
 <h3>Commands</h3>
 
 **create**: Creates a given class, saves it (to the JSON file) and prints the id.
 
     $ ./console.py
    (hbnb) create BaseModel
    119be863-6fe5-437e-a180-b9892e8746b8
    (hbnb) quit
    $ cat file.json ; echo ""
    {"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
    1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
    Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
    
 **show**: Prints the string representation of an instance based on the class name and id.
 
     (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
     [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
     'id': '49faff9a-6318-451f-87b6-        910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
     
**destroy**: Deletes an instance based on the class name and id.

**all**: Prints all string representation of all instances based or not on the class name.

     (hbnb) all BaseModel
     ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime
     (2017, 10, 2, 3, 11, 23,   639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}",
     "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907',
     'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
     'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
     
**update**: Updates an instance based on the class name and id by adding or updating attribute
  
 
  
  
   
  
         
         
     
         
         
 
