# Release notes

## 2.0.0 (2026-05-25)

- release: remove the `v` prefix in version names
- feat: add a live reload flag to update spec on every request (:pr:`10`)
- feat: use pre-commit to run linters (:pr:`13`)
- build: extract the lib version dynamically (``__version__`` and ``pkg_resources`` removed)
- build: migrate to pyproject.toml (:pr:`14`)
- chore: add support for Python 3.10, 3.11, 3.12, 3.13, 3.14 (:pr:`11`)
- chore: drop support for Python 3.6, 3.7, 3.8, 3.9 (:pr:`11`)
- ci: add a workflow to build and release (:pr:`17`)

## 1.0.3 (2021-06-24)

* build: specify the apispec min version
* ci: run tests on GitHub Actions
* fix(readme): add the endpoint `/hello` to the sample code
* test(readme): add a test for the code in the README


## 1.0.2 (2021-02-24)

* Fix(doc): use the right Markdown syntax for links
* Fix(doc): use the right PyPI link
* Fix(setup): remove a typo from entry author.


## 1.0.1 (2020-12-23)

Fix: remove a not supported classifier.


## 1.0.0 (2020-12-23)

First release.
