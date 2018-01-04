[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
Status: Development
# About Pentest-chainsaw project
A bunch of tiny scripts for a lazy pentester ,trying to automize some tasks ,getting easy access to the needed information ,repeat the same process .
# What about ''Routerdb'' script !?
Accessing devices using the default credentials is a daily habit for pentester .Routerdb is a python script based on routerpassword website that gather the default username/password for different routers products .
You don't need to leave your terminal anymore .
## Usage

~~~
$ python routerdb.py -h
[*] Get the Routers Default Passwords

Options:
  -h, --help            show this help message and exit
  -r ROUTER, --router=ROUTER
                        router name
  -l, --list            List of the routers

~~~



## How to install
```sh
git clone https://github.com/ihebski/Pentest-chainsaw.git
cd Pentest-chainsaw/
pip install -r requirements.txt
python routerdb.py -r <router>
```
## License
The MIT License (MIT)
