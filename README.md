# Graphene-Django Decimal Example

Minimal sample project that demonstrates [#1276](https://github.com/graphql-python/graphene-django/issues/1276).

Installation:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Generating the GraphQL schema:

    python manage.py graphql_schema --out schema.graphql
