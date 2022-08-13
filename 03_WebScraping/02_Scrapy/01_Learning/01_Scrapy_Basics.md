Scrapy Development Environment Setup

Step 1: Check if conda is installed in your path.

- Open up the anaconda command prompt
- Type `conda -V` and press enter.
- If the conda is successfully installed in your system you should see a similar output:

[screenshot of my evn]

Step 2: Update the conda environment

- Type `conda update conda` and press enter.
- you should see a similar output as follows:

Step-3: Check available Python version available to setup the virtual environment

- Type `conda search “^python$”` and press enter to view all the available Python versions
- You should be able to see a similar output:

Step-4: Creating a virtual environment

- Type `conda create -n scrapy-workspace python=3.9 anaconda` to create an virtual environment named _scrapy-workspace_ with _Python 3.9_ version
- You can change the virtual environment name and python version as per your requirement
- If executed successfully, you should be able to see a similar output:

Step 5: Activating the virtual environment

- Type `conda activate scrapy-workspace` to activate the virtual environment named _scrapy-workspace_
- You should type your virtual environment name instead of _scrapy-workspace_
- If executed successfully, you should be able to see a similar output:

Step 6: Installing Packages to work with Scrapy

The packages that we should install to easily work with Scrapy are:

- scrapy
- pylint
- autopep8

To install latest version of scrapy: `pip install scrapy`
for anaconda: `conda install -c conda-forge scrapy`

`pip install scrapy`
`pip install pylint`
`pip install autopep8`

if you are planning to rotate user-agents:

`pip install scrapy-user-agents`

also add the following to `settings.py` file:

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
```

if you are planning to rotate IPs:

`pip install scrapy-proxy-pool`

also add the following to `settings.py` file:

```python
PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
```
