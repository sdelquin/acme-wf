# acme-wf

Project to facilitate the renovation process of **SSL certificates** for hosted domains in [Webfaction](https://webfaction.com).

## Requirements

1. [acme-webfaction](https://github.com/gregplaysguitar/acme-webfaction).
2. Python 3.7
2. Pipfile

## `redirect`

In order to validate the *ACME challenge* it is needed to have a **redirect** app & website.

### App

- [Link to configuration](https://my.webfaction.com/applications).
- *Static/CGI/PHP*.

Content of `.htaccess`:

~~~nginx
RewriteEngine On

RewriteCond %{HTTPS} off
RewriteCond %{REQUEST_URI} !\.well-known/acme-challenge
RewriteCond %{HTTP_HOST} ^(?:www\.)?(.*)$ [NC]
RewriteRule (.*) https://%1%{REQUEST_URI} [L,R=301]
~~~

> Redirects whichever *http* request to *https*, **EXCEPT** the request for validation of ACME challenge (`.well-known/acme-challenge`)

### Website

- [Link to configuration](https://my.webfaction.com/websites).
- Only HTTP requests.
- Include into *Domains* all the domains you want to validate. Domains must be in the form `http://...`

## Assumptions

The corresponding SSL certificates are already loaded in the [SSL certificates section of Webfaction](https://my.webfaction.com/ssl-certificates).

## Usage

Set the proper values on file `.env`. Take into account that `DOMAINS` should be a string in the form:

`'<domain>|<cert_name>, <domain>|<cert_name>, ...'`

~~~console
$ pipenv install
$ python main.py
~~~
