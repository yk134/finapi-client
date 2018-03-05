# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserUpdateParamsImpl(object):
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
        'email': 'str',
        'phone': 'str',
        'is_auto_update_enabled': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'phone': 'phone',
        'is_auto_update_enabled': 'isAutoUpdateEnabled'
    }

    def __init__(self, email=None, phone=None, is_auto_update_enabled=False):  # noqa: E501
        """UserUpdateParamsImpl - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._phone = None
        self._is_auto_update_enabled = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        self.is_auto_update_enabled = is_auto_update_enabled

    @property
    def email(self):
        """Gets the email of this UserUpdateParamsImpl.  # noqa: E501

        User's new email address. Maximum length is 320. Pass an empty string (\"\") if you want to clear the current email address.  # noqa: E501

        :return: The email of this UserUpdateParamsImpl.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserUpdateParamsImpl.

        User's new email address. Maximum length is 320. Pass an empty string (\"\") if you want to clear the current email address.  # noqa: E501

        :param email: The email of this UserUpdateParamsImpl.  # noqa: E501
        :type: str
        """
        if email is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', email):  # noqa: E501
            raise ValueError("Invalid value for `email`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UserUpdateParamsImpl.  # noqa: E501

        User's new phone number. Maximum length is 50. Pass an empty string (\"\") if you want to clear the current phone number.  # noqa: E501

        :return: The phone of this UserUpdateParamsImpl.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserUpdateParamsImpl.

        User's new phone number. Maximum length is 50. Pass an empty string (\"\") if you want to clear the current phone number.  # noqa: E501

        :param phone: The phone of this UserUpdateParamsImpl.  # noqa: E501
        :type: str
        """
        if phone is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', phone):  # noqa: E501
            raise ValueError("Invalid value for `phone`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._phone = phone

    @property
    def is_auto_update_enabled(self):
        """Gets the is_auto_update_enabled of this UserUpdateParamsImpl.  # noqa: E501

        Whether the user's bank connections will get updated in the course of finAPI's automatic batch update. Note that the automatic batch update will only update bank connections where all of the following applies:</br></br> - the PIN is stored in finAPI for the bank connection</br> - the previous update using the stored credentials did not fail due to the credentials being incorrect (or there was no previous update with the stored credentials)</br> - the bank that the bank connection relates to is included in the automatic batch update (please contact your Sys-Admin for details about the batch update configuration)</br></br>Also note that the automatic batch update must generally be enabled for your client in order for this field to have any effect.<br/><br/>WARNING: The automatic update will always download transactions and security positions for any account that it updates! This means that the user will no longer be able to download just the balances for his accounts once the automatic update has run (The 'skipPositionsDownload' flag in the bankConnections/update service can no longer be set to true).  # noqa: E501

        :return: The is_auto_update_enabled of this UserUpdateParamsImpl.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_update_enabled

    @is_auto_update_enabled.setter
    def is_auto_update_enabled(self, is_auto_update_enabled):
        """Sets the is_auto_update_enabled of this UserUpdateParamsImpl.

        Whether the user's bank connections will get updated in the course of finAPI's automatic batch update. Note that the automatic batch update will only update bank connections where all of the following applies:</br></br> - the PIN is stored in finAPI for the bank connection</br> - the previous update using the stored credentials did not fail due to the credentials being incorrect (or there was no previous update with the stored credentials)</br> - the bank that the bank connection relates to is included in the automatic batch update (please contact your Sys-Admin for details about the batch update configuration)</br></br>Also note that the automatic batch update must generally be enabled for your client in order for this field to have any effect.<br/><br/>WARNING: The automatic update will always download transactions and security positions for any account that it updates! This means that the user will no longer be able to download just the balances for his accounts once the automatic update has run (The 'skipPositionsDownload' flag in the bankConnections/update service can no longer be set to true).  # noqa: E501

        :param is_auto_update_enabled: The is_auto_update_enabled of this UserUpdateParamsImpl.  # noqa: E501
        :type: bool
        """
        if is_auto_update_enabled is None:
            raise ValueError("Invalid value for `is_auto_update_enabled`, must not be `None`")  # noqa: E501

        self._is_auto_update_enabled = is_auto_update_enabled

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
        if not isinstance(other, UserUpdateParamsImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other