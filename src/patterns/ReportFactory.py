from patterns.print_report import PrintReport
from patterns.web_report import WebReport


def get_report(report_type: str, csv: list):
    if report_type == "web":
        return WebReport("some header title", csv)
    elif report_type == "print":
        return PrintReport("some header title", csv)
    else:
        raise Exception("Report type unknown")