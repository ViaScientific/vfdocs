# API v1

Dmeta API uses
`REST (Representational State Transfer)`{.interpreted-text role="abbr"}.
JSON is returned by all API responses including errors and HTTP response
status codes are to designate success and failure.

::: {.contents local="" backlinks="none" depth="3"}
Table of contents
:::

## Authentication and authorization

Requests to the Dmeta API are for public and private information. All
endpoints require authentication.

### User Login

After getting the access token, users can make a request to the Dmeta
API with the `Authorization` HTTP header. It can be specified with
`Bearer <your-access-token>` to authenticate as a user and have the same
permissions that the user itself.

> Retrieve an access token for the current logged in user.
>
> **Example request**:
>
> ``` bash
> $ curl -X POST 'https://dmeta-skin.dolphinnext.com/api/v1/users/login' \
> -H 'Content-Type: application/json' \
> -d '
>     {
>         "email":"your-email@mail.com",
>         "password":"your-password"
>     }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "token": "eyJhbGciOiJSUz....",
>     "data": {
>         "user": {
>             "role": "user",
>             "_id": "b6c9a200168a225f39add38d",
>             "email": "your-email@mail.com",
>             "name": "test user",
>             "scope": "*",
>             "username": "yukseleo"
>         }
>     }
> }
> ```

## Projects

### Get All Projects

> Retrieve a list of all the projects for the current logged in user.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET 'https://dmeta-skin.dolphinnext.com/api/v1/projects' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "results": 1,
>     "data": {
>         "data": [
>             {
>                 "active": true,
>                 "creationDate": "2020-11-17T19:36:49.048Z",
>                 "lastUpdateDate": "2020-11-17T19:36:49.048Z",
>                 "_id": "5fb2b395c8c1e577fcb8ce6c",
>                 "restrictTo": {
>                     "role": [
>                         "admin"
>                     ]
>                 },
>                 "name": "vitiligo",
>                 "label": "Vitiligo",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 },
>             }
>         ]
>     }
> }
> ```

### Get a Project

> Retrieve details of a single project.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET \
> 'https://dmeta-skin.dolphinnext.com/api/v1/projects/5fb2b395c8c1e577fcb8ce6c' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "results": 1,
>     "data": {
>         "data": [
>             {
>                 "active": true,
>                 "creationDate": "2020-11-17T19:36:49.048Z",
>                 "lastUpdateDate": "2020-11-17T19:36:49.048Z",
>                 "_id": "5fb2b395c8c1e577fcb8ce6c",
>                 "restrictTo": {
>                     "role": [
>                         "admin"
>                     ]
>                 },
>                 "name": "vitiligo",
>                 "label": "Vitiligo",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 },
>             }
>         ]
>     }
> }
> ```

### Create a Project

> This post request is only allowed for the admin role.
>
> **Example request**:
>
> ``` bash
> $ curl -X POST \
> 'https://dmeta-skin.dolphinnext.com/api/v1/projects' \
> -H 'Authorization: Bearer <your-access-token>' \
> -H 'Content-Type: application/json' \
> -d '
>     {
>         "name": "vitiligo",
>         "label": "Vitiligo"
>     }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "active": true,
>             "creationDate": "2021-03-31T02:04:27.474Z",
>             "lastUpdateDate": "2021-03-31T02:04:27.474Z",
>             "_id": "6063dbcfa50bb5fa9eb9cfba",
>             "name": "vitiligo",
>             "label": "Vitiligo",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22"
>         }
>     }
> }
> ```

### Update a Project

> Update an existing project.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X PATCH \
>   -H "Authorization: Bearer <token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/projects/5fb2b395c8c1e577fcb8ce6c \
>   -H "Content-Type: application/json" \
>   -d '
>       {
>         "label": "Vitiligo"
>       }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "active": true,
>             "creationDate": "2020-11-17T19:36:49.048Z",
>             "lastUpdateDate": "2020-11-17T19:36:49.048Z",
>             "_id": "5fb2b395c8c1e577fcb8ce6c",
>             "restrictTo": {
>                 "role": [
>                     "admin"
>                 ]
>             },
>             "name": "vitiligo",
>             "label": "Vitiligo",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             }
>         }
>     }
> }
> ```

### Delete a Project

> Deleting an existing project.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X DELETE \
>   -H "Authorization: Bearer <token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/projects/5fb2b395c8c1e577fcb8ce6c 
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "doc": "Deleted!"
>     }
> }
> ```

## Collections

### Get All Collections

