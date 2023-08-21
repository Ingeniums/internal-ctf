#!/bin/bash

docker run -d -p 1234:1234 --privileged $(docker build -q .)
