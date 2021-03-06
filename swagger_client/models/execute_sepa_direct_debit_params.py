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


class ExecuteSepaDirectDebitParams(object):
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
        'account_id': 'int',
        'banking_tan': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'banking_tan': 'bankingTan'
    }

    def __init__(self, account_id=None, banking_tan=None):  # noqa: E501
        """ExecuteSepaDirectDebitParams - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._banking_tan = None
        self.discriminator = None

        self.account_id = account_id
        self.banking_tan = banking_tan

    @property
    def account_id(self):
        """Gets the account_id of this ExecuteSepaDirectDebitParams.  # noqa: E501

        Identifier of the bank account that you want to transfer money to  # noqa: E501

        :return: The account_id of this ExecuteSepaDirectDebitParams.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ExecuteSepaDirectDebitParams.

        Identifier of the bank account that you want to transfer money to  # noqa: E501

        :param account_id: The account_id of this ExecuteSepaDirectDebitParams.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def banking_tan(self):
        """Gets the banking_tan of this ExecuteSepaDirectDebitParams.  # noqa: E501

        Banking TAN that the user received from the bank for executing the direct debit order  # noqa: E501

        :return: The banking_tan of this ExecuteSepaDirectDebitParams.  # noqa: E501
        :rtype: str
        """
        return self._banking_tan

    @banking_tan.setter
    def banking_tan(self, banking_tan):
        """Sets the banking_tan of this ExecuteSepaDirectDebitParams.

        Banking TAN that the user received from the bank for executing the direct debit order  # noqa: E501

        :param banking_tan: The banking_tan of this ExecuteSepaDirectDebitParams.  # noqa: E501
        :type: str
        """
        if banking_tan is None:
            raise ValueError("Invalid value for `banking_tan`, must not be `None`")  # noqa: E501

        self._banking_tan = banking_tan

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
        if not isinstance(other, ExecuteSepaDirectDebitParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
