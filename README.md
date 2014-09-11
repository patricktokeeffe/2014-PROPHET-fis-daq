Fast Isoprene Sensor Data Acquisition
=====================================

Biogenic VOCs and Secondary Organic Aerosol at PROPHET - WSU 2014
-----------------------------------------------------------------

This main repository hosts the data acquisition system deployed to monitor the 
Fast Isoprene Sensor (FIS) at the UMBS PROPHET tower lab during summer 2014.
There are three major components:

- **Datalogger program** :: A Campbell Scientific datalogger is used to monitor
  and control sensors, provide preliminary data reduction and provide 
  supervisory functions. The program and its changelog are in the `crbasic`
  folder.

- **Documentation** :: Within the `doc` folder are the wiring diagram for the
  datalogger and a user manual. The manual covers installation procedures,
  setup of the datalogger program, operating and maintenance procedures, data
  products, and additional information for developers. The manual *does not*
  cover operation of the FIS itself, nor any of its components -- refer to the
  FIS user manual for such information.

- **Processing scripts** :: Scripts and programs written for use with this 
  system are in the `processing` folder. Refer to the user manual for details
  on software requirements and useful tips for processing routines.

A second private repository hosts sensitive information such as network 
addresses and access credentials specific to the 2014 measurement campaign.

- Main repository (public): https://bitbucket.org/wsular/2014-prophet-fis-daq
- Private repository: https://bitbucket.org/wsular/2014-prophet-fis-secrets
- Data host (read-only): ftp://lar-d216-share.cee.wsu.edu/proj/2014_PROPHET
  [port 1021 off WSU campus]

### Building from source

The user manual is a `.lyx` file and requires [Lyx](http://www.lyx.org) version 
2.1+ to be compiled to a readable PDF file. Alternatively, grab a pre-compiled
user manual from this repository's website. 

The datalogger program can be pre-compiled to check for errors but it does not
need to be pre-built to deploy to a datalogger.

Processing scripts are written in Python and therefore do not require compilation.

### License 

This work is licensed under [The MIT License](http://opensource.org/licenses/mit-license.html).

### Disclaimer

This work is not affiliated with or endorsed by Campbell Scientific Inc., the
maker of the datalogger or Hill Scientific, the maker of the FIS.
