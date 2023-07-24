# Anomaly command detection

Simple example that uses pandas and numpy to detect repetitive commands:

It first calculates the time difference between successive commands and then looks for two types of anomalies: commands that occur too frequently (more than once per hour) and commands that are repeated. Note that these are just simple rules for detecting anomalies and may not be suitable for all scenarios.

The output of this code is a list of all commands that are considered anomalous (i.e., have a value of 1 in the "anomaly" column). We can adjust the threshold values and rules to fine-tune the anomaly detection process based on your specific requirements.

## Example execution

This is the CSV example:

![image](https://github.com/cguz/detect-anomaly-command-spacecraft/assets/15159632/8a8c04ce-2791-495e-8142-e7933de328f1)

This is the output with commands that occur too frequently (e.g., more than once per hour)

![image](https://github.com/cguz/detect-anomaly-command-spacecraft/assets/15159632/0630215d-f828-4196-b3bc-d1a846b8174d)

And this example if we increase the thresdhold to three hours:

