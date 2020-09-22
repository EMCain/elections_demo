first do this to get the line endings right 

https://medium.com/@csmunuku/windows-and-linux-eol-sequence-configure-vs-code-and-git-37be98ef71df

do the stuff in the first answer, but specifying python3 for the last one
https://stackoverflow.com/questions/55422929/e-unable-to-locate-package-python-pip-on-ubuntu-18-04

```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
```

then do this, starting at "Install Docker Compose", but specify pip3

https://medium.com/@joaoh82/setting-up-docker-toolbox-for-windows-home-10-and-wsl-to-work-perfectly-2fd34ed41d51

```
 pip install --user docker-compose
```

got as far as setting the $PATH and now I need to do "Configure WSL to Connect to Docker for Windows"