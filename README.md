# Pentest-chainsaw
![screen_1](https://i.imgur.com/YrUNZIv.png)

Status: <b>Development</b>
# About Pentest-chainsaw project
A bunch of tiny scripts for a lazy pentester ,trying to automize some tasks ,getting easy access to the needed information ,repeat the same process .
# What about ''Routerdb'' script !?
Accessing devices using the default credentials is a daily habit for pentester .Routerdb is a python script based on routerpassword website that gather the default username/password for different routers products .
You don't need to leave your terminal anymore .

* <b>329</b> Router supported
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

## How to run :
Get the router default password 
``` -r option ```
![Cisco router](https://i.imgur.com/lDsg1Sh.png)


another router

![ZTE router](https://i.imgur.com/VtV3uw1.png)

``` -r ```  option is used to list the available routers products .

329 router available .


![ZTE router](https://i.imgur.com/4RFFYsx.png)

## How to install
```sh
git clone https://github.com/ihebski/Pentest-chainsaw.git
cd Pentest-chainsaw/
pip install -r requirements.txt
python routerdb.py -r <router>
```
## Contribute with us 

```
    [+] AUTOR:        Iheb Ben Salem (ihebski)
    [+] EMAIL:        ihebbensalem.dev@gmail.com
    [+] GITHUB:       https://github.com/ihebski
```
## License
The MIT License (MIT)
