# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.42.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExecutePasswordChangeParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'password': 'str',
        'password_change_token': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'password': 'password',
        'password_change_token': 'passwordChangeToken'
    }

    def __init__(self, user_id=None, password=None, password_change_token=None):  # noqa: E501
        """ExecutePasswordChangeParams - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._password = None
        self._password_change_token = None
        self.discriminator = None

        self.user_id = user_id
        self.password = password
        self.password_change_token = password_change_token

    @property
    def user_id(self):
        """Gets the user_id of this ExecutePasswordChangeParams.  # noqa: E501

        User identifier  # noqa: E501

        :return: The user_id of this ExecutePasswordChangeParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExecutePasswordChangeParams.

        User identifier  # noqa: E501

        :param user_id: The user_id of this ExecutePasswordChangeParams.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if user_id is not None and not re.search('[a-zA-Z0-9\\-_\\.\\+@]*', user_id):  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must be a follow pattern or equal to `/[a-zA-Z0-9\\-_\\.\\+@]*/`")  # noqa: E501

        self._user_id = user_id

    @property
    def password(self):
        """Gets the password of this ExecutePasswordChangeParams.  # noqa: E501

        User's new password. Minimum length is 6, and maximum length is 36.  # noqa: E501

        :return: The password of this ExecutePasswordChangeParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ExecutePasswordChangeParams.

        User's new password. Minimum length is 6, and maximum length is 36.  # noqa: E501

        :param password: The password of this ExecutePasswordChangeParams.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', password):  # noqa: E501
            raise ValueError("Invalid value for `password`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._password = password

    @property
    def password_change_token(self):
        """Gets the password_change_token of this ExecutePasswordChangeParams.  # noqa: E501

        Decrypted password change token (the token that you received from the /users/requestPasswordChange service, decrypted with your data decryption key)  # noqa: E501

        :return: The password_change_token of this ExecutePasswordChangeParams.  # noqa: E501
        :rtype: str
        """
        return self._password_change_token

    @password_change_token.setter
    def password_change_token(self, password_change_token):
        """Sets the password_change_token of this ExecutePasswordChangeParams.

        Decrypted password change token (the token that you received from the /users/requestPasswordChange service, decrypted with your data decryption key)  # noqa: E501

        :param password_change_token: The password_change_token of this ExecutePasswordChangeParams.  # noqa: E501
        :type: str
        """
        if password_change_token is None:
            raise ValueError("Invalid value for `password_change_token`, must not be `None`")  # noqa: E501
        if password_change_token is not None and not re.search('[0-9a-f\\-]*', password_change_token):  # noqa: E501
            raise ValueError("Invalid value for `password_change_token`, must be a follow pattern or equal to `/[0-9a-f\\-]*/`")  # noqa: E501

        self._password_change_token = password_change_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecutePasswordChangeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