> Retrieve a list of all the collections for the current logged in user.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET 'https://dmeta-skin.dolphinnext.com/api/v1/collections' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {"status": "success",
>     "results": 10,
>     "data": {
>         "data": [
>             {
>                 "version": 1,
>                 "required": false,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.301Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.301Z",
>                 "_id": "5f57ffba35db5980ba020ff3",
>                 "restrictTo": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 },
>                 "name": "exp_series",
>                 "label": "Experiment Series",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "projectID": "5fb2b395c8c1e577fcb8ce6c",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 },
>                 "id": "5f57ffba35db5980ba020ff3"
>             },
>             {
>                 "version": 1,
>                 "required": false,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.301Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.301Z",
>                 "_id": "5f57ffe635db5980ba020ff4",
>                 "restrictTo": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 },
>                 "name": "exp",
>                 "label": "Experiments",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "projectID": "5fb2b395c8c1e577fcb8ce6c",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 },
>                 "id": "5f57ffe635db5980ba020ff4"
>             }]
>     }
> }
> ```

### Get a Collection

> Retrieve details of a single collection.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET \
> 'https://dmeta-skin.dolphinnext.com/api/v1/collections/5f57ffe635db5980ba020ff4' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": [
>             {
>                 "version": 1,
>                 "required": false,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.301Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.301Z",
>                 "_id": "5f57ffe635db5980ba020ff4",
>                 "restrictTo": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 },
>                 "name": "exp",
>                 "label": "Experiments",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "projectID": "5fb2b395c8c1e577fcb8ce6c",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 }
>             }
>         ]
>     }
> }
> ```

### Create a Collection

> This post request is only allowed for the project-admin role.
>
> **Example request**:
>
> ``` bash
> $ curl -X POST \
> 'https://dmeta-skin.dolphinnext.com/api/v1/collections' \
> -H 'Authorization: Bearer <your-access-token>' \
> -H 'Content-Type: application/json' \
> -d '
>     {
>         "name": "analysis",
>         "label": "Analysis",
>         "projectID":"5fb2b395c8c1e577fcb8ce6c",
>         "restrictTo": {"group":["5fb45793aa5adff6f407f2d2"]},
>     }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "version": 1,
>             "required": false,
>             "active": true,
>             "creationDate": "2021-03-31T02:26:17.087Z",
>             "lastUpdateDate": "2021-03-31T02:26:17.087Z",
>             "_id": "6063e3a33c195afbe6d5e036",
>             "name": "analysis",
>             "label": "Analysis",
>             "restrictTo": {
>                 "group": [
>                     "5fb45793aa5adff6f407f2d2"
>                 ]
>             },
>             "projectID": "5fb2b395c8c1e577fcb8ce6c",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             }
>         }
>     }
> }
> ```

### Update a Collection

> Update an existing collection.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X PATCH \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/collections/6063e3a33c195afbe6d5e036 \
>   -H "Content-Type: application/json" \
>   -d '
>       {
>         "label": "Analysis"
>       }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "version": 1,
>             "required": false,
>             "active": true,
>             "creationDate": "2021-03-31T02:26:17.087Z",
>             "lastUpdateDate": "2021-03-31T02:26:17.087Z",
>             "_id": "6063e3a33c195afbe6d5e036",
>             "name": "analysis",
>             "label": "Analysis",
>             "restrictTo": {
>                 "group": [
>                     "5fb45793aa5adff6f407f2d2"
>                 ]
>             },
>             "projectID": "5fb2b395c8c1e577fcb8ce6c",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             }
>         }
>     }
> }
> ```

### Delete a Collection

> Deleting an existing collection.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X DELETE \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/collections/6063e3a33c195afbe6d5e036 
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "doc": "Deleted!"
>     }
> }
> ```

## Fields

### Get All Fields

> Retrieve a list of fields for the current logged in user.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET 'https://dmeta-skin.dolphinnext.com/api/v1/fields' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "results": 2,
>     "data": {
>         "data": [
>             {
>                 "type": "String",
>                 "required": true,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.406Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.406Z",
>                 "_id": "5f58518835db5980ba020ff7",
>                 "name": "name",
>                 "label": "Name",
>                 "collectionID": "5f57ffba35db5980ba020ff3",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 },
>                 "unique": true
>             },
>             {
>                 "type": "String",
>                 "required": false,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.406Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.406Z",
>                 "_id": "5f58559f35db5980ba020ff8",
>                 "name": "design",
>                 "label": "Design",
>                 "collectionID": "5f57ffba35db5980ba020ff3",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 }
>             }]
>         }
>     }
> ```

### Get a Field

> Retrieve details of a single field.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET \
> 'https://dmeta-skin.dolphinnext.com/api/v1/fields/5f58559f35db5980ba020ff8' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": [
>             {
>                 "type": "String",
>                 "required": false,
>                 "active": true,
>                 "creationDate": "2020-09-08T21:56:35.406Z",
>                 "lastUpdateDate": "2020-09-08T21:56:35.406Z",
>                 "_id": "5f58559f35db5980ba020ff8",
>                 "name": "design",
>                 "label": "Design",
>                 "collectionID": "5f57ffba35db5980ba020ff3",
>                 "lastUpdatedUser": "5f39add38db6c9a200168a22",
>                 "owner": "5f39add38db6c9a200168a22",
>                 "perms": {
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     },
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     }
>                 }
>             }
>         ]
>     }
> }
> ```

