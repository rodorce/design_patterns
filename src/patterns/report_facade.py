from patterns.print_report import PrintReport
from patterns.web_report import WebReport

class ReportFacade:
    def generateReports(self, webReport: WebReport, printReport: PrintReport):
        web_content = webReport.create_content()
        webReport.create_file(web_content)

        print_content = printReport.create_content()
        printReport.create_file(print_content)