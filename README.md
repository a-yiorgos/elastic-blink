# elastic-blink
Use a BlinkStick to monitor the health of an ElasticSearch cluster

BlinkStick is a simple USB driven LED that you can control programmatically
from a programming language like Python. Using a couple of scripts and just a
few lines of Python, it is fairly easy to have it report to you the status of
your ElasticSearch cluster (green, yellow, red) so that you can have a quick
visual alert.

- check_elastic_health.py can be run via cron(8) or a monitor like nagios. By making use of ElasticSearch's [Cluster Health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html) and BlinkStick's [Website API](https://www.blinkstick.com/help/website-api) it sets the color of the LED to the appropriate state.

- elastic-blink.py is a program [from the BlinkStick wiki](https://github.com/arvydas/blinkstick-python/wiki/Example%3A-Control-Remotely) that is used to figure out what the color of the LED should be according to the value set via the Website API and act accordingly.

You need to edit both scripts and set the appropriate variables. 
