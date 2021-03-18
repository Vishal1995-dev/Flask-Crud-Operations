"""Routes for the course resource.
"""

from run import app
from flask import request
from http import HTTPStatus
import data
from data import load_data
import json
from werkzeug.exceptions import BadRequest
import datetime

courses=load_data()
words={}

for i in courses:
    s=courses[i]['title'].split(" ")
    for j in s:
        if(j in words):
            words[j].append(i)
        else:
            words[j]=[i]
            
@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    ret={}
    if(id not in courses):
    	response = app.response_class(
        status=404,
        response="Course not found",
        mimetype='application/json'
    	)
    else:
        ret["data"]=courses[id]
        response = app.response_class(
	    status=200,
	    response=json.dumps(ret),
	    mimetype='application/json'
        )
    return response

@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    content=request.get_json()
    ret=[]
    if('page-size' not in content):
    	size=1
    else:
    	size=content['page-size']
    if('title-words' in content):
        for i in content['title-words']:
           print(i)
           if(i in words):
            	for j in words[i]:
            	    ret.append(courses[j])
            	    size-=1
            	    if(size==0):
            	        break
           if(size==0):
      	    	break      	
    for i in courses:
    	if(size==0):
    	    break
    	ret.append(courses[i])
    	size-=1
    	
    response = app.response_class(
        status=200,
        response=json.dumps(ret),
        mimetype='application/json'
    )
    return response
    	     	    		    
@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    
    content=request.get_json()
    if('title' not in content or 'price' not in content or 'on_discount' not in content):
    	response = app.response_class(
        status=400	,
        response="Enter required data",
        mimetype='application/json'
        )
    else:
    	i=max(courses)+1
    	courses[i]=content
    	now = datetime.datetime.now()
    	courses[i]['date_created']=now.strftime("%Y-%m-%d %H:%M:%S")
    	courses[i]['date_updated']=now.strftime("%Y-%m-%d %H:%M:%S")
    	response = app.response_class(
            status=201,
            response=json.dumps(courses),
            mimetype='application/json'
        )
    return response


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    content=request.get_json()
    if(id not in courses):
    	response = app.response_class(
        status=400,
        response="Id does not match payload",
        mimetype='application/json'
        )	
    else:
    	courses[id]=content
    	now = datetime.datetime.now()
    	courses[id]['date_updated']=now.strftime("%Y-%m-%d %H:%M:%S")
    	response = app.response_class(
            status=200,
            response=json.dumps(courses),
            mimetype='application/json'
        )
    return response


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    if(id not in courses):
    	response = app.response_class(
        status=404,
        response="Course does not exist",
        mimetype='application/json'
        )	
    else:
    	courses.pop(id)
    	response = app.response_class(
            status=200,
            response="Specified course deleted",
            mimetype='application/json'
        )
    return response

