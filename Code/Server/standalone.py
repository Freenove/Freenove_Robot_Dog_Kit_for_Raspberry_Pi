#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Server import *

# To automatically start this server after boot, please do the following:
## edit dog.service and change the two paths to the correct code repository.
## Then copy the file:
# cp dog.service /etc/systemd/system/dog.service
#
# systemctl daemon-reload
## Test that it works:
# systemctl start dog
## Now run the client and connect to the server
## If everything works, enable the service on boot time:
# systemctl enable systemd-networkd-wait-online
# systemctl enable dog

if __name__ == '__main__':
  server=Server()
  server.turn_on_server()
  server.tcp_flag=True
  video=threading.Thread(target=server.transmission_video)
  video.start()
  instruction=threading.Thread(target=server.receive_instruction)
  instruction.start()