### Create a Field

> This post request is only allowed for the project-admin role.
>
> **Example request**:
>
> ``` bash
> $ curl -X POST \
> 'https://dmeta-skin.dolphinnext.com/api/v1/fields' \
> -H 'Authorization: Bearer <your-access-token>' \
> -H 'Content-Type: application/json' \
> -d '
>     {
>         "name": "clin_pheno",
>         "label": "Clinical Phenotype",
>         "type": "String",
>         "collectionID":"5f74a0e05443973d2bfd870c"
>     }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "type": "String",
>             "required": false,
>             "active": true,
>             "creationDate": "2021-03-31T02:57:02.771Z",
>             "lastUpdateDate": "2021-03-31T02:57:02.771Z",
>             "_id": "6063e7c91bfc89fd1960ae5b",
>             "name": "clin_pheno",
>             "label": "Clinical Phenotype",
>             "collectionID": "5f74a0e05443973d2bfd870c",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             },
>             "id": "6063e7c91bfc89fd1960ae5b"
>         }
>     }
> }
> ```

### Update a Field

> Update an existing field.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X PATCH \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/fields/6063e7c91bfc89fd1960ae5b \
>   -H "Content-Type: application/json" \
>   -d '
>       {
>         "ontology": {
>             "create": true,
>             "include": [
>                 "Dermatomyositis",
>                 "GVHD",
>                 "Healthy Control",
>                 "Lupus",
>                 "Psoriasis",
>                 "Vitiligo"
>             ]
>         }
>       }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "type": "String",
>             "required": false,
>             "active": true,
>             "creationDate": "2021-03-31T02:57:02.771Z",
>             "lastUpdateDate": "2021-03-31T02:57:02.771Z",
>             "_id": "6063e7c91bfc89fd1960ae5b",
>             "name": "clin_pheno",
>             "label": "Clinical Phenotype",
>             "collectionID": "5f74a0e05443973d2bfd870c",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             },
>             "ontology": {
>                 "create": true,
>                 "include": [
>                     "Dermatomyositis",
>                     "GVHD",
>                     "Healthy Control",
>                     "Lupus",
>                     "Psoriasis",
>                     "Vitiligo"
>                     ]
>             }
>         }
>     }
> }
> ```

### Delete a Field

> Deleting an existing field.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X DELETE \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/fields/6063e7c91bfc89fd1960ae5b 
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "doc": "Deleted!"
>     }
> }
> ```

## Data

### Get All Data of the Collection in a Project

