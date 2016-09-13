# Backend Endpoints (for mobile)

Base Url: tams-142602.appspot.com/

---

# Asset Management

For most up to date definitions, view comments in the source: https://github.com/ScribblesProject/Backend/blob/master/api/views/assets.py

## List

- Endpoint:       /api/asset/list/
- HTTP method:    GET
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body:   `<none>`
- Response:

```
{
    "assets": [{
        'id':              Integer64 (e.g 5206187557519360)
        'name':            String
        'description':     String
        'category':        String
        'asset-type':      String
        'media-image-url': String
        'media-voice-url': String
        'locations': {
            '0': {
                'latitude':             Double
                'longitude':            Double
            }
            '1': ...
        }
    }, ...]
}
```

## Fetch

- Endpoint:       /api/asset/`<asset_id>`/
- HTTP method:    GET
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body:   `<none>`
- Response:

```
{
    'id':                  Integer64 (e.g 5206187557519360)
    'name':                String
    'description':         String
    'category':            String
    'asset-type':          String
    'media-image-url':     String
    'media-voice-url':     String
    'locations': {         # Key is the order of the locations
        '0': {
            'latitude':             Double
            'longitude':            Double
        }
        '1': ...
    }
}
```

## Update

- Endpoint:       /api/asset/update/`<asset_id>`/
- HTTP method:    PUT
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body: **NOTE: all fields must be present**

```
{
    'name':                 String
    'description':          String
    'category-name':        String  # If category doesnt exist, it will be created
    'category-description': String
    'type-name':            string  # If type doesnt exist, it will be created
    'locations': {          # Key is the order of the locations
        '0': {                      
            'latitude':             Double
            'longitude':            Double
        }
        '1': ...
    }
}
```

- Response:

```
{
    'success': Boolean
}
```

## Delete

- Endpoint:       /api/asset/delete/`<asset_id>`/
- HTTP method:    DELETE
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body:   `<none>`
- Response:

```
{
    'success': Boolean
}
```

## Create

- Endpoint:       /api/asset/create/
- HTTP method:    POST
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body: **NOTE: all fields must be present**

```
{
    'name':                 String
    'description':          String
    'category':             String  # If category doesnt exist, it will be created
    'category-description': String
    'type-name':            string  # If type doesnt exist, it will be created
    'locations': {          # Key is the order of the locations.
        '0': {
            'latitude':             Double
            'longitude':            Double
        }
        '1': ...
    }
}
```

- Response:

```
{
    'id':        Integer64 (e.g 5206187557519360)
    'success':   Boolean
}
```

---

# Asset-Category Management

- Endpoint:       /api/asset/category/list/
- HTTP method:    GET
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body:   `<none>`
- Response:

```
{
    "categories": [{
        'id':              Integer64 (e.g 5206187557519360)
        'name':            String
        'description':     String
    }, ...]
}
```

# Asset-Type Management

- Endpoint:       /api/asset/type/list/
- HTTP method:    GET
- HTTP headers:   `<none>`
- Query string:   `<none>`
- Request body:   `<none>`
- Response:

```
{
    "types": [{
        'id':              Integer64 (e.g 5206187557519360)
        'name':            String
    }, ...]
}
```

---

# Asset Media Management

## Create Image

- Endpoint:       /api/asset/media/image-upload/`<asset_id>`/
- HTTP method:    POST
- HTTP headers:   

```
[
    'content-type' : "image/jpeg"   # change this to a valid meme type 
    'content-size' : 123456         # size of the data contained in request body
]
```

- Query string:   `<none>`
- Request body:   `raw image data`
- Response:

```
{
    "status": true
}
```

## Create Voice Memo

- Endpoint:       /api/asset/media/voice-upload/`<asset_id>`/
- HTTP method:    POST
- HTTP headers:   

```
[
    'content-type' : "audio/aac"    # change this to a valid meme type 
    'content-size' : 123456         # size of the data contained in request body
]
```

- Query string:   `<none>`
- Request body:   `raw voice data`
- Response:

```
{
    "status": true
}
```
