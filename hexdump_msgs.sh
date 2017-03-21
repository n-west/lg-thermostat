#!/bin/bash

for msgnum in {0..19}
do
    msgfile=captures/msg${msgnum}.hex
    echo msg number ${msgnum} is $(du -b $msgfile | cut -f1) B
    hexdump -x $msgfile
done

