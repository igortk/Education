#!/bin/bash

let year="$(date +\%Y)"

if [ $(year % 4) -eq 0 ]
then
    echo '29 february' >> /home/test
fi