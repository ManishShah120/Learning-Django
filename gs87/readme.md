# Template Fragment Caching

## Template Fragment Caching[Local Memory based Caching]

### More control what to cache
- {% load cache %} [Gives the access to cache tag in template]
- {% cache %} [Caches the contents of the block]
    Syntax:
        {% cache timeout name variable using="" %} ... {% endcache name %}
    Example
        {% cache 60 sidebar request.user.username using="localcache" %}
            ..sidebar for logged in user ...
        {% endcache %}

# Till Now we have seen [urls.py & viewws.py in both ways]:-

Per site Cache:
- Database Caching
- File System Caching
- Local Memory Caching

Per view Caching:
- Database Caching
- File System Caching
- Local Memory Caching

Template Fragment Caching
- Database Caching
- File System Caching
- Local Memory Caching
