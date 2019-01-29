# coding: utf-8

"""
    ORR Ont API Documentation

    The main ORR documentation is located at: http://mmisw.org/orrdoc/ ``` ###################################################### # NOTE #   OUT-OF-DATE for the time being. # Currently the swagger spec is maintained in the # https://github.com/mmisw/mmiorr-docs repo, which # is served at http://mmisw.org/orrdoc/api/ ###################################################### ``` __Note__: - We are in the process of writing this API documentation.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page also allows to directly exercise the API. - Actual requests from this page are against the endpoint at   `http://cor.esipfed.org/sparql`. This may change in a future version in   particular regarding a more general way of exercising the API (regardless   of concrete endpoint), or by allowing the selection of the particular endpoint.  - You can use the \"Authorize\" button above and enter your COR credentials to login   in this API interface. In this way you will be able to perform not only the basic   `GET` operations, but see expanded responses according to your access priviliges   and ontology visibility settings, as well as perform other operations as listed below.   # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PostOnt(object):
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
        'uri': 'str',
        'original_uri': 'str',
        'name': 'str',
        'org_name': 'str',
        'visibility': 'str',
        'status': 'str',
        'user_name': 'str',
        'uploaded_filename': 'str',
        'uploaded_format': 'str',
        'contents': 'str',
        'format': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'original_uri': 'originalUri',
        'name': 'name',
        'org_name': 'orgName',
        'visibility': 'visibility',
        'status': 'status',
        'user_name': 'userName',
        'uploaded_filename': 'uploadedFilename',
        'uploaded_format': 'uploadedFormat',
        'contents': 'contents',
        'format': 'format'
    }

    def __init__(self, uri=None, original_uri=None, name=None, org_name=None, visibility=None, status=None, user_name=None, uploaded_filename=None, uploaded_format=None, contents=None, format=None):  # noqa: E501
        """PostOnt - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._original_uri = None
        self._name = None
        self._org_name = None
        self._visibility = None
        self._status = None
        self._user_name = None
        self._uploaded_filename = None
        self._uploaded_format = None
        self._contents = None
        self._format = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if original_uri is not None:
            self.original_uri = original_uri
        if name is not None:
            self.name = name
        if org_name is not None:
            self.org_name = org_name
        if visibility is not None:
            self.visibility = visibility
        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if uploaded_filename is not None:
            self.uploaded_filename = uploaded_filename
        if uploaded_format is not None:
            self.uploaded_format = uploaded_format
        if contents is not None:
            self.contents = contents
        if format is not None:
            self.format = format

    @property
    def uri(self):
        """Gets the uri of this PostOnt.  # noqa: E501

        The URI of the ontology.   # noqa: E501

        :return: The uri of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this PostOnt.

        The URI of the ontology.   # noqa: E501

        :param uri: The uri of this PostOnt.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def original_uri(self):
        """Gets the original_uri of this PostOnt.  # noqa: E501

        In case of a fully-hosted registration, enter this field to indicate the original URI in the provided contents to be used for the \"migration\" of corresponding entities to the new URI.   # noqa: E501

        :return: The original_uri of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._original_uri

    @original_uri.setter
    def original_uri(self, original_uri):
        """Sets the original_uri of this PostOnt.

        In case of a fully-hosted registration, enter this field to indicate the original URI in the provided contents to be used for the \"migration\" of corresponding entities to the new URI.   # noqa: E501

        :param original_uri: The original_uri of this PostOnt.  # noqa: E501
        :type: str
        """

        self._original_uri = original_uri

    @property
    def name(self):
        """Gets the name of this PostOnt.  # noqa: E501

        The name for the ontology. If omitted, the ORR will try to get this information from standard metadata in the submitted ontology contents.   # noqa: E501

        :return: The name of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostOnt.

        The name for the ontology. If omitted, the ORR will try to get this information from standard metadata in the submitted ontology contents.   # noqa: E501

        :param name: The name of this PostOnt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_name(self):
        """Gets the org_name of this PostOnt.  # noqa: E501

        ID of the organization that will own the ontology registration. If omitted, the owner will be the submitting user.   # noqa: E501

        :return: The org_name of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this PostOnt.

        ID of the organization that will own the ontology registration. If omitted, the owner will be the submitting user.   # noqa: E501

        :param org_name: The org_name of this PostOnt.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def visibility(self):
        """Gets the visibility of this PostOnt.  # noqa: E501

        One of: `owner` or `public`. The default visibility is `owner`.   # noqa: E501

        :return: The visibility of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this PostOnt.

        One of: `owner` or `public`. The default visibility is `owner`.   # noqa: E501

        :param visibility: The visibility of this PostOnt.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def status(self):
        """Gets the status of this PostOnt.  # noqa: E501

        One of: `draft`, `unstable`, `testing`, `stable`,  `deprecated`, `archaic`. There's no default value.   # noqa: E501

        :return: The status of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostOnt.

        One of: `draft`, `unstable`, `testing`, `stable`,  `deprecated`, `archaic`. There's no default value.   # noqa: E501

        :param status: The status of this PostOnt.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_name(self):
        """Gets the user_name of this PostOnt.  # noqa: E501

        Registered user making the request.   # noqa: E501

        :return: The user_name of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this PostOnt.

        Registered user making the request.   # noqa: E501

        :param user_name: The user_name of this PostOnt.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def uploaded_filename(self):
        """Gets the uploaded_filename of this PostOnt.  # noqa: E501

        Name of file previously uploaded via prior `POST /ont/upload` request.   # noqa: E501

        :return: The uploaded_filename of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_filename

    @uploaded_filename.setter
    def uploaded_filename(self, uploaded_filename):
        """Sets the uploaded_filename of this PostOnt.

        Name of file previously uploaded via prior `POST /ont/upload` request.   # noqa: E501

        :param uploaded_filename: The uploaded_filename of this PostOnt.  # noqa: E501
        :type: str
        """

        self._uploaded_filename = uploaded_filename

    @property
    def uploaded_format(self):
        """Gets the uploaded_format of this PostOnt.  # noqa: E501

        Format of the file previously uploaded via prior `POST /ont/upload` request.   # noqa: E501

        :return: The uploaded_format of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_format

    @uploaded_format.setter
    def uploaded_format(self, uploaded_format):
        """Sets the uploaded_format of this PostOnt.

        Format of the file previously uploaded via prior `POST /ont/upload` request.   # noqa: E501

        :param uploaded_format: The uploaded_format of this PostOnt.  # noqa: E501
        :type: str
        """

        self._uploaded_format = uploaded_format

    @property
    def contents(self):
        """Gets the contents of this PostOnt.  # noqa: E501

        Direct contents of the ontology.   # noqa: E501

        :return: The contents of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this PostOnt.

        Direct contents of the ontology.   # noqa: E501

        :param contents: The contents of this PostOnt.  # noqa: E501
        :type: str
        """

        self._contents = contents

    @property
    def format(self):
        """Gets the format of this PostOnt.  # noqa: E501

        Format of the `contents`.   # noqa: E501

        :return: The format of this PostOnt.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PostOnt.

        Format of the `contents`.   # noqa: E501

        :param format: The format of this PostOnt.  # noqa: E501
        :type: str
        """

        self._format = format

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
        if issubclass(PostOnt, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostOnt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
