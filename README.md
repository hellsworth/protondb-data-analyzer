## Collect data from the protondb reports

Protondb publishes monthly data on https://github.com/bdefore/protondb-data

If you grab any of those report tarballs and unpack it, the resulting filename is 'reports_piiremoved.json'.

The `analyze-protondb-reports.py` script will analyze one report.

Note that unfortunately it seems Valve stoppped putting the "result" in the json files starting from Dec 2019. So this script only works for Nov 2018 - Nov 2019.
