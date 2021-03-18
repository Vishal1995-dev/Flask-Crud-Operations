# Flask-Crud-Operations

Created a courses dictionary with course id as the key so that the user can perform operations on courses using id in linear time.

Also created a dictionary named words having all the title words as keys and id of course titles having those words as value. This would help in getting the courses based on title-words.
In case of get courses using title-words if title words are not given then it gives the page-size number of courses. If page-size is not provided then it considers page-size as one by default.

For testing the API's, I have used pytest. All the get,post,put and delete API are tested for correct input as well as wrong input.
PFA the screenshot for same.
