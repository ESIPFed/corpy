# coding: utf-8

# flake8: noqa

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `http://cor.esipfed.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `http://cor.esipfed.org/ont`.   # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.ontology_api import OntologyApi
from swagger_client.api.organization_api import OrganizationApi
from swagger_client.api.term_api import TermApi
from swagger_client.api.triplestore_api import TriplestoreApi
from swagger_client.api.user_api import UserApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.ont import Ont
from swagger_client.models.org import Org
from swagger_client.models.org_new import OrgNew
from swagger_client.models.org_updated import OrgUpdated
from swagger_client.models.possible_ontology_info import PossibleOntologyInfo
from swagger_client.models.post_ont import PostOnt
from swagger_client.models.post_org import PostOrg
from swagger_client.models.post_term import PostTerm
from swagger_client.models.post_user import PostUser
from swagger_client.models.put_ont import PutOnt
from swagger_client.models.put_org import PutOrg
from swagger_client.models.put_user import PutUser
from swagger_client.models.uploaded_file_info import UploadedFileInfo
from swagger_client.models.user import User
