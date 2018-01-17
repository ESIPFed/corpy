# coding: utf-8

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `https://mmisw.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `https://mmisw.org/ont`. 

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PostTerm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'voc_iri': 'str',
        'version': 'str',
        'class_iri': 'str',
        'term_name': 'str',
        'term_iri': 'str',
        'attributes': 'list[list[str]]'
    }

    attribute_map = {
        'voc_iri': 'vocIri',
        'version': 'version',
        'class_iri': 'classIri',
        'term_name': 'termName',
        'term_iri': 'termIri',
        'attributes': 'attributes'
    }

    def __init__(self, voc_iri=None, version=None, class_iri=None, term_name=None, term_iri=None, attributes=None):
        """
        PostTerm - a model defined in Swagger
        """

        self._voc_iri = None
        self._version = None
        self._class_iri = None
        self._term_name = None
        self._term_iri = None
        self._attributes = None

        if voc_iri is not None:
          self.voc_iri = voc_iri
        if version is not None:
          self.version = version
        if class_iri is not None:
          self.class_iri = class_iri
        if term_name is not None:
          self.term_name = term_name
        if term_iri is not None:
          self.term_iri = term_iri
        if attributes is not None:
          self.attributes = attributes

    @property
    def voc_iri(self):
        """
        Gets the voc_iri of this PostTerm.
        The IRI of the affected ORR vocabulary. 

        :return: The voc_iri of this PostTerm.
        :rtype: str
        """
        return self._voc_iri

    @voc_iri.setter
    def voc_iri(self, voc_iri):
        """
        Sets the voc_iri of this PostTerm.
        The IRI of the affected ORR vocabulary. 

        :param voc_iri: The voc_iri of this PostTerm.
        :type: str
        """

        self._voc_iri = voc_iri

    @property
    def version(self):
        """
        Gets the version of this PostTerm.
        The version to be affected. By default, latest version. 

        :return: The version of this PostTerm.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PostTerm.
        The version to be affected. By default, latest version. 

        :param version: The version of this PostTerm.
        :type: str
        """

        self._version = version

    @property
    def class_iri(self):
        """
        Gets the class_iri of this PostTerm.
        IRI of the specific class to be affected within the vocabulary. Can be ommitted if the vocabulary only contains one class (which will be the one affected). 

        :return: The class_iri of this PostTerm.
        :rtype: str
        """
        return self._class_iri

    @class_iri.setter
    def class_iri(self, class_iri):
        """
        Sets the class_iri of this PostTerm.
        IRI of the specific class to be affected within the vocabulary. Can be ommitted if the vocabulary only contains one class (which will be the one affected). 

        :param class_iri: The class_iri of this PostTerm.
        :type: str
        """

        self._class_iri = class_iri

    @property
    def term_name(self):
        """
        Gets the term_name of this PostTerm.
        Simple name of the new term. 

        :return: The term_name of this PostTerm.
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """
        Sets the term_name of this PostTerm.
        Simple name of the new term. 

        :param term_name: The term_name of this PostTerm.
        :type: str
        """

        self._term_name = term_name

    @property
    def term_iri(self):
        """
        Gets the term_iri of this PostTerm.
        Full IRI of the new term. 

        :return: The term_iri of this PostTerm.
        :rtype: str
        """
        return self._term_iri

    @term_iri.setter
    def term_iri(self, term_iri):
        """
        Sets the term_iri of this PostTerm.
        Full IRI of the new term. 

        :param term_iri: The term_iri of this PostTerm.
        :type: str
        """

        self._term_iri = term_iri

    @property
    def attributes(self):
        """
        Gets the attributes of this PostTerm.
        Values for the properties defined for the vocabulary class. 

        :return: The attributes of this PostTerm.
        :rtype: list[list[str]]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this PostTerm.
        Values for the properties defined for the vocabulary class. 

        :param attributes: The attributes of this PostTerm.
        :type: list[list[str]]
        """

        self._attributes = attributes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PostTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other