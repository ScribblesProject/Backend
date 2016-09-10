# Backend Endpoints (for mobile)

Base Url: tams-142602.appspot.com/

---

# Asset Management

For most up to date definitions, view comments in the source: https://github.com/ScribblesProject/Backend/blob/master/api/views/assets.py

## List
Endpoint:       /api/asset/list/
HTTP method:    GET
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:   `<none>`
```
Response:
{
    "assets": [{
        'id':              Integer
        'name':            String
        'description':     String
        'category':        String
        'asset-type':      String
        'latitude':        Double
        'longitude':       Double
        'media-image-url': String
        'media-voice-url': String
    }, ...]
}
```

## Fetch
Endpoint:       /api/asset/`<asset_id>`/
HTTP method:    GET
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:   `<none>`
Response:
```
{
    'id':              Integer
    'name':            String
    'description':     String
    'category':        String
    'asset-type':      String
    'latitude':        Double
    'longitude':       Double
    'media-image-url': String
    'media-voice-url': String
}
```

## Update
Endpoint:       /api/asset/update/`<asset_id>`/
HTTP method:    PUT
HTTP headers:   `<none>`
Query string:   `<none>`
Request body: 
**NOTE: all fields must be present**
```
{
    'name':                 String
    'description':          String
    'category-name':        String  # If category doesnt exist, it will be created
    'category-description': String
    'type-name':            string  # If type doesnt exist, it will be created
    'latitude':             Double
    'longitude':            Double
}
```
Response:
```
{
    'success': Boolean
}
```

## Delete
Endpoint:       /api/asset/delete/`<asset_id>`/
HTTP method:    DELETE
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:   `<none>`
Response:
```
{
    'success': Boolean
}
```

## Create
Endpoint:       /api/asset/create/
HTTP method:    POST
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:
**NOTE: all fields must be present**
```
{
    'name':                 String
    'description':          String
    'category':             String  # If category doesnt exist, it will be created
    'category-description': String
    'type-name':            string  # If type doesnt exist, it will be created
    'latitude':             Double
    'longitude':            Double
}
```
Response:
```
{
    'id': Int
    'success': Boolean
}
```

---

# Asset-Category Management
Endpoint:       /api/asset/category/list/
HTTP method:    GET
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:   `<none>`
Response:
```
{
    "categories": [{
        'id':              Integer
        'name':            String
        'description':     String
    }, ...]
}
```

# Asset-Type Management
Endpoint:       /api/asset/type/list/
HTTP method:    GET
HTTP headers:   `<none>`
Query string:   `<none>`
Request body:   `<none>`
Response:
```
{
    "types": [{
        'id':              Integer
        'name':            String
    }, ...]
}
```

# Asset Media Management
endpoint: api/asset/media/image-upload/(?P<asset_id>[0-9A-Fa-f]*)/
endpoint: api/asset/media/voice-upload/(?P<asset_id>[0-9A-Fa-f]*)/
