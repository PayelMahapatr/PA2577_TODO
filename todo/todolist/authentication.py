from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

class RemoteJWTAuthentication(JWTAuthentication):
    """
    Custom JWT auth that validates token signature but
    does not require the user to exist in the local DB.
    """

    def get_user(self, validated_token):
        """
        Instead of looking up a user in todo_service DB,
        return a simple object with user_id from token.
        """
        try:
            user_id = validated_token["user_id"]
        except KeyError:
            raise InvalidToken("Token contained no recognizable user identification")

       # Simple dummy user object
        class SimpleUser:
            def __init__(self, user_id):
                self.id = user_id
                self.is_authenticated = True 

        return SimpleUser(user_id)