> Retrieve all data of the collection in a project for the current
> logged in user.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET 'https://dmeta-skin.dolphinnext.com/api/v1/projects/vitiligo/data/sample' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "results": 2,
>     "data": {
>         "data": [
>             {
>                 "creationDate": "2020-12-17T16:42:06.252Z",
>                 "lastUpdateDate": "2020-12-17T16:42:06.252Z",
>                 "_id": "5fdb8c6ad6330eb80d503fe2",
>                 "name": "CL067_L2_V1_Bst_sc_iD",
>                 "sample_type": "scRNAseq",
>                 "technology": "inDrop",
>                 "status": "Processed",
>                 "contract": "scRNAseq",
>                 "bead_occup": "65-70%",
>                 "biosamp_id": "5fdb8820d6330eb80d503a31",
>                 "lastUpdatedUser": "5f92529b89c7d0b3bf31ac27",
>                 "owner": "5f92529b89c7d0b3bf31ac27",
>                 "perms": {
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     },
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     }
>                 },
>                 "DID": 1
>             },
>             {
>                 "creationDate": "2020-12-17T16:42:06.252Z",
>                 "lastUpdateDate": "2020-12-17T16:42:06.252Z",
>                 "_id": "5fdb8c6ad6330eb80d503fe4",
>                 "name": "VB071_L1_V1_Bst_sc_iD",
>                 "sample_type": "scRNAseq",
>                 "technology": "inDrop",
>                 "status": "Processed",
>                 "contract": "scRNAseq",
>                 "bead_occup": "33/50 (~65%)",
>                 "biosamp_id": "5fdb8820d6330eb80d503a33",
>                 "lastUpdatedUser": "5f92529b89c7d0b3bf31ac27",
>                 "owner": "5f92529b89c7d0b3bf31ac27",
>                 "perms": {
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     },
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     }
>                 },
>                 "DID": 2
>             }]
>         }
>     }
> ```

### Get a Data

> Retrieve details of a single data.
>
> **Example request**:
>
> ``` bash
> $ curl -X GET \
> 'https://dmeta-skin.dolphinnext.com/api/v1/projects/vitiligo/data/sample/5fdb8c6ad6330eb80d503fe2' \
> -H 'Authorization: Bearer <your-access-token>'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": [
>                     {
>                 "creationDate": "2020-12-17T16:42:06.252Z",
>                 "lastUpdateDate": "2020-12-17T16:42:06.252Z",
>                 "_id": "5fdb8c6ad6330eb80d503fe2",
>                 "name": "CL067_L2_V1_Bst_sc_iD",
>                 "sample_type": "scRNAseq",
>                 "technology": "inDrop",
>                 "status": "Processed",
>                 "contract": "scRNAseq",
>                 "bead_occup": "65-70%",
>                 "biosamp_id": "5fdb8820d6330eb80d503a31",
>                 "lastUpdatedUser": "5f92529b89c7d0b3bf31ac27",
>                 "owner": "5f92529b89c7d0b3bf31ac27",
>                 "perms": {
>                     "write": {
>                         "group": [
>                             "5fb45793aa5adff6f407f2d2"
>                         ]
>                     },
>                     "read": {
>                         "group": [
>                             "5fb4575faa5adff6f407f2d1"
>                         ]
>                     }
>                 },
>                 "DID": 1
>             }
>         ]
>     }
> }
> ```

### Create a Data

> This post request is only allowed for the users that have the write
> permission.
>
> **Example request**:
>
> ``` bash
> $ curl -X POST \
> 'https://dmeta-skin.dolphinnext.com/api/v1/projects/vitiligo/data/sample' \
> -H 'Authorization: Bearer <your-access-token>' \
> -H 'Content-Type: application/json' \
> -d '
>     {
>         "name": "CL070_L2_V1_Bst_sc_iD",
>         "sample_type": "scRNAseq",
>         "technology": "inDrop",
>         "status": "Sequenced",
>         "contract": "scRNAseq",
>         "bead_occup": "65-70%",
>         "biosamp_id":"5fdb8820d6330eb80d503a31"
>     }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "creationDate": "2021-03-31T03:16:58.503Z",
>             "lastUpdateDate": "2021-03-31T03:16:58.503Z",
>             "_id": "606453c0cb44bcfdbb84c6a2",
>             "name": "CL070_L2_V1_Bst_sc_iD",
>             "sample_type": "scRNAseq",
>             "technology": "inDrop",
>             "status": "Sequenced",
>             "contract": "scRNAseq",
>             "bead_occup": "65-70%",
>             "biosamp_id": "5fdb8820d6330eb80d503a31",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             },
>             "DID": 135
>         }
>     }
> }
> ```

### Update a Data

> Update an existing field.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X PATCH \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/projects/vitiligo/data/sample/606453c0cb44bcfdbb84c6a2 \
>   -H "Content-Type: application/json" \
>   -d '
>       {
>         "status":"Processed"
>       }'
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "data": {
>             "creationDate": "2021-03-31T03:16:58.503Z",
>             "lastUpdateDate": "2021-03-31T03:16:58.503Z",
>             "_id": "606453c0cb44bcfdbb84c6a2",
>             "name": "CL070_L2_V1_Bst_sc_iD",
>             "sample_type": "scRNAseq",
>             "technology": "inDrop",
>             "status": "Processed",
>             "contract": "scRNAseq",
>             "bead_occup": "65-70%",
>             "biosamp_id": "5fdb8820d6330eb80d503a31",
>             "lastUpdatedUser": "5f39add38db6c9a200168a22",
>             "owner": "5f39add38db6c9a200168a22",
>             "perms": {
>                 "read": {
>                     "group": [
>                         "5fb4575faa5adff6f407f2d1"
>                     ]
>                 },
>                 "write": {
>                     "group": [
>                         "5fb45793aa5adff6f407f2d2"
>                     ]
>                 }
>             },
>             "DID": 135
>         }
>     }
> }
> ```

### Delete a Data

> Deleting an existing data.
>
> **Example request**:
>
> ``` bash
> $ curl \
>   -X DELETE \
>   -H "Authorization: Bearer <your-access-token>" \
>   https://dmeta-skin.dolphinnext.com/api/v1/projects/vitiligo/data/sample/606453c0cb44bcfdbb84c6a2 
> ```
>
> **Example response**:
>
> ``` json
> {
>     "status": "success",
>     "data": {
>         "doc": "Deleted!"
>     }
> }
> ```
