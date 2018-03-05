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


class ClientConfigurationParams(object):
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
        'user_notification_callback_url': 'str',
        'user_synchronization_callback_url': 'str',
        'refresh_tokens_validity_period': 'int',
        'user_access_tokens_validity_period': 'int',
        'client_access_tokens_validity_period': 'int'
    }

    attribute_map = {
        'user_notification_callback_url': 'userNotificationCallbackUrl',
        'user_synchronization_callback_url': 'userSynchronizationCallbackUrl',
        'refresh_tokens_validity_period': 'refreshTokensValidityPeriod',
        'user_access_tokens_validity_period': 'userAccessTokensValidityPeriod',
        'client_access_tokens_validity_period': 'clientAccessTokensValidityPeriod'
    }

    def __init__(self, user_notification_callback_url=None, user_synchronization_callback_url=None, refresh_tokens_validity_period=None, user_access_tokens_validity_period=None, client_access_tokens_validity_period=None):  # noqa: E501
        """ClientConfigurationParams - a model defined in Swagger"""  # noqa: E501

        self._user_notification_callback_url = None
        self._user_synchronization_callback_url = None
        self._refresh_tokens_validity_period = None
        self._user_access_tokens_validity_period = None
        self._client_access_tokens_validity_period = None
        self.discriminator = None

        if user_notification_callback_url is not None:
            self.user_notification_callback_url = user_notification_callback_url
        if user_synchronization_callback_url is not None:
            self.user_synchronization_callback_url = user_synchronization_callback_url
        if refresh_tokens_validity_period is not None:
            self.refresh_tokens_validity_period = refresh_tokens_validity_period
        if user_access_tokens_validity_period is not None:
            self.user_access_tokens_validity_period = user_access_tokens_validity_period
        if client_access_tokens_validity_period is not None:
            self.client_access_tokens_validity_period = client_access_tokens_validity_period

    @property
    def user_notification_callback_url(self):
        """Gets the user_notification_callback_url of this ClientConfigurationParams.  # noqa: E501

        Callback URL to which finAPI sends the notification messages that are triggered from the automatic batch update of the users' bank connections. This field is only relevant if the automatic batch update is enabled for your client. For details about what the notification messages look like, please see the documentation in the 'Notification Rules' section. finAPI will call this URL with HTTP method POST. Note that the response of the call is not processed by finAPI. Also note that while the callback URL may be a non-secured (http) URL on the finAPI sandbox or alpha environment, it MUST be a SSL-secured (https) URL on the finAPI live system.<p>The maximum allowed length of the URL is 512. If you have previously set a callback URL and now want to clear it (thus disabling user-related notifications altogether), you can pass an empty string (\"\").  # noqa: E501

        :return: The user_notification_callback_url of this ClientConfigurationParams.  # noqa: E501
        :rtype: str
        """
        return self._user_notification_callback_url

    @user_notification_callback_url.setter
    def user_notification_callback_url(self, user_notification_callback_url):
        """Sets the user_notification_callback_url of this ClientConfigurationParams.

        Callback URL to which finAPI sends the notification messages that are triggered from the automatic batch update of the users' bank connections. This field is only relevant if the automatic batch update is enabled for your client. For details about what the notification messages look like, please see the documentation in the 'Notification Rules' section. finAPI will call this URL with HTTP method POST. Note that the response of the call is not processed by finAPI. Also note that while the callback URL may be a non-secured (http) URL on the finAPI sandbox or alpha environment, it MUST be a SSL-secured (https) URL on the finAPI live system.<p>The maximum allowed length of the URL is 512. If you have previously set a callback URL and now want to clear it (thus disabling user-related notifications altogether), you can pass an empty string (\"\").  # noqa: E501

        :param user_notification_callback_url: The user_notification_callback_url of this ClientConfigurationParams.  # noqa: E501
        :type: str
        """

        self._user_notification_callback_url = user_notification_callback_url

    @property
    def user_synchronization_callback_url(self):
        """Gets the user_synchronization_callback_url of this ClientConfigurationParams.  # noqa: E501

        Callback URL for user synchronization. This field should be set if you - as a finAPI customer - have multiple clients using finAPI. In such case, all of your clients will share the same user base, making it possible for a user to be created in one client, but then deleted in another. To keep the client-side user data consistent in all clients, you should set a callback URL for each client. finAPI will send a notification to the callback URL of each client whenever a user of your user base gets deleted. Note that finAPI will send a deletion notification to ALL clients, including the one that made the user deletion request to finAPI. So when deleting a user in finAPI, a client should rely on the callback to delete the user on its own side. <p>The notification that finAPI sends to the clients' callback URLs will be a POST request, with this body: <pre>{    \"userId\" : string // contains the identifier of the deleted user    \"event\" : string // this will always be \"DELETED\" }</pre><br/>Note that finAPI does not process the response of this call. Also note that while the callback URL may be a non-secured (http) URL on the finAPI sandbox or alpha system, it MUST be a SSL-secured (https) URL on the live system.</p>As long as you have just one client, you can ignore this field and let it be null. However keep in mind that in this case your client will not receive any callback when a user gets deleted - so the deletion of the user on the client-side must not be forgotten. Of course you may still use the callback URL even for just one client, if you want to implement the deletion of the user on the client-side via the callback from finAPI.<p> The maximum allowed length of the URL is 512. If you have previously set a callback URL and now want to clear it (thus disabling user synchronization related notifications for this client), you can pass an empty string (\"\").  # noqa: E501

        :return: The user_synchronization_callback_url of this ClientConfigurationParams.  # noqa: E501
        :rtype: str
        """
        return self._user_synchronization_callback_url

    @user_synchronization_callback_url.setter
    def user_synchronization_callback_url(self, user_synchronization_callback_url):
        """Sets the user_synchronization_callback_url of this ClientConfigurationParams.

        Callback URL for user synchronization. This field should be set if you - as a finAPI customer - have multiple clients using finAPI. In such case, all of your clients will share the same user base, making it possible for a user to be created in one client, but then deleted in another. To keep the client-side user data consistent in all clients, you should set a callback URL for each client. finAPI will send a notification to the callback URL of each client whenever a user of your user base gets deleted. Note that finAPI will send a deletion notification to ALL clients, including the one that made the user deletion request to finAPI. So when deleting a user in finAPI, a client should rely on the callback to delete the user on its own side. <p>The notification that finAPI sends to the clients' callback URLs will be a POST request, with this body: <pre>{    \"userId\" : string // contains the identifier of the deleted user    \"event\" : string // this will always be \"DELETED\" }</pre><br/>Note that finAPI does not process the response of this call. Also note that while the callback URL may be a non-secured (http) URL on the finAPI sandbox or alpha system, it MUST be a SSL-secured (https) URL on the live system.</p>As long as you have just one client, you can ignore this field and let it be null. However keep in mind that in this case your client will not receive any callback when a user gets deleted - so the deletion of the user on the client-side must not be forgotten. Of course you may still use the callback URL even for just one client, if you want to implement the deletion of the user on the client-side via the callback from finAPI.<p> The maximum allowed length of the URL is 512. If you have previously set a callback URL and now want to clear it (thus disabling user synchronization related notifications for this client), you can pass an empty string (\"\").  # noqa: E501

        :param user_synchronization_callback_url: The user_synchronization_callback_url of this ClientConfigurationParams.  # noqa: E501
        :type: str
        """

        self._user_synchronization_callback_url = user_synchronization_callback_url

    @property
    def refresh_tokens_validity_period(self):
        """Gets the refresh_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501

        The validity period that newly requested refresh tokens initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire (Unless explicitly invalidated, e.g. by revocation , or when a user gets locked, or when the password is reset for a user).  # noqa: E501

        :return: The refresh_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :rtype: int
        """
        return self._refresh_tokens_validity_period

    @refresh_tokens_validity_period.setter
    def refresh_tokens_validity_period(self, refresh_tokens_validity_period):
        """Sets the refresh_tokens_validity_period of this ClientConfigurationParams.

        The validity period that newly requested refresh tokens initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire (Unless explicitly invalidated, e.g. by revocation , or when a user gets locked, or when the password is reset for a user).  # noqa: E501

        :param refresh_tokens_validity_period: The refresh_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :type: int
        """

        self._refresh_tokens_validity_period = refresh_tokens_validity_period

    @property
    def user_access_tokens_validity_period(self):
        """Gets the user_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501

        The validity period that newly requested access tokens for users initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire.  # noqa: E501

        :return: The user_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :rtype: int
        """
        return self._user_access_tokens_validity_period

    @user_access_tokens_validity_period.setter
    def user_access_tokens_validity_period(self, user_access_tokens_validity_period):
        """Sets the user_access_tokens_validity_period of this ClientConfigurationParams.

        The validity period that newly requested access tokens for users initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire.  # noqa: E501

        :param user_access_tokens_validity_period: The user_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :type: int
        """

        self._user_access_tokens_validity_period = user_access_tokens_validity_period

    @property
    def client_access_tokens_validity_period(self):
        """Gets the client_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501

        The validity period that newly requested access tokens for clients initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire.  # noqa: E501

        :return: The client_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :rtype: int
        """
        return self._client_access_tokens_validity_period

    @client_access_tokens_validity_period.setter
    def client_access_tokens_validity_period(self, client_access_tokens_validity_period):
        """Sets the client_access_tokens_validity_period of this ClientConfigurationParams.

        The validity period that newly requested access tokens for clients initially have (in seconds). The value must be greater than or equal to 60, or 0. A value of 0 means that the tokens never expire.  # noqa: E501

        :param client_access_tokens_validity_period: The client_access_tokens_validity_period of this ClientConfigurationParams.  # noqa: E501
        :type: int
        """

        self._client_access_tokens_validity_period = client_access_tokens_validity_period

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
        if not isinstance(other, ClientConfigurationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other