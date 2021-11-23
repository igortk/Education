#!/bin/bash

if [ "$(date +\%u)" == "0" ] || [ "$(date +\%u)" == "7" ] && [ "$(date '+\%:z') == '+0300'" ] then
   timedatectl set-timezone Europe/Kiev
fi