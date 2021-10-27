#!/bin/bash

echo "Number of max attribute rolls: "
ls images | grep -v _ | wc | awk '{print $1}'

echo "Number of single attribute rolls: "
ls images/*.?*_*_*_*_* | wc | awk '{print $1}'

echo "Number of zero attribute rolls: "
ls images/*.?_____.* | wc | awk '{print $1}'

echo "DiamondNecklaces: "
ls images/*.?1*

echo "DiamondVipers: "
ls images/*.?????n.*

echo "Crowns: "
ls images/*.*H?.*

echo "Aliens: "
ls images/*.a*

echo "Devils: "
ls images/*.v*

echo "Matching Goku or Saiyan: "
ls images/*.?J??W?.*
ls images/*.?J??f?.*
