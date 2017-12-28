# IPTV playlist parser

This is a mini web service that manipulate IPTV playlist adding user-agent to the end of channel link.
This fix Kodi user-agent problem.

Steps:
- Install Python 3.x
- Open terminal and type this: pip install flask
- Open file run.py and customize IPTV link
- Run file run.py
- Open Kodi
- Configure Kodi plugin IPTV to fetch playlist from url http://127.0.0.1:65432
