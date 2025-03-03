from setuptools import setup,find_packages

install_requires = [
    'aiohttp==3.11.13',
    'aiosignal==1.3.2',
    'annotated-types==0.7.0',
    'anyio==4.8.0',
    'asttokens==3.0.0',
    'attrs==25.1.0',
    'backcall==0.2.0',
    'beautifulsoup4==4.13.3',
    'bleach==6.2.0',
    'blinker==1.9.0',
    'certifi==2025.1.31',
    'charset-normalizer==3.4.1',
    'click==8.1.8',
    'dataclasses-json==0.6.7',
    'decorator==5.2.1',
    'defusedxml==0.7.1',
    'distro==1.9.0',
    'docopt==0.6.2',
    'dotenv==0.9.9',
    'executing==2.2.0',
    'fastjsonschema==2.21.1',
    'filelock==3.17.0',
    'Flask==3.1.0',
    'frozenlist==1.5.0',
    'fsspec==2025.2.0',
    'greenlet==3.1.1',
    'h11==0.14.0',
    'httpcore==1.0.7',
    'httpx==0.28.1',
    'httpx-sse==0.4.0',
    'huggingface-hub==0.29.1',
    'idna==3.10',
    'ipython==8.12.3',
    'itsdangerous==2.2.0',
    'jedi==0.19.2',
    'Jinja2==3.1.5',
    'jiter==0.8.2',
    'jsonpatch==1.33',
    'jsonpointer==3.0.0',
    'jsonschema==4.23.0',
    'jsonschema-specifications==2024.10.1',
    'jupyter_client==8.6.3',
    'jupyter_core==5.7.2',
    'jupyterlab_pygments==0.3.0',
    'kafka-python==2.0.5',
    'langchain==0.3.19',
    'langchain-community==0.3.18',
    'langchain-core==0.3.40',
    'langchain-mistralai==0.2.7',
    'langchain-openai==0.3.7',
    'langchain-text-splitters==0.3.6',
    'langsmith==0.3.11',
    'MarkupSafe==3.0.2',
    'marshmallow==3.26.1',
    'matplotlib-inline==0.1.7',
    'mistune==3.1.2',
    'multidict==6.1.0',
    'mypy-extensions==1.0.0',
    'nbclient==0.10.2',
    'nbconvert==7.16.6',
    'nbformat==5.10.4',
    'numpy==1.26.4',
    'openai==1.65.2',
    'orjson==3.10.15',
    'packaging==24.2',
    'pandocfilters==1.5.1',
    'parso==0.8.4',
    'pickleshare==0.7.5',
    'pipreqs==0.5.0',
    'platformdirs==4.3.6',
    'prompt_toolkit==3.0.50',
    'propcache==0.3.0',
    'pure_eval==0.2.3',
    'pydantic==2.10.6',
    'pydantic-settings==2.8.1',
    'pydantic_core==2.27.2',
    'Pygments==2.19.1',
    'python-dateutil==2.9.0.post0',
    'python-dotenv==1.0.1',
    'pywin32==308',
    'PyYAML==6.0.2',
    'pyzmq==26.2.1',
    'referencing==0.36.2',
    'regex==2024.11.6',
    'requests==2.32.3',
    'requests-toolbelt==1.0.0',
    'rpds-py==0.23.1',
    'six==1.17.0',
    'sniffio==1.3.1',
    'soupsieve==2.6',
    'SQLAlchemy==2.0.38',
    'stack-data==0.6.3',
    'tenacity==9.0.0',
    'tiktoken==0.9.0',
    'tinycss2==1.4.0',
    'tokenizers==0.21.0',
    'tornado==6.4.2',
    'tqdm==4.67.1',
    'traitlets==5.14.3',
    'typing-inspect==0.9.0',
    'typing_extensions==4.12.2',
    'urllib3==2.3.0',
    'wcwidth==0.2.13',
    'webencodings==0.5.1',
    'Werkzeug==3.1.3',
    'yarg==0.1.9',
    'yarl==1.18.3'
]

setup(
    name='ds-service',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    include_package_data=True,
)