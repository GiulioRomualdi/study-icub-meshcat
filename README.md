# study-icub-meshcat

This repository contains a python script to spawn an `icub-model` in the meshcat environment.

## :runner: How to run the script

1. Open a terminal and create a conda enviroment
   ```shell
   conda create -n icub-meshcat
   conda activate icub-meshcat
   ```

2. Once the environment is created please install pinocchio and meshcat
   ```shell
   conda install -c conda-forge pinocchio meshcat-python
   ```

3. Now your environment is ready and you can clone this repository
   ```shell
   git clone --recurse-submodules https://github.com/GiulioRomualdi/study-icub-meshcat.git
   ```

4. You can finally run the script
   ```shell
   python visualize-icub.py -h
   ```
