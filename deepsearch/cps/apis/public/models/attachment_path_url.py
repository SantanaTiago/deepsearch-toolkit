# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.public.configuration import Configuration


class AttachmentPathUrl(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attachment_path': 'str',
        'upload_url': 'object'
    }

    attribute_map = {
        'attachment_path': 'attachment_path',
        'upload_url': 'upload_url'
    }

    def __init__(self, attachment_path=None, upload_url=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentPathUrl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachment_path = None
        self._upload_url = None
        self.discriminator = None

        self.attachment_path = attachment_path
        self.upload_url = upload_url

    @property
    def attachment_path(self):
        """Gets the attachment_path of this AttachmentPathUrl.  # noqa: E501

        Attachment path.  # noqa: E501

        :return: The attachment_path of this AttachmentPathUrl.  # noqa: E501
        :rtype: str
        """
        return self._attachment_path

    @attachment_path.setter
    def attachment_path(self, attachment_path):
        """Sets the attachment_path of this AttachmentPathUrl.

        Attachment path.  # noqa: E501

        :param attachment_path: The attachment_path of this AttachmentPathUrl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attachment_path is None:  # noqa: E501
            raise ValueError("Invalid value for `attachment_path`, must not be `None`")  # noqa: E501

        self._attachment_path = attachment_path

    @property
    def upload_url(self):
        """Gets the upload_url of this AttachmentPathUrl.  # noqa: E501

        Signed URL to upload blob content to.  # noqa: E501

        :return: The upload_url of this AttachmentPathUrl.  # noqa: E501
        :rtype: object
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this AttachmentPathUrl.

        Signed URL to upload blob content to.  # noqa: E501

        :param upload_url: The upload_url of this AttachmentPathUrl.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and upload_url is None:  # noqa: E501
            raise ValueError("Invalid value for `upload_url`, must not be `None`")  # noqa: E501

        self._upload_url = upload_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, AttachmentPathUrl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentPathUrl):
            return True

        return self.to_dict() != other.to_dict()
