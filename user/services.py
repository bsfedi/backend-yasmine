
from fastapi import HTTPException
from database import db
import argon2

def signup(user):
    # Create a new dictionary to store the user data
    new_user = dict(user)

    # The collection is not empty, so we need to check if the user already exists and if the email domain matches an admin's domain
    if db["users"].find_one({"adresse_mail": new_user["adresse_mail"]}):
        raise HTTPException(status_code=409, detail="Email address already in use")
    
    # Insert the new user into the database
    response = db["users"].insert_one(new_user)

    if response:
        return {
            "message": "User added successfully !",
            "user_id": response.inserted_id,
        }


def get_user_by_email(email):
    # Query the database to find a user by email
    user = db["users"].find_one(dict(adresse_mail=email))
    # Return the user object if found, or None if not found
    return user


def get_all_users():
    user_list = []
    try:
        for user in db["users"].find():
            # Convert ObjectId to string
            user["_id"] = str(user["_id"]) 
            # Convert the bytes to a base64-encoded string using base64.b64encode
            user_list.append(user)  # Append user object to user_list

        return user_list  # Return the list of users
    except Exception as ex:
        return {
            "message": f"{str(ex)}"
        }  # Return an error message with exception details if an exception occurs


def verify_password(hashed_password, password):
    try:
        # Verify if the provided password matches the hashed password
        if argon2.PasswordHasher().verify(hashed_password, password):
            # Return a message indicating that the password is correct
            return {"message": "Password is correct!"}
        else:
            # Raise an HTTPException with appropriate error message if password is invalid
            raise HTTPException(status_code=411, detail="Invalid password")
    except argon2.exceptions.VerifyMismatchError:
        # Raise an HTTPException with appropriate error message if password is incorrect
        raise HTTPException(status_code=412, detail="Incorrect password!")
    

