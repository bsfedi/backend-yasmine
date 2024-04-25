from fastapi import APIRouter, HTTPException
from secuirty import *
from user.models import *
from user.services import *
from argon2 import PasswordHasher
import re

user_router = APIRouter(tags=["User"])

ph = PasswordHasher()





@user_router.post(
    "/auth/signup",
)
async def sign_up(user: User):
    """
    Validates a password format based on specified requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    # Get date of today
    now = datetime.now()
    user.role = "client"
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$"
    if re.match(pattern, user.password):
        # hash a passsword
        hashed_password = ph.hash(user.password)
        user.password = hashed_password
        user_id = signup(user)
        return {"message": "user added succesfully !"}
    else:
        raise HTTPException(
            status_code=411,
            detail="Password format is invalid. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.",
        )


@user_router.post(
    "/auth/login",
)
async def login_api(userr: User_login):
    """
    API endpoint for user login.

    Args:
        userr (User_login): User login information (email, password) .

    Returns:
        dict: Dictionary containing user email and access token.

    """
    # retrieves the user from the database by email
    user = get_user_by_email(userr.adresse_mail)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # verify the password hash
    verify_password(user.get("password"), userr.password)

    # Create an access token with user ID
    token = create_access_token({"id": str(user["_id"])})
    return {"user": user["adresse_mail"], "role" : user["role"],"token": token}


@user_router.get(
    "/users",
)
async def get_list_users():
    """
    API endpoint for getting a list of all users.

    Args:
        token (dict): Token required for authentication.

    Returns:
        dict: Dictionary containing a list of all users.

    """

    all_users = get_all_users()
    return {"users": all_users}