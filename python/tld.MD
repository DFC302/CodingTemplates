```
#!/usr/bin/env python3

from tld import get_tld


def break_down_url(url):
    url = get_tld(url, as_object=True)
    _tld = url.tld
    subdomain = url.subdomain
    domain = url.domain
    fld = url.fld

    return <>

```
