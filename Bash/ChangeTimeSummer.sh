#!/bin/bash

if [ "$(date +\%u)" == "0" ] || [ "$(date +\%u)" == "7" ] && [ "$(date '+\%:z') == '+0200'" ] then
   timedatectl set-timezone Europe/Moscow
fi